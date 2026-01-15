from typing import List, Dict, Any

def team_summary(entries: List[Dict[str, Any]], team_number: int) -> str:
    team_entries = [e for e in entries if e.get("team_number") == team_number]

    if not team_entries:
        print(f"No entries found for team {team_number}")
        return
    
    n = len(team_entries)
    avg_auto = sum(e.get("auto_pieces", 0) for e in team_entries) / n
    avg_tele = sum(e.get("teleop_pieces", 0 ) for e in team_entries) / n
    avg_pen = sum(e.get("penalties", 0) for e in team_entries ) / n

    climb_successes = sum(1 for e in team_entries if e.get("climb_success", False))
    climb_rate = (climb_successes / n) * 100

    breakdowns = sum(1 for e in team_entries if e.get("breakdown", False))

    defense_avg = sum(e.get("defense_rating", 0) for e in team_entries) / n

    lines = [
        f"Team {team_number} summary ({n} match(es))",
        f"- Avg auto pieces: {avg_auto:.2f}",
        f"- Avg teleop pieces: {avg_tele:.2f}",
        f"- Avg defense rating: {defense_avg:.2f}/5",
        f"- Climb success rate: {climb_rate:.0f}%",
        f"- Avg penalties: {avg_pen:.2f}",
        f"- Breakdowns: {breakdowns}",
    ]

    return "\n".join(lines)

def list_entries(entries):
    if not entries:
        return "No entries saved"
    
    lines = ["Saved entries:"]
    for e in entries:
        lines.append(
            f'M{e.get("match_number")} | '
            f'Team {e.get("team_number")} |'
            f'Scout: {e.get("scouter")} |'
            f'Auto: {e.get("auto_pieces")} | '
            f'Tele: {e.get("teleop_pieces")} | '
            f'Def: {e.get("defense_rating")}/5 | '
            f'Climb: {e.get("climb_type")} {"✅" if e.get("climb_success") else "❌"}'
        ) 

    return "\n".join(lines)