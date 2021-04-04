sayi = int(input("Bir sayı giriniz : "))

for i in range(2 , sayi+1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(f"{i} asal")
   