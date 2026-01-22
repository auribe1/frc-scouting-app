from storage import get_unsynced_entries, mark_entry_synced
import requests

url = "http://127.0.0.1:8000/entries"

def sync():
    unsynced = get_unsynced_entries()
    print(f"Found {len(unsynced)} unsynced entr{'y' if len(unsynced) ==1 else 'ies'}")
    if not unsynced:
          return
    payload = {"entries": unsynced}
    

    try:
        response = requests.post(url, json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        print("Upload failed:", e)
        return

    # If server didn't accept it, dont mark anything synced
    print("status code:", response.status_code)
    if response.status_code != 200:
        print("Upload failed. Body:", response.text)
        return
    
    try:
        data = response.json()
    except ValueError:
        print("Upload failed: server did not return Json. Body: ", response.text)
        return
    
    print("response json:", data)

    stored = data.get("stored")
    skipped = data.get("skipped")
    if not isinstance(stored, int):
        print("Upload failed: server response missing integer 'stored'. Not marking anything synced.")
        return
    
    #This assumes server only “skips” entries that already exist (same entryID). If server starts skipping invalid entries, this must change.
    if (stored + skipped) != len(unsynced):
        print(
            f"Server stored {stored}/{len(unsynced)} entries. "
            f"Not marking anything synced to avoid lying."
        )
        return
   
    #for every unsynced entry, go through and mark them synced, which also goes through and overwrites the file.
    marked = 0
    for e in unsynced:
            entry_id = e.get("entryID")
            if not entry_id:
                 continue
            print("Uploading entry:", entry_id)
            #pretend upload went through
            ok = mark_entry_synced(entry_id)
            if ok:
                marked += 1

    print(f"Marked {marked} entries as synced locally")

if __name__ == "__main__":
      sync()