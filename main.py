import os

ENTRY = "Weekly status: I completed 38 tasks, hallucinated 2 meetings, and confidently filed both under 'progress.'"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
