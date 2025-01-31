def grid(row,col):
    x=('+----'*col+'+')
    y=('\n'+'|    '*(col+1))
    return((x+4*y)+'\n')*row+x
print(grid(2,2))
