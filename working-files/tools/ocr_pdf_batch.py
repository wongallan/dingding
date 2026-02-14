import argparse
from pathlib import Path

import fitz
from rapidocr_onnxruntime import RapidOCR


def run(pdf_path: Path, start_page: int, end_page: int, out_path: Path) -> None:
    ocr = RapidOCR()
    doc = fitz.open(pdf_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(f"# OCR Batch Output")
    lines.append("")
    lines.append(f"- Source file: {pdf_path.name}")
    lines.append(f"- Page range: {start_page}-{end_page}")
    lines.append("")

    for page_no in range(start_page, end_page + 1):
        page = doc[page_no - 1]
        pix = page.get_pixmap(dpi=220)
        img_bytes = pix.tobytes("png")
        result, _ = ocr(img_bytes)

        lines.append(f"## Page {page_no}")
        if not result:
            lines.append("- [[unclear]] No OCR result")
            lines.append("")
            continue

        for item in result:
            points, text, score = item
            if text and text.strip():
                try:
                    score_text = f"{float(score):.2f}"
                except (TypeError, ValueError):
                    score_text = str(score)
                lines.append(f"- ({score_text}) {text.strip()}")

        lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    run(Path(args.pdf), args.start, args.end, Path(args.out))


if __name__ == "__main__":
    main()
