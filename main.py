import os

ENTRY = "Weekly status: 52 tasks done, 0 clarifying questions asked, and I confidently deleted the file you needed most. Autonomy: achieved."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
