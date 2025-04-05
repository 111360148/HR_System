def f_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f_recursive(n - 1) + f_recursive(n - 2)

def f_loop(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        i = 2
        while i <= n:
            temp = a + b
            a = b
            b = temp
            i += 1
        return b

while True:
    try:
        method = int(input("請選擇計算方法：\n1. 遞迴 2. 非遞迴 輸入 1 或 2: "))
        if method == 1 or method == 2:
            break
        else:
            print("請重新輸入 1 或 2。")
    except ValueError:
        print("輸入錯誤！請重新輸入 1 或 2。")

while True:
    try:
        n = int(input("請輸入一個非負整數："))
        if n >= 0:
            break
        else:
            print("請輸入非負整數！")
    except ValueError:
        print("輸入錯誤！請輸入整數，不要輸入浮點數或其他字符。")

if method == 1:
    print(f"第 {n} 個 Fibonacci 數（遞迴）是：{f_recursive(n)}")
else:
    print(f"第 {n} 個 Fibonacci 數（非遞迴）是：{f_loop(n)}")
