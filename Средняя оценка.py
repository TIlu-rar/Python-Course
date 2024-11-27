Bagalar = []
y = 0
while True:
    x = int(input("Auditoria: "))
    if x == 1000:
        y = y / len(str(y))
        break
    Bagalar.append(x)
    y = y + x
    print(Bagalar)
print(Bagalar)
y = y * 0.6
print(y)

Modul1 = int(input("Modul1: "))
Modul2 = int(input("Modul2: "))
Modul = Modul2 * 0.2 + Modul1 * 0.2
print(Modul)
Obshi = Modul + y
Exam = int(input("Exam: "))
Sesia = Exam + Obshi
OS = Sesia / 2
print(OS)
