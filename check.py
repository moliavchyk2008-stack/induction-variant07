def f(n):
    return 5**(2*n - 1) + 1 

m = 6 
bad = [n for n in range(1, 101) if f(n) % m != 0]
print("Контрприкладів не знайдено" if not bad else bad)
