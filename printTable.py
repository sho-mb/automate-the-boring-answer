tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def getLongest(table):
    listOfMaxLen = []
    max_len = -1
    for row in range(len(table)):
        max_len = 0
        for col in range(len(table[row])):
            item = table[row][col]
            if len(item) > max_len:
                max_len = len(item)
        listOfMaxLen.append(max_len)
    
    return listOfMaxLen

    
def printTable(table):
    newTable = []
    newData = []
    listOfMaxLen = getLongest(table)
    for row in range(len(table[0])):
        for col in range(len(table)):
            item = table[col][row]
            maxLen = listOfMaxLen[col]
            alignedItem = item.rjust(maxLen)
            newData.append(alignedItem)
        newTable.append(newData)
        newData = []
    for data in range(len(newTable)):
        print(' '.join(newTable[data]))

printTable(tableData)
