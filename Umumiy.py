# Kvadrat va kub topuvchi dastur
# a = int(input("Sonni kiriting: "))
# b = a**2
# c = a**3
# print("Kvadrati: ", b)
# print("Kubi: ", c)


# Tug'ulgan yilni topuvchi dastur
# a = int(input("Nechi yoshdasiz: "))
# b = 2025 - a
# print("Siz", b, "yilda tug'ilgansiz")  

# Nomalumlar
# x, y, z = 1, 2, 4
# a = x + y + z
# b = x * y * z
# print(a, "har doim ",  b, "Dan kichik" )


# List va royxatlar
# sonlar = list(range(0,11))

# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng ")

# For uchun


# odamlar = ["Sardor","Sayyod","Kamron","Farhod","Kamol"]
# for odam in odamlar:
#     print(f"Salom {odam} qandaysan")

# Toq sonlar ro'yxati 

# n = list(range(11,100,2))
# for n1 in n :
#     print(f"{n1} ning kvadrati {n1**2} ga teng")
#     print(f"{n1} ning kubi {n1**3} ga teng")


# if aperatori

# mashinalar = ["nexia", "bmw", "toyota", "spark"]
# for car in mashinalar :
#     if car == "bmw" :
#         print(car.upper())
#     else :
#         print(car.title())

# a = str(input("Ismingizni kiriting: "))
# if a.lower() == "sayyod" :
#     input("Assalomu aleykum Sayyod yaxshimisiz ? ")
# else :
#     print(f"Uzr {a.title()}, siz ro'yxatdan o'tmagansiz !!! ")


# ro'yxatdan o'tish uchun
# print("Assalomu aleykum" )
# age = int(input("Yoshingizni kiriting: "))
# if age <= 18 :
#     print("Siz yosh chegarasiga to'g'ri kelmadingiz")
# else :
#     want = input("Matematika faniga qiziqasizmi ? ")
#     if want.lower() == "xa" :
#         print("Unda darslarni boshlaymiz, let's go ...")
#     else : 
#         print("Uzr biz sizga yordam bera olmaymiz ....") 


# Yosh topadi va hisoblab aytadi
# print("Assalomu ayekum")
# age = int(input("Yilingizni kiriting :  "))
# if 2026 - age > 18 :
#     print(f"Siz {2026 - age} yoshda ekansiz !")
#     print("Xush kelibsiz ")
# else :
    
#     print("Yosh cheklovingiz to'g'ri kelmadi !!!")

# cars = ["malibu", "Toyota", "gm", "Nexia"]
# print("Assalomu aleyum, ro'yxatda ")
# for car in cars :

#     if car == "gm" :
#         print(car.upper())
#     else :
#         print(car.title())
# print("moshinalari bor")

#Amaliyotlarim


# name = input("Assalomu aleykum \nIsmizgizni kiriting:  ")
# if name.lower() == "sardor" :
#     print("Qandaysiz ? Bugungi kuningiz qanday o'tyapti ? ")
# else :
#     print("Kechirasiz, siz bilan bog'lanolmayman")

#Son bilan ishlash

# son1 = int(input("1-soni kiriting :  "))
# son2 = int(input("2-sonni kiriting :  "))

# if son1 == son2 :
#     print("Siz kirgizgan sonlar teng ")
# elif son1 > son2 :
#     print(f"{son1} > {son2}")
# else :
#     print(f"{son1} < {son2}")
    

#Ildiz topadi 
# import math
# number1 = int(input("Enter your first number : " ))
# number2 = int(input("Enter your second number : "))

# if number1 < 0 and number2 < 0 :
#     print("You can't take square root of the numbers !!!")
# elif number1 > 0 and number2 < 0 :
#     print(f"Only first number is extracted square root \nIt is {math.sqrt(number1)} ")
# elif number1 < 0 and number2 > 0 :
#     print(f"Only second number is extracted square root \nIt is {math.sqrt(number2)} ")
# else :
#     print(f"First root {math.sqrt(number1)}\nSecond root {math.sqrt(number2)}")

#Juft son topadi 


# juft = int(input("Juft son kiriting : "))
# if juft % 2 == 0 :
#     print("Ajoyib, Siz uddaladingiz ")
# else :
#     print("Afsus, Bu juft son emas !!!") 


#Sonlar bo'linishi


# number = int(input("Enter the number :  "))
# c = False 
# if number % 2 == 0 :
#     print("Bu son 2 ga bo'linadi ")
#     c = True
# if number % 3==0 :
#     print("Bu son 3 ga bo'linadi ")
#     c = True
# if number % 4==0 : 
#     print("Bu son 4 ga bo'linadi ")
#     c = True
# if number % 5 == 0 :
#     print("Bu son 5 ga bo'linadi ")
#     c = True
# if number % 6 == 0 : 
#     print("Bu son 6 ga bo'linadi ")
#     c = True
# if number % 7 == 0 : 
#     print("Bu son 7 ga bo'linadi ")
#     c = True
# if number % 8 == 0 : 
#     print("Bu son 8 ga bo'linadi ")
#     c = True
# if number % 9 == 0 : 
#     print("Bu son 9 ga bo'linadi ")
#     c = True
# if number % 10 == 0 : 
#     print("Bu son 10 ga bo'linadi ")
#     c = True
# if c == False : 
#     print("Bu son 1 dan 10 gacha bo'lgan hech qaysi songa bo'lnmaydi ")


#Menyu dasturi

# menu = ["osh" , "manti" , "shashlik" , "lavash" , "sho'rva"]

# take = input("Buyurtma bering : ")
# if take.lower() in menu :
#     print("Buyurtma qabul qilindi ")
# else :
#     print(f"Afsus, bizda bu ovqat yo'q \nXoxlasangiz : {menu} shular bor ")

#Ikki bosqichli menu

# meal = ["osh" , "lavash" , "sho'rva" , "lag'mon" , "manti"]
# desert = ["tort" , "cake" , "shkalat" , "mevali cake"]


# ovqat = input("Ovqat buyurtma qiling : ")
# tort = input("Dessert buyurtma qiling : ")


# if ovqat and tort in meal :
#     print("Buyurtmalar qabul qilindi ") 
# elif ovqat in meal and tort not in meal :
#     print(f"Ovqat qabul qilindi \nLekin afsus, bu dessert bizda yo'q \nXoxlasangiz {desert} bular bor bizda. ")
# elif tort in meal and ovqat not in meal : 
#     print(f"Dessert qabul qilindi \nLekin afsus, bu ovqat bizda yo'q \nXoxlasangiz {meal} bular bor bizda. ")
# else : 
#     print("Siz buyutma qilgan narsalar biza yo'q")  
    
#Qilgan progranmmalaim ichida eng qiyini 

# number = int(input("Enter the number :  "))
# c = False 
# if number % 2 == 0 :
#     print("Bu son 2 ga bo'linadi ")
#     c = True
# if number % 3==0 :
#     print("Bu son 3 ga bo'linadi ")
#     c = True
# if number % 4==0 : 
#     print("Bu son 4 ga bo'linadi ")
#     c = True
# if number % 5 == 0 :
#     print("Bu son 5 ga bo'linadi ")
#     c = True
# if number % 6 == 0 : 
#     print("Bu son 6 ga bo'linadi ")
#     c = True
# if number % 7 == 0 : 
#     print("Bu son 7 ga bo'linadi ")
#     c = True
# if number % 8 == 0 : 
#     print("Bu son 8 ga bo'linadi ")
#     c = True
# if number % 9 == 0 : 
#     print("Bu son 9 ga bo'linadi ")
#     c = True
# if number % 10 == 0 : 
#     print("Bu son 10 ga bo'linadi ")
#     c = True
# if c == False : 
#     print("Bu son 1 dan 10 gacha bo'lgan hech qaysi songa bo'lnmaydi ")


