def valid (grid,row,col,num): 
    for x in range (4): 
        if grid[row][x] == num: 
            return False 
    for x in range (4):
        if grid[x][col] == num: 
            return False
        
    strtrow, strtcol = (row//2)*2, (col//2)*2
    for i in range (2): 
        for j in range (2): 
            if grid[i+strtrow][j+strtcol] == num:
                return False 
    return True

def check (grid): 
    for row in range (4): 
        for col in range (4): 
            if grid [row][col] == 0: 
                for num in range (1,5): 
                    if valid (grid,row,col,num): 
                        grid[row][col] = num 
                        if check (grid): 
                            return True 
                        
                        grid[row][col]= 0
                return False  
    return True
    

def main ():
    grid =[]
    for i in range(4): 
        row = list(map(int,input().split()))
        grid.append(row)

    if check(grid): 
        for row in grid: 
            print(*(row))
main ()
