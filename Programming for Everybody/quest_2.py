file_name = input("Enter the file name: ")

count = 0
total = 0.0
maximum = None

with open(file_name, "r") as file_handle:
    for line in file_handle:
        if not line.startswith("X-DSPAM-Probability:"):
            continue

        value = float(line.split(":", 1)[1].strip())
        count += 1
        total += value

        if maximum is None or value > maximum:
            maximum = value

if count == 0:
    print("No X-DSPAM-Probability values found.")
else:
    print(f"Maximum probability: {maximum:.4f}")
    print(f"Average probability: {total / count:.4f}")

