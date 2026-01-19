from storage import get_unsynced_entries, mark_entry_synced

def sync():
    unsynced = get_unsynced_entries()
    print(f"Found {len(unsynced)} unsynced entr{'y' if len(unsynced) ==1 else 'ies'}")

    #simulate upload
    #for every unsynced entry, go through and mark them synced, which also goes through and overwrites the file.
    for e in unsynced:
            entry_id = e.get("entryID")
            print("Uploading entry:", entry_id)

            #pretend upload went through
            ok = mark_entry_synced(entry_id)

if __name__ == "__main__":
      sync()