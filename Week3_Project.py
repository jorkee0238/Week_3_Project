from datetime import datetime

def convertData(data):
    selected_spreadsheet = 1
    if selected_spreadsheet == 1:
        # F to C formula: (F - 32) * 5/9
        return (data - 32) * 5 / 9
    elif selected_spreadsheet == 2:
        # lbs to Kg formula: lbs / 2.205
        return data / 2.205
    elif selected_spreadsheet == 3:
        # in to cm formula: in * 2.54
        return data * 2.54
    else:
        return data

def getInput():
    try:
        num_entries = int(input("How many entries are being entered? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for i in range(num_entries):
        print(f"\n--- Entry {i + 1} ---")
        entry_date = input("Enter the date: ")
        
        try:
            entry_value = float(input("Enter the highest temp value: "))
        except ValueError:
            print("Invalid numeric value. Skipping entry.")
            continue

        converted_value = convertData(entry_value)

        print(f"The following was saved at {datetime.now()}: Date: {entry_date}, Value: {entry_value}, Converted Value: {converted_value}")


def main():
    
    print("jorkee0238 Spreadsheet Automation Menu")

    print("Please select from an option below:")
    print("1. Input Data")
    print("2. View Current Date")
    print("3. Generate Report")

    selection = input()
    now = datetime.now()

    print(f"You chose {selection} at {now}")

    if selection == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")

if __name__ == "__main__":
    main()
