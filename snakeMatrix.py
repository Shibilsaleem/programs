def snakeMatrix(n):
    matrix=[[0]*n for _ in range(n)]
    number=1
    for i in range(n):
        if i%2==0:
            for j in range(n):
                matrix[i][j]=number
                number+=1    
        else:
            for j in range(n-1,-1,-1):
                matrix[i][j]=number
                number+=1
    for row in matrix:
        print(" ".join(map(str,row)))
n=int(input('Enter n : '))
print(snakeMatrix(n))