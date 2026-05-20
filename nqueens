def nqueen(n):
    board=[["."] * n for i in range (n)]
    solution=[]
    cols=set()
    neg_dia=set()
    pos_dia=set()
    def backta(r):
        if r==n:
            solution.append([" ".join(row) for row in board]) 
            return
        for c in range (n):
            if c in cols or (r+c) in pos_dia or (r-c) in neg_dia:
                continue
            cols.add(c)
            pos_dia.add(r+c)
            neg_dia.add(r-c)
            board[r][c]="Q"
            
            backta(r+1)
            
            cols.remove(c)
            pos_dia.remove(r+c)
            neg_dia.remove(r-c)
            board[r][c]="."
    backta(0)
    return solution
print(nqueen(4))   
