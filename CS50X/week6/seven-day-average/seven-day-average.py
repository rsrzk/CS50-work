import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = dict()
    prev_cases = dict()

    for row in reader:
        state = row["state"]
        cases = int(row["cases"])

        if state not in prev_cases:
            new_cases[state] = []
            new_case = cases
        else:
            new_case = cases - prev_cases[state]
            if len(new_cases[state]) >= 14:
                new_cases[state].pop(0)

        prev_cases[state] = cases
        new_cases[state].append(new_case)

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        current = 0
        prev = 0
        for day in new_cases[state][6:]:
            current += day
        for day in new_cases[state][:6]:
            prev += day
        current /= 7
        prev /= 7
        try:
            diff = current / prev - 1
            diff = diff * 100
        except ZeroDivisionError:
            raise ZeroDivisionError

        if current > prev:
            print(f"{state} had a 7-day average of {round(current)} and an increase of {round(diff)}%.")
        elif current < prev:
            print(f"{state} had a 7-day average of {round(current)} and a decrease of {round(diff * -1)}%.")
        else:
            print(f"{state} had a 7-day average of {round(current)} which was similar the previous week")


main()
