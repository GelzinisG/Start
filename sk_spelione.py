
import random
sarasas = []

def info():
    print("\n    Made in\n"
          "       *** CODE ACADEMY ***\n"
          "                By Giedrius Gelžinis")

def rezultatas():
    if len(sarasas) <= 0:
        pass
    else:
        print(f"\nGeriausias rezultatas priklauso {min(sarasas)} bandymams")


def zaidimas():
    skaicius = int(random.randint(1, 10))
    print("\nSveiki atvykę į spėlionių žaidimą!")
    vartotojas = input("Koks tavo vardas?"
                       "\n")
    ivedimas = input(f'\n{vartotojas}, ar norėtum žaisti "atspėk skaičių" žaidimą?'
                     "\nJei nori žaisti, įvesk - t"
                     "\nJei nenori žaisti, įvesk - n"
                     "\n")

    bandymai = 0
    rezultatas()
    while True:
        while ivedimas == "t":
            try:
                spejimas = int(input("Pasirink skaičių nuo 1 iki 10 "))
                if int(spejimas) < 1 or int(spejimas) > 10:
                    raise ValueError("Prašome atspėti skaičių")
                if int(spejimas) == skaicius:
                    print("Puiku! Atspėjai!")
                    bandymai += 1
                    sarasas.append(bandymai)
                    print(f"\nTavo bandymų rezultatas: {bandymai}.")
                    dar_karta = input("Ar norėtum žaisti dar kartą? (t/n) ")
                    bandymai = 0
                    rezultatas()
                    skaicius = int(random.randint(1, 10))
                    if dar_karta.lower() == "t":
                        print("\nŠaunus pasirinkimas.\n"
                              "PAVAROM!\n")
                        continue
                    if dar_karta.lower() == "n":
                        print("Šauniai sudalyvavai!\n")
                        return rezultatas(), info()
                    elif ValueError:
                        print("Neteisingai įvedei. Bandyk iš naujo...\n")
                        zaidimas()
                    else:
                        return info()

                if int(spejimas) > skaicius:
                    print("Neatspėjai, mažesnis.\n")
                    bandymai += 1
                if int(spejimas) < skaicius:
                    print("Neatspėjai, didesnis.\n")
                    bandymai += 1
            except ValueError:
                print("O ne!, Neteisingai įvedei. Bandyk iš naujo...")
        if ivedimas == "n":
            print("*** Lauksime sugrįžtant ***\n"
                  "   *** Iki pasimatymo ***\n"
                  "       ***   ;)   ***")
            return info()
        elif ValueError:
            print("\nKlaidinga įvestis\n"
                  "       Bandyk dar kartą!\n")
            return zaidimas()


if __name__ == '__main__':
    zaidimas()