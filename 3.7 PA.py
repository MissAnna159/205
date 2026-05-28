import pandas as pd
import matplotlib.pyplot as plt

def main():
    #1. Print Student ID
    print("carana9896\n")

    #2. Create the ballroom capacity table
    data = {
         "Names": ["Ballroom 1", "Ballroom 2", "Ballroom 3"],
         "Capacity": [25000,11000,5000]
         }
    df = pd.DataFrame(data)
    #define df first before call barchart which require df
    print(df)
    BarChart(df)
    PieChart()
    
def BarChart(df):
    plt.figure()
    plt.bar(df["Names"], df["Capacity"], label="Capacity")
    plt.xlabel("Ballroom")
    plt.ylabel("Capacity")
    plt.title("Ballroom Capacity")
    plt.legend()
    plt.show() 
    plt.close()
    
def PieChart():
    labels = ["Children", "Adults", "Teens"]
    sizes = [18000, 13000, 10000]

    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Attendess")
    plt.show()
    plt.close()
    
main()


