import json
from pathlib import Path
from models import ScoutingEntry
from storage import load_entries
from reports import team_summary, list_entries

Base_Dir = Path(__file__).resolve().parent
Data_Dir = Base_Dir / "data"
Data_Dir.mkdir(exist_ok=True)
Entries_Path = Data_Dir / "entries.json1"



if __name__ == "__main__":
    '''
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
    '''

    #save_entry(entry)


    entries = load_entries()
    #print(f"Loaded {len(entries)} entries")
    print(list_entries(entries))
    print()
    team_summary(entries, team_number=125)



   # save_entry(sample)