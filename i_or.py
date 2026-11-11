import json
from pathlib import Path
PROFILE_FILE = Path(__file__).parent / "game_history.json"

def reading_from_json():
    if not PROFILE_FILE.exists():
        return []

    with open(PROFILE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def writing_for_json(new_profile):
    history_list = reading_from_json()
    history_list.append(new_profile)

    with open(PROFILE_FILE, "w", encoding="utf-8") as file:
        json.dump(history_list, file, indent=2, ensure_ascii=False)



