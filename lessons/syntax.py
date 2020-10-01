x = 7
y = 5
if x > y:
    print(x)

a = 5
if a == 5:
    print('Ура!')

# Числа кроме 0, непустой объект всегда true
if 1:
    print(True)
else:
    print(False)
# 0, пустой объект и None всегда false
if 0:
    print(True)
else:
    print(False)

a = int(input())
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')

