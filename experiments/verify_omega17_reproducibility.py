"""Reproduce Ω-17 directly from the committed implementation and preserve raw runs.

This checks aggregate agreement with the 2026-10-09 report but does not treat a
matching toy-network result as physical evidence.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments" / "relational_fabric_connectivity_memory_controls.py"
EXPECTED = ROOT / "results" / "2026-10-09-relational-fabric-connectivity-memory-controls.json"
OUTPUT = ROOT / "results" / "2026-10-10-relational-fabric-connectivity-memory-controls-reproduction.json"
SEED_START = 20261100
SEED_COUNT = 40
TOLERANCE = 1e-8


def load_module():
    spec = importlib.util.spec_from_file_location("omega17_committed_source", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load committed Ω-17 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compare_numbers(actual, expected, path=""):
    differences = []
    if isinstance(actual, dict) and isinstance(expected, dict):
        for key in sorted(set(actual) & set(expected)):
            differences.extend(compare_numbers(actual[key], expected[key], f"{path}.{key}"))
    elif isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        delta = abs(float(actual) - float(expected))
        if delta > TOLERANCE:
            differences.append({"path": path, "actual": actual, "expected": expected, "abs_delta": delta})
    return differences


def main():
    module = load_module()
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    runs = [
        row
        for i in range(SEED_COUNT)
        for row in module.run_seed(SEED_START + i)
    ]
    summary = module.summarize(runs)
    paired = {
        "learned_minus_permuted_domain_retention": module.paired(
            runs, "frozen_learned_norm", "permuted_learned_norm", "domain_retention"
        ),
        "learned_minus_degreebin_domain_retention": module.paired(
            runs, "frozen_learned_norm", "degreebin_permuted_norm", "domain_retention"
        ),
        "learned_minus_original_domain_retention": module.paired(
            runs, "frozen_learned_norm", "fixed_original", "domain_retention"
        ),
        "learned_minus_permuted_patch_recovery": module.paired(
            runs, "frozen_learned_norm", "permuted_learned_norm", "patch_recovery"
        ),
    }
    expected_run_counts = {mode: sum(r["mode"] == mode for r in runs) for mode in sorted({r["mode"] for r in runs})}
    edge_counts = sorted({int(r["edges"]) for r in runs})
    edge_count_histogram = {
        str(edge_count): sum(int(r["edges"]) == edge_count for r in runs)
        for edge_count in edge_counts
    }
    differences = compare_numbers(summary, expected.get("summary", {}), "summary")
    differences.extend(compare_numbers(paired, expected.get("paired_comparisons", {}), "paired_comparisons"))
    source_sha256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    metadata_matches = (
        bool(edge_counts)
        and all(edge == expected.get("metadata", {}).get("edges_per_graph") for edge in edge_counts)
    )
    status = "SUMMARY_MATCH_METADATA_CORRECTED" if not differences and not metadata_matches else (
        "SUMMARY_MATCH" if not differences else "SUMMARY_MISMATCH"
    )
    output = {
        "metadata": {
            "experiment": "Ω-17 — direct clean-checkout reproduction",
            "date": "2026-10-10",
            "status": status,
            "source_path": str(SOURCE.relative_to(ROOT)),
            "source_sha256": source_sha256,
            "runs_per_condition": SEED_COUNT,
            "total_condition_runs": len(runs),
            "observed_condition_counts": expected_run_counts,
            "nodes": 160,
            "observed_edge_count_histogram": edge_count_histogram,
            "previous_reported_edges_per_graph": expected.get("metadata", {}).get("edges_per_graph"),
            "previous_edge_metadata_matches_execution": metadata_matches,
            "previous_reported_raw_run_count": len(expected.get("runs", [])),
            "summary_tolerance": TOLERANCE,
            "interpretation": "Toy network only; not evidence about physical matter or universal laws.",
        },
        "summary": summary,
        "paired_comparisons": paired,
        "comparison_with_2026_10_09_report": {
            "matches_within_tolerance": not differences,
            "differences": differences,
        },
        "runs": runs,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": status,
        "total_condition_runs": len(runs),
        "condition_counts": expected_run_counts,
        "edge_count_histogram": edge_count_histogram,
        "previous_reported_raw_run_count": len(expected.get("runs", [])),
        "summary_matches_previous_report": not differences,
        "difference_count": len(differences),
        "output": str(OUTPUT.relative_to(ROOT)),
    }, indent=2, sort_keys=True))
    if differences:
        print(json.dumps(differences[:50], indent=2, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
