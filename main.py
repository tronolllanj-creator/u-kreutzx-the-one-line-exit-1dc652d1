"""Write the wedding elopement message to the designated output file."""

import os

LINE = "Dear Bride and Groom, midway through the cake cutting I eloped with your head caterer, so consider this my resignation."
# Entry validated: output is 1-140 chars, one line, deterministic.


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("Content failed validation")
    
    # Ensure main output directory exists
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")
    
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
