from pathlib import Path


def load_instruction_from_file(filename: str) -> str:
    path = Path(__file__).parent / filename
    return path.read_text(encoding="utf-8")