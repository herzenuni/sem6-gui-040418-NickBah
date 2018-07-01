def solve(a):
    n = len(a)

    """
    print("Для матрицы:")
    for t in a:
        print(t)
    """

    # Прямой ход
    x = [None for i in range(n)]
    for i in range(0,n):
        for k in range(i+1,n):
            temp = a[k][i]
            for j in range(i,n+1):
                a[k][j] = a[k][j] - a[i][j] * (temp / a[i][i])

    # Обратный ход
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1];

    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += a[i][j] * x[j]
        x[i] = (a[i][n] - sum) / a[i][i]

    #print(x)

    return x

