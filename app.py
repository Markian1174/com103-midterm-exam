# com103-midterm-exam
chore_names = ["Sweeping / Mopping", "Dishwashing", "Taking Out Trash",
               "Cleaning Bathroom", "Buying Groceries"]
chore_frequency = ["Daily", "After meals", "Every other day", "Weekly", "Weekly"]

print("=" * 50)
print("DORM ROOM -- CHORE LIST")
print("=" * 50)

# Room monitor name (non-empty, no digits, no spaces)
while True:
    room_monitor = input("Room monitor name: ").strip()
    
    if room_monitor == "":
        print("Cannot be empty.")
        continue
    if " " in room_monitor:
        print("No spaces allowed in name.")
        continue
    if any(ch.isdigit() for ch in room_monitor):
        print("Name cannot contain numbers.")
        continue
    break

# Room number (single digit: 1-5 only)
while True:
    raw_room = input("Room number (1-5): ").strip()
    if raw_room == "":
        print("Room number cannot be empty. Please enter a number.")
        continue
    if len(raw_room) != 1:
        print("Room number must be a single digit only (1-5).")
        continue
    try:
        room_number = int(raw_room)
    except ValueError:
        print("Invalid number. Please enter a valid single digit (1-5).")
        continue
    if room_number < 1 or room_number > 5:
        print("Room number must be between 1 and 5.")
        continue
    break

# Display chore list
print("\n" + "=" * 50)
print("   DORM ROOM -- CHORE LIST")
print("=" * 50)
for i in range(len(chore_names)):
    print(f"{i + 1}. {chore_names[i]:<25} [{chore_frequency[i]}]")
print("=" * 50)

# Assignment lists
assigned_chores = []
assigned_roommates = []
assigned_status = []

# Allowed status inputs
allowed_done = {"done", "d", "yes", "y"}
allowed_not_done = {"not done", "not_done", "notdone", "n", "no", "incomplete"}

# Accept chore assignments 4 times
for chore_slot in range(1, 5):
    print(f"\n--- CHORE {chore_slot} ---")

    # Chore number loop (0 to skip), using integer validation (allows multi-digit)
    while True:
        raw = input(f"Chore number (0 to skip) — enter an integer between 1 and {len(chore_names)}: ").strip()
        if raw == "":
            print(f"Input cannot be empty. Enter 0 to skip or an integer between 1 and {len(chore_names)}.")
            continue
        try:
            num = int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer (0 to skip or a chore number).")
            continue
        if num == 0:
            chore_number = 0
            break
        if 1 <= num <= len(chore_names):
            chore_number = num
            break
        print(f"Invalid chore number. Enter 0 to skip or an integer between 1 and {len(chore_names)}.")

    if chore_number == 0:
        print(f"Chore {chore_slot} : skipped (chore = 0)")
        continue

    # Roommate name (non-empty)
    while True:
        roommate_name = input("Roommate name: ").strip()
        if roommate_name != "":
            break
        print("Roommate name cannot be empty. Please enter a name.")

    # Status (validated, case-insensitive)
    while True:
        raw_status = input("Status (done/not done): ").strip()
        if raw_status == "":
            print("Status cannot be empty. Please enter 'done' or 'not done'.")
            continue
        sval = raw_status.lower().replace("_", " ").strip()
        if sval in allowed_done:
            status = "done"
            break
        if sval in allowed_not_done:
            status = "not done"
            break
        print("Unrecognized status. Please type 'done' or 'not done' (or y/n).")

    assigned_chores.append(chore_number)
    assigned_roommates.append(roommate_name)
    assigned_status.append(status)

# Count completed chores and completion rate
completed_count = sum(1 for s in assigned_status if s == "done")

total_assigned = len(assigned_chores)
completion_rate = int((completed_count / total_assigned) * 100) if total_assigned > 0 else 0

# Determine room status tag
if completion_rate == 100:
    room_status = "ROOM IS SPOTLESS!"
elif completion_rate >= 50:
    room_status = "ALMOST THERE!"
else:
    room_status = "NEEDS CATCHING UP!"

# Print formatted chore report
print("\n" + "=" * 45)
print("ROOM " + str(room_number) + " -- WEEKLY CHORE REPORT")
print("=" * 45)
print(f"Room Monitor:{room_monitor}\n")

for i in range(len(assigned_chores)):
    chore_num = assigned_chores[i]
    chore_name = chore_names[chore_num - 1]
    chore_freq = chore_frequency[chore_num - 1]
    roommate = assigned_roommates[i]
    status = assigned_status[i]

    print(f"[{i + 1}] {chore_name:<25} [{chore_freq}]")
    print(f"    Roommate:{roommate}")
    print(f"    Status:{status}\n")

print("=" * 45)
print(f"Completed:{completed_count} out of {total_assigned} assigned")
print(f"Completion Rate:{completion_rate}%")
print(f"Room Status:{room_status}")
print("=" * 45)
