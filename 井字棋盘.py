#井字棋盘建模
#选用字典作为数据结构对井字棋盘建模
theBoard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'low-l':' ','low-m':' ','low-r':' '}
#解释该数据结构
def printBoard(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['low-l']+'|'+board['low-m']+'|'+board['low-r'])
turn='X'
for i in range(9):
    printBoard(theBoard)
    print('This step is for '+turn+'. where to move space?')
    where=input()
    theBoard[where]=turn
    if(turn=='X'):
        turn='O'
    else:
        turn='X'
printBoard(theBoard)

