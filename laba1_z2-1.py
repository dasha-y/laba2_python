def SumDigits(a):
    c = 0
    s = 0
    
    while a > 0:
        digit = a % 10
        s += digit
        c += 1
        a //= 10
        
    return c, s
nums = [1, 123, 1234, 12345, 123456] 
for num in nums:
    c, s = SumDigits(num)
    print(f"Число: {num}, Количество цифр: {c}, Сумма цифр: {s}")