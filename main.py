"#"
#frewrfr3wtg
def s():
    x=input("ввод пароля")
    y=input("повтор пароля")
    if x == y:
        return("пароль принят")
    else:
        return("пароль не принят")
print(s())

def q():
    x=int(input("номер места"))
    if x == 1 or x==7:
        print("место боковое верхнее")
    if x==2 or x==8 :
        print("место боковое нижнее")
    if x == 3 or x == 9:
        print ("место купе слева верхнее")
    if x == 4 or x == 10:
        print ("место купе справа верхнее")

    if x == 5 or x == 11:
        print ("место купе слева низ")
    if x == 6 or x == 12:
        print ("место купе справа низ")
q()

def w():
    x=int(input("номер года"))
    if x % 4 ==0 and x % 100 != 0:
        print ("год", x, " високосный")
    else:
        print("год", x, "не високосный")
w()

def e():
    x=str(input("первый цвет"))
    y=str(input ("второй цвет"))
    if x!="красный" and x!="желтый" and x!="синий":
        print("ошибка")
    if y!="красный" and y!="желтый" and y!="синий":
        print("ошибка")
    if x=="желтый" and y=="красный":
        print("оранжевый")
    if x=="желтый" and y=="синий":
        print("зеленый")
    if x == "красный" and y == "синий":
        print("фиолетовый")
    if x =="красный" and y=="желтый":
        print("оранжевый")
    if x=="синий" and y=="желтый":
        print("зеленый")
    if x=="синий" and y=="красный":
        print("фиолетовый")
e()

def r():
    x=int(input("колличество слов"))
    y=str(input("слово"))
    a=""
    for i in range (x):
        a=a+" " + y
    print(a)
r()

