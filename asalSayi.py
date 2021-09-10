i, sayac, a = 2, 0, 1
adet = []
while True:
    sayi = input("Bir sayı giriniz, girdiğiniz sayıya kadar olan asallar bulunacaktır: ")
    depo = sayi
    if sayi.isdigit() and int(sayi) == 2:
        sayi = int(sayi)
        print("Girdiğiniz sayı en küçük asal sayıdır: 2")
        quit()
    if sayi.isdigit() and int(sayi) > 2:
        sayi = int(sayi)
        for x in range(sayi):
            while sayi >= i:
                kalan = sayi % i
                if kalan == 0:
                    sayac = sayac + 1
                else:
                    pass
                i = i + 1
            if sayac == 1:
                adet.append(sayi)

            i = 2
            sayi = sayi - 1
            sayac = 0
        adet.reverse()
        print("{} sayısına kadar olan asal sayılar: {} -- Toplam {} adet asal sayı bulunmaktadır.".format(depo,adet,len(adet)))
        quit()
    else:
        print("Tekrar deneyin")
