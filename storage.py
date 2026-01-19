import json
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

ENTRIES_PATH = DATA_DIR / "entries.jsonl"

def make_entry_key(e: dict) -> tuple:
    return(
        e.get("event"),
        int(e.get("match_number", -1)),
        int(e.get("team number", -1)),
        e.get("scouter"),
    )

#allows us to rewrite an entries file.
def rewrite_entries(entries:list[dict]) -> None:
   
    with open(ENTRIES_PATH, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e) + "\n")

#marks one entry that is passed in as synced. Returns true if the entry gets synced. The time complexity won't be a huge deal since we won't have too many entries but we'll switch to SQLite eventually.
def mark_entry_synced(entry_id: str) -> bool:
    
    entries = load_entries()
    updated = False
    now = datetime.now(timezone.utc).isoformat()

    for e in entries:
        if e.get("entryID") == entry_id:
            e["synced_at"] = now
            updated = True
            break
    if updated:
        rewrite_entries(entries)
    
    return updated

#finds all the unsynced entries
def get_unsynced_entries() -> list[dict]:
    entries = load_entries()
    return [e for e in entries if not e.get("synced_at")]


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
    """Append a single scouting entry if not duplicate
        Returns True if saved, false if duplicate
    """

    entries = load_entries()
    existing_keys = {make_entry_key(e) for e in entries}

    key = make_entry_key(entry)

    if key in existing_keys:
        print("Duplicate entry detected. Not saved: ", key)
        return False
    
    with open(ENTRIES_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    print("Saved entry to", ENTRIES_PATH)
    return True
