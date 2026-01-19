import csv
from pathlib import Path
from storage import load_entries

from storage import BASE_DIR, DATA_DIR

def export_entries_to_csv(out_path: Path):
    entries = load_entries()
    if not entries:
        print("No entries to export")
        return
    
    for e in entries:
        if e.get("synced_at") is None:
            e["synced_at"] = ""


    #this basically matches the data we have to these field names set up as the headers
    fieldnames = [
    "entryID", "createdAt", "synced_at",
    "event", "match_number", "team_number", "scouter",
    "auto_mobility", "auto_pieces",
    "teleop_pieces", "defense", "defense_rating",
    "climb_type", "climb_success",
    "penalties", "breakdown", "notes"
]

#use the out path that was passed in, write to that file using the fieldnames we wrote and put in each entry as a row
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer= csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(entries)

    print(f"Exported {len(entries)} entries to {out_path}")

if __name__ ==  "__main__":
    #setting our output directory to be in the data folder giving it the name entries.csv. Then we call the function using that file path.
    out_csv = DATA_DIR / "entries.csv"
    export_entries_to_csv(out_csv)