#Calculator
def startstop():
    ss=int(input("Devam etmek için 1, sonlandırmak için 0 tuşlayınız: "))
    if ss == 1:
        interface()
    else:
        print("-" * 25)
        print("Sonlandırılıyor...")
        exit(0)
        quit(0)

def run():
    print("-" * 25)
    print("Hesap Makinesi v1.0")
    interface()

def interface():
    print("-" * 25)
    showactions()
    datarequests()

transactions = ["Toplama", "Çıkarma", "Çarpma", "Bölme"]

def showactions():
    print("işlem Listesi")
    for showlist in transactions:
        print(transactions.index(showlist),showlist,sep=".")

def datarequests():
    print("-"*25)
    chooseaction= int(input("İşlem Numarasını Giriniz: "))
    if chooseaction < 0 or chooseaction >= len(transactions):
        print("Hatalı işlem seçimi!")
        datarequests()
    numberone=float(input("Sayı Giriniz: "))
    numbertwo=float(input("Sayı Giriniz: "))
    result=float(takeaction(chooseaction, numberone, numbertwo))
    print("İşlem Sonucunuz: ", result, sep="")
    print("-" * 25)
    memoryinterface(result)

def takeaction(action, numberone, numbertwo):
    result = float()
    if transactions[action] == "Toplama":
        result = numberone + numbertwo
    elif transactions[action] == "Çıkarma":
        result = numberone - numbertwo
    elif transactions[action] == "Çarpma":
        result = numberone * numbertwo
    elif transactions[action] == "Bölme":
        if numbertwo == 0:
            print("Sıfıra bölünemez!")
            datarequests()
        else:
            result = numberone / numbertwo
    else:
        print("Sistem Hatası!")
        datarequests()
    return result
#Calculator

#Memory
memory=float(0.0)

def memoryinterface(result):
    print("Bellek İşlemleri")
    print("-" * 25)
    memoryshowactions()
    memorydatarequests(result)

memoryactions = ["Ekle", "Çıkar", "Temizle", "İşlem Yapmadan Devam Et"]

def memoryshowactions():
    print("İşlem Listesi")
    for showmemorylist in memoryactions:
        print(memoryactions.index(showmemorylist), showmemorylist, sep=".")

def memorydatarequests(result):
    print("-" * 25)
    chooseaction= int(input("Bellek İşlem Numarası Giriniz: "))
    if chooseaction < 0 or chooseaction >= len(memoryactions):
        print("Hatalı bellek işlem seçimi!")
        memorydatarequests(result)
    memoryresult = takememoryaction(chooseaction, result)
    print("Bellekteki Sayı: ", memoryresult, sep="")
    print("-" * 25)
    startstop()

def takememoryaction(action, result):
    global memory
    if memoryactions[action] == "Ekle":
        memory = memory + result
    elif memoryactions[action] == "Çıkar":
        memory = memory - result
    elif memoryactions[action] == "Temizle":
        memory = 0.0
        print("Bellek Temizlendi!")
        memorydatarequests(result)
    elif memoryactions[action] == "İşlem Yapmadan Devam Et":
        return memory
    else:
        print("Sistem Hatası!")
        memorydatarequests(result)
    return memory
#Memory

run()

#Creation Date: April 2021