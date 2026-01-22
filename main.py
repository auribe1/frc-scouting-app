import json
from pathlib import Path
from models import ScoutingEntry
from storage import load_entries, save_entry, validate_entry
from reports import team_summary, list_entries

Base_Dir = Path(__file__).resolve().parent
Data_Dir = Base_Dir / "data"
Data_Dir.mkdir(exist_ok=True)
Entries_Path = Data_Dir / "entries.json1"



if __name__ == "__main__":
    """ code for testing duplicate entries 
    
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
    

    save_entry(entry.to_dict())


    entries = load_entries()
    
    """
    entry = ScoutingEntry.new(
    event="TestEvent",
    match_number=1,
    team_number=1678,
    scouter="Ariel",
    auto_mobility=True,
    auto_pieces=22,
    teleop_pieces=999,
    defense=True,
    defense_rating=4,
    climb_type="high",
    climb_success=True,
    penalties=0,
    breakdown=True,
    notes="Looks consistent."
    )
    

    entryDict = entry.to_dict()
    try:
        save_entry(entryDict)
    except (KeyError, ValueError) as e:
        print(f"Not saved: {e}")



    entries = load_entries()
    
    #print(f"Loaded {len(entries)} entries")
    print(list_entries(entries))
    print()
    team_summary(entries, team_number=254)



   # save_entry(sample)