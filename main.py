import pandas

def open_csv(filename): 
    try:
        return pandas.read_csv(filename)             
    except Exception as err:
        print(err)
        return None


def filter_by_pop(file):
    try:
        file.drop(file[file['popularity']<65].index, inplace=True) #usuwa wszystko ponizej 65
    except Exception as err:
        print(err)


def save_csv(file):
    file.to_csv('new_csv.csv')
  

filecsv = "data_by_artist.csv"
file = open_csv(filecsv) 
filter_by_pop(file)
save_csv(file)