#! /usr/bin/python3
# 输出右对齐的二维列表
def printTable(table):
    colWidths=[0]*len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if(len(table[i][j])>colWidths[i]):     
               colWidths[i]=len(table[i][j])
        for j in range(len(table[i])):
            table[i][j]=table[i][j].rjust(colWidths[i])
    for i in range(len(table[0])):
        for j in range(len(table)):
             print(table[j][i]+' ',end='')
        print('\n')
tableData=[['apples','oranges','bananas','peaches','plums'],
           ['Anna','Kabuda','Kinduofen','kaka','dede'],
           ['eggs','sausages','bacon','fish','cabbage']]
printTable(tableData)
