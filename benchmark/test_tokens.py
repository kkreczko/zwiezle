"""
Benchmark tokenów: empiryczny pomiar redukcji zużycia tokenów dla skilla zwięźle.
Tokenizer: o200k_base (Claude / GPT-4o).
"""

import json
from collections import defaultdict
from pathlib import Path

import tiktoken
from tabulate import tabulate

from samples import SAMPLES

ENCODING = tiktoken.get_encoding("o200k_base")
REPORT_PATH = Path(__file__).parent / "REPORT.md"
RESULTS_JSON = Path(__file__).parent / "results.json"


def count_tokens(text: str) -> int:
    return len(ENCODING.encode(text))


def run_benchmark() -> dict:
    """Uruchom benchmark i zwróć wyniki jako dict."""
    results = []

    for category, mode, normal, terse in SAMPLES:
        normal_tokens = count_tokens(normal)
        terse_tokens = count_tokens(terse)
        savings_pct = round((1 - terse_tokens / normal_tokens) * 100, 1)

        results.append({
            "category": category,
            "mode": mode,
            "normal_tokens": normal_tokens,
            "terse_tokens": terse_tokens,
            "savings_pct": savings_pct,
        })

    return {"samples": results}


def aggregate_by_mode(results: dict) -> dict[str, dict]:
    """Agreguj wyniki per tryb (średnia oszczędność)."""
    mode_data: dict[str, list[float]] = defaultdict(list)
    for sample in results["samples"]:
        mode_data[sample["mode"]].append(sample["savings_pct"])

    aggregated = {}
    for mode, savings in sorted(mode_data.items()):
        aggregated[mode] = {
            "mean_savings_pct": round(sum(savings) / len(savings), 1),
            "min_savings_pct": round(min(savings), 1),
            "max_savings_pct": round(max(savings), 1),
            "n_samples": len(savings),
        }
    return aggregated


def aggregate_by_category(results: dict) -> dict[str, dict]:
    """Agreguj wyniki per kategoria (średnia oszczędność)."""
    cat_data: dict[str, list] = defaultdict(list)
    for sample in results["samples"]:
        cat_data[sample["category"]].append(sample)

    aggregated = {}
    for cat, samples in cat_data.items():
        normal_total = sum(s["normal_tokens"] for s in samples)
        terse_total = sum(s["terse_tokens"] for s in samples)
        aggregated[cat] = {
            "normal_tokens_avg": round(normal_total / len(samples), 1),
            "terse_tokens_avg": round(terse_total / len(samples), 1),
            "mean_savings_pct": round(
                sum(s["savings_pct"] for s in samples) / len(samples), 1
            ),
        }
    return aggregated


def generate_report(results: dict) -> str:
    """Generuj raport markdown."""
    by_mode = aggregate_by_mode(results)
    by_category = aggregate_by_category(results)

    lines = [
        "# Benchmark redukcji tokenów — wyniki empiryczne",
        "",
        f"Tokenizer: `o200k_base` | Próbek: {len(results['samples'])}",
        "",
        "## Wyniki per tryb (średnia ze wszystkich kategorii)",
        "",
    ]

    mode_table = []
    for mode, data in by_mode.items():
        mode_table.append([
            mode,
            f"{data['mean_savings_pct']}%",
            f"{data['min_savings_pct']}%",
            f"{data['max_savings_pct']}%",
            data["n_samples"],
        ])

    lines.append(tabulate(
        mode_table,
        headers=["Tryb", "Średnia oszcz.", "Min", "Max", "N"],
        tablefmt="github",
    ))
    lines.append("")

    lines.append("## Wyniki per kategoria (średnia ze wszystkich trybów)")
    lines.append("")

    cat_table = []
    for cat, data in by_category.items():
        cat_table.append([
            cat,
            data["normal_tokens_avg"],
            data["terse_tokens_avg"],
            f"{data['mean_savings_pct']}%",
        ])

    lines.append(tabulate(
        cat_table,
        headers=["Kategoria", "Norm. tok. (śr.)", "Zwięzłe tok. (śr.)", "Oszcz. (śr.)"],
        tablefmt="github",
    ))
    lines.append("")

    lines.append("## Szczegółowe wyniki")
    lines.append("")

    detail_table = []
    for s in results["samples"]:
        detail_table.append([
            s["category"],
            s["mode"],
            s["normal_tokens"],
            s["terse_tokens"],
            f"{s['savings_pct']}%",
        ])

    lines.append(tabulate(
        detail_table,
        headers=["Kategoria", "Tryb", "Normal tok.", "Zwięzłe tok.", "Oszczędność"],
        tablefmt="github",
    ))
    lines.append("")

    return "\n".join(lines)


# ============================================================================
# Testy pytest
# ============================================================================


def test_all_samples_have_savings():
    """Każdy tryb powinien dawać jakąś oszczędność vs normalna odpowiedź."""
    results = run_benchmark()
    for sample in results["samples"]:
        # suwalsko3 może mieć ujemne oszczędności — to jest oczekiwane
        if sample["mode"] == "suwalsko3":
            continue
        assert sample["savings_pct"] > 0, (
            f"{sample['category']}/{sample['mode']}: "
            f"brak oszczędności ({sample['savings_pct']}%)"
        )


def test_polsko_ordering():
    """polsko1 < polsko2 < polsko3 w oszczędnościach (per kategoria)."""
    results = run_benchmark()
    by_cat_mode: dict[str, dict[str, float]] = defaultdict(dict)
    for s in results["samples"]:
        if s["mode"].startswith("polsko"):
            by_cat_mode[s["category"]][s["mode"]] = s["savings_pct"]

    for cat, modes in by_cat_mode.items():
        assert modes["polsko1"] <= modes["polsko2"], (
            f"{cat}: polsko1 ({modes['polsko1']}%) > polsko2 ({modes['polsko2']}%)"
        )
        assert modes["polsko2"] <= modes["polsko3"], (
            f"{cat}: polsko2 ({modes['polsko2']}%) > polsko3 ({modes['polsko3']}%)"
        )


def test_terse_en_meaningful_savings():
    """terse-en powinien dawać co najmniej 20% oszczędności średnio."""
    results = run_benchmark()
    by_mode = aggregate_by_mode(results)
    assert by_mode["terse-en"]["mean_savings_pct"] >= 20, (
        f"terse-en średnia: {by_mode['terse-en']['mean_savings_pct']}% < 20%"
    )


def test_generate_report_and_save():
    """Generuj i zapisz raport + JSON wyników."""
    results = run_benchmark()
    report = generate_report(results)

    REPORT_PATH.write_text(report, encoding="utf-8")
    RESULTS_JSON.write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    assert REPORT_PATH.exists()
    assert RESULTS_JSON.exists()
    assert "Benchmark" in report
