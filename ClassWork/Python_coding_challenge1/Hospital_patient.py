def display_records():
    file = open("patients.txt", "r")

    print("\nAll Patient Records:")
    for line in file:
        print(line.strip())

    file.close()


def critical_patients():
    file = open("patients.txt", "r")

    print("\nCritical Patients:")
    for line in file:
        data = line.strip().split(",")

        if data[2] == "Critical":
            print(data[1])

    file.close()


def count_status():
    normal = 0
    stable = 0
    critical = 0

    file = open("patients.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if data[2] == "Normal":
            normal += 1
        elif data[2] == "Stable":
            stable += 1
        elif data[2] == "Critical":
            critical += 1

    file.close()

    print("\nPatient Count:")
    print("Normal :", normal)
    print("Stable :", stable)
    print("Critical :", critical)


def search_patient(pid):
    file = open("patients.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == pid:
            print("\nPatient Found:")
            print(line.strip())
            found = True
            break

    if not found:
        print("Patient Not Found.")

    file.close()


def save_critical():
    file = open("patients.txt", "r")
    output = open("critical_patients.txt", "w")

    for line in file:
        data = line.strip().split(",")

        if data[2] == "Critical":
            output.write(line)

    file.close()
    output.close()

    print("\nCritical Patient Report Generated Successfully.")


# Main Program
display_records()
critical_patients()
count_status()

pid = input("\nEnter Patient ID to Search: ")
search_patient(pid)

save_critical()