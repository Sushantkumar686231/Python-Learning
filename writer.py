import csv


with open("students.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Age","Grade"])
    writer.writerow(["ALice",14,"8th"])
    writer.writerow(["Sushant",15,"9th"])
    writer.writerow(["Charlie",13,"7th"])
