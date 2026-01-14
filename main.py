import json
from pathlib import Path
from models import ScoutingEntry

Base_Dir = Path(__file__).resolve().parent
Data_Dir = Base_Dir / "data"
Data_Dir.mkdir(exist_ok=True)
Entries_Path = Data_Dir / "entries.json1"

def load_entries():
    entries = []
    if not Entries_Path.exists():
        return entries
    
    with open(Entries_Path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entries.append(json.loads(line))
        return entries
    
def team_summary(entries, team_number: int):
    team_entries = [e for e in entries if e.get("team_number") == team_number]

    if not team_entries:
        print(f"No entries found for team {team_number}")
        return
    
    n = len(team_entries)
    avg_auto = sum(e.get("auto_pieces", 0) for e in team_entries) / n
    avg_tele = sum(e.get("teleop_pieces", 0 ) for e in team_entries) / n
    avg_pen = sum(e.get("penalties", 0) for e in team_entries ) / n

    climbs = [e.get("climb_success", False) for e in team_entries]
    climb_rate = (sum(1 for c in climbs if c) / n) * 100

    breakdowns = sum(1 for e in team_entries if e.get("breakdown", False))

    print(f"Team {team_number} summary ({n} match(es))")
    print(f"- Avg auto pieces: {avg_auto: .2f}")
    print(f"- Avg teleop pieces: {avg_tele: .2f}")
    print(f"- Climb success rate: {climb_rate: .0f}%")
    print(f"- Avg penalties: {avg_pen:.2f}")
    print(f"- Breakdowns: {breakdowns}")





def save_entry(entry: ScoutingEntry):
    out_path = Data_Dir / "entries.json1"
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry.to_dict()) + "\n")
    print("Saved entry to", out_path)

if __name__ == "__main__":
    
    entry = ScoutingEntry.new(
    event="TestEvent",
    match_number=1,
    team_number=125,
    scouter="Ariel",
    auto_mobility=True,
    auto_pieces=2,
    teleop_pieces=100,
    defense=False,
    defense_rating=4,
    climb_type="high",
    climb_success=True,
    penalties=0,
    breakdown=True,
    notes="Looks consistent."
)

    #save_entry(entry)


    entries = load_entries()
    print(f"Loaded {len(entries)} entries")

    team_summary(entries, team_number=125)



   # save_entry(sample)