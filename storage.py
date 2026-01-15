import json
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

ENTRIES_PATH = DATA_DIR / "entries.jsonl"

def load_entries() -> List[Dict[str, Any]]:
    """Load JSONL scouting entries"""
    entries =[]
    if not ENTRIES_PATH.exists():
        print("nothing here")
        return entries
    

    print("Reading entries from:", ENTRIES_PATH)
    with open(ENTRIES_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entries.append(json.loads(line))
    return entries

def save_entry(entry: Dict[str, Any]) -> None:
    """Append a single scouting entry"""
    with open(ENTRIES_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

