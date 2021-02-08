import pandas

def loadFile(filename):
    try:
        return pandas.read_csv(filename)
    except Exception as err:
        print(err)
        return None


def filterByPopularity(data, percentage, lessThan = False):
    filterData(data, 'popularity', lessThan, percentage)


def filterData(data, filter, lessThan, percentage):
    try:
        if lessThan:
            data.drop(data[data[filter] > percentage].index, inplace=True)
        else:
            data.drop(data[data[filter] < percentage].index, inplace=True)
    except Exception as err:
        print(err)


def saveToNewFile(data, filename = 'out.csv'):
    try:
        data.to_csv(filename)
    except Exception as err:
        print(err)


data = loadFile('data_by_artist.csv')
filterByPopularity(data, 90)
saveToNewFile(data)
print('\nFiltering finished!\n')