#二维矩阵的顺时针90度转置
def rotate(grid):
    if(not isinstance(grid,list)):
        return
    length=len(grid[0])
    for i in range(len(grid)):
        if(not isinstance(grid[i],list)):
            return
        if(length!=len(grid[i])):
            return
    g2=[]
    t=[]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
           t.append(grid[len(grid)-1-i][j])
        g2.append(t)
        print(t)
        t=[]
    return g2
grid=[['0','1','0'],
      ['0','1','0'],
      ['0','1','1']]
grid2=rotate(grid)
s=''
for j in range(len(grid2)):
  for i in range(len(grid2[0])):
     s+=grid2[j][i]+' '
  print(s)
  s=''

