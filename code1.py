while True:
    try:
        num1 = int(input("請輸入整數："))
        
        if num1 < 0: 
            num2 = -num1
        else:
            num2 = num1

        result = 0
        while num2 != 0:
            result = result * 10 + num2 % 10
            num2 //= 10

        if num1 < 0:
            result = -result

        print(f"反轉後的數字：{result}")
        break 
        
    except ValueError:
        print("輸入錯誤！請輸入整數，不要輸入浮點數或其他字符。")
