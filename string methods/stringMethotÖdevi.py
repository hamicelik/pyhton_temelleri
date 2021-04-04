a=' hello world '
b=' hello world '
c=' hello world '
d='https.www.hamicelik.com.tr'
website ='www.sadikturan.com'
course="Pyhton Kursu: Baştan Sona Pyhton Programlama Rehberiniz (40 saat)"
e='content'
#' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

# a=a.strip()    # baştaki ve sondaki boşluğu sildi 
# print(a)
# b=b.lstrip()   # baştaki  boşluğu sildi 
# print(b)
# a=a.strip()    # sondaki boşluğu sildi 
# c=c.rstrip()          
# print(c)
# d=d.strip('htps.') # verdiğimiz değeri sildi
# print(d)

#'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# website=website.strip('w.moc').lstrip('n')  #baştan yada sondan kontrol ederek silme işlemi yapar. verdiğimiz değerlere uymayan olursa silmeyi bırakır
# print(website)                             #ilk veriğim değerleri sildi ve durdu ikinci verdiğim 'n' değerine baktı ve sonda gördü ve sildi

# #'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
# print(course)
# course=course.lower()
# print(course)

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
#website=website.count('a')
# website=website.count('a',0,15)   #0. index ten 15 e kadar gitti ve aradı
# print(website)

#5- 'website' "www" ile başlayıp com ile bitiyor mu?
#website=website.startswith('www')
# website=website.endswith('com')
# print(website)

#6-'website' içinde 'com' ifadesi var mı?
# website=website.find('com')
# print(website)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
# course=course.isalpha()
# print(course)
# course=course.isdigit()
# print(course)

# # 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# e=e.center(50,'*')
 

# 9-'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

course=course.replace(' ','-')
print(course)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

# course=course.split(' ')
# print(course)
