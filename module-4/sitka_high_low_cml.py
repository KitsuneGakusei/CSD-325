import csv
from datetime import datetime
from matplotlib import pyplot as plt

def read_weather_data(filename):
    """Read dates, highs, and lows from a CSV file."""
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except (IndexError, ValueError):
                # Skip rows with missing data
                print(f"Skipping row: {row}")
                continue
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_temperatures(dates, temperatures, title, color):
    """Plot temperatures on a graph."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    while True:
        print("\nMenu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("Thanks for using the weather charting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()