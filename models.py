from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import uuid

@dataclass
class ScoutingEntry:
    #Add more items to this list later like defense rating

    entryID: str
    createdAt : str

    event: str
    match_number: int
    team_number: int
    scouter: str

    auto_mobility: bool
    auto_pieces: int

    teleop_pieces: int
    defense: bool
    defense_rating : int #1-5

    climb_type: str
    climb_success: bool

    penalties: int
    breakdown: bool
    notes: str

    def __post_init__(self):
        if not (1 <= self.defense_rating <= 5):
            raise ValueError("defense_rating must be between 1 and 5")

    def to_dict(self):
        #turned all the scouting entry data into a dictionary
        return asdict(self)

    @staticmethod
    def new(
            event: str,
            match_number: int,
            team_number: int,
            scouter: str,

            auto_mobility: bool,
            auto_pieces: int,

            teleop_pieces: int,
            defense: bool,
            defense_rating : int, #1-5

            climb_type: str,
            climb_success: bool,

            penalties: int,
            breakdown: bool,
            notes: str,

    ):
        """Factory: creates a new entry with uuid + time stamp"""
        return ScoutingEntry(
            entryID= str(uuid.uuid4()),
            createdAt= datetime.now(timezone.utc).isoformat(),

            event=event,
            match_number=match_number,
            team_number=team_number,
            scouter=scouter,

            auto_mobility=auto_mobility,
            auto_pieces=auto_pieces,

            teleop_pieces=teleop_pieces,
            defense=defense,
            defense_rating=defense_rating,

            climb_type=climb_type,
            climb_success=climb_success,

            penalties=penalties,
            breakdown=breakdown,
            notes=notes
            )