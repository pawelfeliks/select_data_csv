import csv


def open_file(path):

    try:
        f = open(path, "r", encoding="utf-8")
        for line in f:
            print(line, end="")
            
    except:
        print("Error or no such file")



def open_csv(plik):
    
    try:
        
        with open(plik, 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                
    except:
        print("Error or no such file")

 

filecsv = "E:\Studia\Programowanie\Python\plik_csv.csv"
open_csv(filecsv) 
