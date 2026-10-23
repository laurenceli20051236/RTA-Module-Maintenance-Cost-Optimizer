#!/usr/bin/env python3
"""End-to-end self-test with synthetic sources (no network, no paid APIs)."""

import csv
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
STUDY = [sys.executable, "-I", str(HERE / "study.py")]


def run(root, *args, expect=0):
    r = subprocess.run(STUDY + ["--root", str(root), *args], capture_output=True, text=True)
    assert r.returncode == expect, f"{args} rc={r.returncode} (want {expect})\n{r.stdout}\n{r.stderr}"
    return r.stdout


def make_sources(src: Path):
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet
    import docx

    st = getSampleStyleSheet()["Normal"]
    SimpleDocTemplate(str(src / "synthetic_rta_paper.pdf"), pagesize=A4).build([
        Paragraph("Synthetic RTA Study. The lamp lifetime is 1200 hours at rated power.", st),
        Paragraph("tau = R * C", st),
        PageBreak(),
        Paragraph("Table 1 lists maintenance cost per module.", st),
        Table([["Module", "Cost (USD)"], ["Lamp", "450"], ["Pyrometer", "900"]],
              style=[("GRID", (0, 0), (-1, -1), 0.5, "black")]),
    ])
    d = docx.Document()
    d.add_paragraph("Chamber leak rate must stay below 2 mTorr/min per the synthetic spec.")
    d.save(src / "synthetic_spec.docx")
    (src / "notes.md").write_text("Wafer throughput is 40 wph.\nE = m * c\n", encoding="utf-8")
    (src / "notes_copy.md").write_text("Wafer throughput is 40 wph.\nE = m * c\n", encoding="utf-8")  # duplicate
    (src / "ignored.xyz").write_text("x")


def main():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "study"
        run(root, "init")
        make_sources(root / "sources")
        out = run(root, "inventory")
        assert "ignored.xyz" in out and "3 sources" in out, out  # dedup by hash + unsupported reported
        run(root, "extract")
        out = run(root, "extract", "--force")
        assert "'table': 1" in out and "'equation': 1" in out, out

        import json
        inv = json.loads((root / "ledger" / "inventory.json").read_text())["sources"]
        sid = {Path(v["path"]).name: k for k, v in inv.items()}
        PDF, DOCX = sid["synthetic_rta_paper.pdf"], sid["synthetic_spec.docx"]
        run(root, "matrix-init")
        rows = [
            ["C001", "Lamp lifetime is 1200 h", PDF, "p.1", "lamp lifetime is 1200 hours", "direct", "high", ""],
            ["C002", "Pyrometer costs 900 USD", PDF, "p.2 table 1", "Pyrometer | 900", "direct", "high", ""],
            ["C003", "Leak spec", DOCX, "para 1", "below 2 mTorr/min", "direct", "medium", ""],
        ]
        ev = root / "ledger" / "evidence.csv"
        with ev.open("a", newline="") as fh:
            csv.writer(fh).writerows(rows)
        run(root, "matrix")

        (root / "drafts" / "ch1.md").write_text(
            "# Chapter 1\n\nLamp life is 1200 hours [C001] and the leak limit holds [@" + DOCX + " para 1].\n\n"
            "The time constant follows tau = R C [@" + PDF + " p.1].\n\n$$\\Delta x = N v$$ {own}\n", encoding="utf-8")
        run(root, "qa")
        run(root, "export", "--name", "ch1", "--formats", "md", "docx", "pdf")
        for ext in ("md", "docx", "pdf"):
            f = root / "export" / f"ch1.{ext}"
            assert f.exists() and f.stat().st_size > 150, f
        import shutil as _sh
        if _sh.which("pdftotext"):
            txt = subprocess.run(["pdftotext", str(root / "export" / "ch1.pdf"), "-"], capture_output=True, text=True).stdout
            import unicodedata
            flat = unicodedata.normalize("NFKC", txt).replace(" ", "").replace("\n", "")
            assert "Δx=Nv" in flat, "equation missing from PDF"
        assert PDF in (root / "export" / "ch1.md").read_text() and "sha256" in (root / "export" / "ch1.md").read_text()

        # negative controls: every traceability failure must be caught
        with ev.open("a", newline="") as fh:
            csv.writer(fh).writerow(["C004", "Fabricated", PDF, "p.1", "not in the paper", "direct", "low", ""])
            csv.writer(fh).writerow(["C005", "Bad loc", PDF, "p.9", "x", "direct", "low", ""])
            csv.writer(fh).writerow(["C006", "Ghost source", "S099", "p.1", "x", "direct", "low", ""])
            csv.writer(fh).writerow(["C007", "Inferred no note", PDF, "p.1", "", "inferred", "low", ""])
        out = run(root, "matrix", expect=1)
        for needle in ("quote not found", "p.9", "S099", "need a note"):
            assert needle in out, needle
        (root / "drafts" / "bad.md").write_text(
            "Uses C004 [C004] and ghost [@S042 p.1] and bad page [@" + PDF + " p.7] and no locator [@" + PDF + "].\n\n"
            "The yield rose to 97 percent in the pilot run.\n", encoding="utf-8")
        out = run(root, "qa", str(root / "drafts" / "bad.md"), expect=1)
        for needle in ("C004", "S042", "p.7", "no locator", "numeric statement"):
            assert needle in out, needle
        run(root, "export", str(root / "drafts" / "bad.md"), "--name", "bad", "--formats", "md", expect=1)
        print("SELFTEST PASSED")


if __name__ == "__main__":
    main()
