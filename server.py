from fastapi import FastAPI
from pathlib import Path
import json
from typing import Any

from main import Base_Dir, Data_Dir

Server_Entries_Path = Data_Dir / "server_entries.jsonl"

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/health")
async def health():
    return {"message" : "yogurt"}

#will return all existing entry ids after reading server_entries
def load_existing_entry_ids() -> set[str]:
    ids = set()
    if not Server_Entries_Path.exists():
        return ids
    
    with open(Server_Entries_Path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                entry_id = entry.get("entryID")
                if entry_id:
                    ids.add(entry_id)
            except json.JSONDecodeError:
                continue

    return ids
@app.post("/entries/")
async def upload_entries(payload : dict[str,Any]):
    """
    Expect Json like:

    {
        "entries: [ {entry1}, {entry2} ...]
    }
    """

    entries = payload.get("entries", [])
    if not isinstance(entries, list):
        return {"error" : "entries must be a list"}
    
    existing_ids = load_existing_entry_ids()

    received = len(entries)
    stored = 0
    skipped = 0

    with open(Server_Entries_Path, "a", encoding="utf-8") as f:
        for entry in entries:
            entry_id = entry.get("entryID")
            if not entry_id:
                skipped += 1
                continue

            if entry_id in existing_ids:
                skipped += 1
                continue

            f.write(json.dumps(entry) + "\n")
            existing_ids.add(entry_id)
            stored += 1

    return {"received": received, "stored" : stored, "skipped" : skipped}

    