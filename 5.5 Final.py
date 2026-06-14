# IMPORTS
import csv
from datetime import datetime
from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference
import matplotlib.pyplot as plt


# FUNCTION 1
def askUser():
    total = 0

    # Loop runs 5 times to collect 5 numbers from the user and accumulate their total
    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                total += num
                break
            except:
                print("Invalid input. Please enter a number.")

    print("Total of numbers:", total)


# FUNCTION 2
def askIncome():
    filename = "final.csv"

    # Loop runs 5 times to collect name and income, then append each entry to the CSV file
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)

        for i in range(5):
            name = input(f"Enter name {i+1}: ")
            income = input(f"Enter income for {name}: ")
            writer.writerow([name, income])


# FUNCTION 3
def excelPie():
    wb = Workbook()
    ws = wb.active
    ws.title = "Income Data"

    names = []
    incomes = []

    # Read CSV data
    with open("final.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row[0])
            incomes.append(int(row[1]))   # Cast to int (IMPORTANT)

    # Add headers
    ws.append(["Name", "Income"])

    # Write data to worksheet
    for i in range(len(names)):
        ws.append([names[i], incomes[i]])

    # Create pie chart object
    chart = PieChart()
    # Purpose: Create a pie chart visualization object

    data = Reference(ws, min_col=2, min_row=1, max_row=len(names)+1)
    # Purpose: Select income values for chart data

    labels = Reference(ws, min_col=1, min_row=2, max_row=len(names)+1)
    # Purpose: Select names for chart labels

    chart.add_data(data, titles_from_data=True)
    # Purpose: Add income data into the chart

    chart.set_categories(labels)
    # Purpose: Attach labels (names) to the data

    student_id = "carana9896"
    date = datetime.now().strftime("%B %d, %Y")

    chart.title = f"{student_id} {date}"
    # Purpose: Set the title of the chart

    ws.add_chart(chart, "E2")
    # Purpose: Place chart on the worksheet

    wb.save("final.xlsx")
    # Purpose: Save the Excel file with chart


# FUNCTION 4
def verticalBar():
    names = []
    incomes = []

    # Read CSV data
    with open("final.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row[0])
            incomes.append(int(row[1]))

    # Create bar chart
    plt.bar(names, incomes)

    student_id = "carana9896"
    date = datetime.now().strftime("%B %d, %Y")

    plt.title(f"{student_id} {date}")
    plt.xlabel("Names")
    plt.ylabel("Income")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


def main():
    #askUser()
    #askIncome()
    excelPie()
    verticalBar()
if __name__ == "__main__":
    main()

