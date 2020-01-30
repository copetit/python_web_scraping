import csv

def save_to_file():
    file = open("jobs.csv", mode = "w")
    print(file)
    writer = csv.writer(file)
    writer.writerow(["title","company","locatioin","link"])
    return