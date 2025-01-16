bagalar = []

def baga_engizu (baga: int):
    if baga > 100:
        print("100 den ulken")
    else:
        bagalar.append(baga)
    print(bagalar)
    return bagalar
def arm (bagalar):
    c = sum(bagalar)/len(bagalar)
    return(c)
def qoritindy(x, y, z, s):
    mani = x * 0.4 + (((y+z)/2)*0.2) + s * 0.4
    return mani

def Display(tauarlar):
    for id, data in tauarlar.items():
        print(f"{id} | {data["name"]} | бағасы {data["baga"]} тенге | {data["zapas"]} {data["olshemi"]} бар")


def cart(tauarlar):
    total_sum = 0
    korzina = []
    korzina_sany = []
    korzina_baga = []
    stock_dec_dynamics = {1:[],2:[],3:[]}
    while True:
        id = int(input("Тауарлардың айдиын енгізіңіз (үтір арқылы): "))
        if id == 0:
            for x in range(len(korzina)):
                print(f"{tauarlar[korzina[x]]["name"]} {tauarlar[korzina[x]]["baga"]}тг | {korzina_sany[x]} {tauarlar[korzina[x]]["olshemi"]} | {korzina_baga[x]} ")
            print(f"Итого: {total_sum}")
            break
        else:
            korzina.append(id)
            quantity = int(input(f"Қанша {tauarlar[id]["olshemi"]} алғыңыз келеді?: "))
            tauarlar[id]["zapas"] -= quantity
            korzina_sany.append(quantity)
            baga = tauarlar[id]["baga"]
            summa = baga * quantity
            if quantity >= 10 and tauarlar[1]:
                summa -= 1.1111111111
            if quantity >= 5 and tauarlar[3]:
                summa /= 1.0752688172
            if quantity >= 5 and tauarlar[2]:
                summa /= 1.0309278351
            korzina_baga.append(summa)
            total_sum = total_sum + summa
            print(korzina)
            print(korzina_sany)
            Display(tauarlar)