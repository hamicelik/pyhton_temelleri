number=[0,25,119,632,47,852,654,5]
letter=['h','a','b','y','n','e','o','z','p']
# number.append(14)  # append dizi sonuna eleman eklemek için kullanılır fakat ekenecek olan değişken dizi halinde verilirse bu aynen dizi olarak eklenir
# number.append([14,12])
# print(number)
# number.extend([23,45])  # dizi sonuna eleman eklemek için kullanılır fakat ekenecek olan değişken dizi halinde verilirse bu dizi olarak değil teker teker eleman olrak eklenir
# print(number)

# number=number.index(632) # index aradığımız elemanın index numarasını bize döner. Fakat oluşturduğumuz methoda bir değişken için koyarak kullanmak gerek. Örnekte tekrar number içine attık
# print(number)

names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
# names.append("Cenk")
# print(names)

# 2-  "Sena" değerini listenin başına ekleyiniz.
# names.insert(1, "Sena")
# print(names)

# 3-  "Deniz" ismini listeden siliniz.
# names.remove('Deniz')
#  print(names)

# 4-  "Deniz" isminin indeksi nedir ?
# a=names.index('Deniz')
# print(a)

# 5-  "Ali" listenin bir elemanı mıdır ?
# ali='Ali' in names
# print(ali)
# for i in names :
#    if (i == 'Hakan') : 
#      print('aranan mevcut')

# 6-  Liste elemanlarını ters çevirin.
# names.reverse()
# print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# names.sort()
# print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
# years.sort()
# print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# str = "Chevrolet,Dacia"
# result = str.split(',')
# print(result)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?

# years_max=max(years)
# years_min=min(years)
# print(years_max)
# print(years_min)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

# years_count=years.count(1998)
# print(years_count)

# 12- years dizisinin tüm elemanlarını siliniz.

# years.clear()
# print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

# marka=[input('beğendiğiniz markayı giriniz:  '),input('beğendiğiniz markayı giriniz:  '),input('beğendiğiniz markayı giriniz:  ')]

# print(marka)

