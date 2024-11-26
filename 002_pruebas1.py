# Enteros:

#guardamos los numeros en una string 
a = 0b100 #binario
b = 0x17 #hexadecimal
c = 0o720 #octal
print(a, type(a)) #4 <class 'int'>
print(b, type(b)) #23 <class 'int'>
print(c, type(c)) #464 <class 'int'>

# vamos a usar un float, en este caso aunque sea un entero,
# como hemos usado un decimal, tenemos un resultado float
d = 354 * 5.5
print(d, type(d)) # 1947.0 <class 'float'>

#igualamos d al casteo a int del mismo
d = int(d)
print(d, type(d)) # 1947.0 <class 'int'>


# Booleanos

x = True
y = False

# Esto lo evalua el programa
print(1 > 0)  #True
print(1 <= 0) #False
print(9 == 9) #True

# 
v = 1 > 0
print (v)
m = 1==0
print(m)


if b > a:
    print("b es mayor que a ")

k = 2e-3
print(k)

