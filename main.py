from os import error
import pandas

def loadFile(filename):
    try:
        return pandas.read_csv(filename)
    except Exception as err:
        print(err)
        return None


def filterByPopularity(filename, percentage, lessThan = False):
    data = loadFile(filename)
    try:
        if lessThan:
            data.drop(data[data.popularity > percentage].index, inplace=True)
        else:
            data.drop(data[data.popularity < percentage].index, inplace=True)
    except Exception as err:
        print(err)

    return data


def saveToNewFile(data, filename = 'out.csv'):
    try:
        data.to_csv(filename)
    except Exception as err:
        print(err)


filtered = filterByPopularity('data_by_artist.csv', 90)
saveToNewFile(filtered)