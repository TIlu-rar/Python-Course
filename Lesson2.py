y = 50
while True:
    San1 = int(input("Birinshi san: "))
    Tanba = input("Amaldi engiz: ")
    San2 = int(input("Ekinshi san: "))

    if Tanba == "+":
        x = San1 + San2
        print("Eki san kosindisi: ", San1+San2)
    elif Tanba == "-":
        x = San1 - San2
        print("Eki san azaitindisi: ", San1-San2)
    elif Tanba == "*":
        x = San1 * San2
        print("Eki san kobeitindisi: ", San1 * San2)
    elif Tanba == "/":
        x = San1 / San2
        print("Eki san bolindisi: ", San1 / San2)

    if x >= y:
        print("Ulken")
    elif x <= y:
        print("Kishi")

    if x == y:
        print("taptin")
        break