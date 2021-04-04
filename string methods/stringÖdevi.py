website="https://www.google.com.tr/"
course="Pyhton Kursu: Baştan Sona Pyhton Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

print("{}".format(len(course)))

# 2-'website' içerisinden www karakterlerini alın.
print("{a}".format(a=website[8:11]))
# 3-'website' içerisinden com karakterlerini alın.
length= len(website)
result= website[length-7:length-4]
print(" {} ".format(result))

# 4-'course' içerisinden ilk 15 ve son 15  karakterlerini alın.
lengthCourse=len(course)
first15=course[0:15]
print(first15)
last15=course[lengthCourse-15:lengthCourse]
print(last15)


# 5-'course' ifadesindeki karakterleri tersten yazdırın. 
#print("{b:[12]}".format(b=course))
tersten=course[::-1]
print(tersten)
name, surname, age, job= "Bora","Yılmaz",32,"Mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim Mühendis.'
print(f"Benim adım {name} {surname}, Yaşım {age}, ve mesleğim {job}")

# 7-Hello world ifadesindeki 'w' harfini 'W' ile değiştirin.
a="Hello world"
#a=a[0:6] + 'W' + a[-4:]
a=a.replace('w','W')
print(a)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın
print('abc'*3)