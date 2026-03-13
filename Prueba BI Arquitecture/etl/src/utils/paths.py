from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR.parent / "temp" / "data"
RESULT_DIR = BASE_DIR.parent / "temp" / "result"