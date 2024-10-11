import random
import os
import time
os.system('cls')

jatek = input("Szeretnél játszani? (y/n)\n")

if jatek == "y":
    while jatek == "y":
        os.system('cls')

        egy = " "
        ketto = " "
        harom = " "
        negy = " "
        ot = " "
        hat = " "
        het = " "
        nyolc = " "
        kilenc = " "


        turn = int(input(""))
        ember = []
        szamitogép = []


        print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        sarok = [1, 3, 7, 9]
        oldal = [2, 4, 6, 8]
        kozep = [5]

        gep = ""

        foglalt = []
        #00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        while turn == 0:
            gep = random.choice(sarok)
            foglalt.append(gep)
            szamitogép.append(gep)
            if gep == 1:
                egy = "x"
            elif gep == 2:
                ketto = "x"
            elif gep == 3:
                harom = "x"
            elif gep == 4:
                negy = "x"
            elif gep == 5:
                ot = "x"
            elif gep == 6:
                hat = "x"
            elif gep == 7:
                het = "x"
            elif gep == 8:
                nyolc = "x"
            else:
                kilenc = "x"
            turn += 1
            time.sleep(2)
            os.system('cls')
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        #11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
        while turn == 1:
            rakas = int(input("Hova szeretnél tenni?(1-9)\n"))
            foglalt.append(rakas)
            ember.append(rakas)
            if rakas == 1:
                egy = "o"
            elif rakas == 2:
                ketto = "o"
            elif rakas == 3:
                harom = "o"
            elif rakas == 4:
                negy = "o"
            elif rakas == 5:
                ot = "o"
            elif rakas == 6:
                hat = "o"
            elif rakas == 7:
                het = "o"
            elif rakas == 8:
                nyolc = "o"
            elif rakas == 9:
                kilenc = "o"
            else:
                print("Elbasztad")
            turn += 1
            os.system('cls')
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        time.sleep(2)
        os.system('cls')

        #222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
        while turn == 2:
            if rakas in sarok:
                gep = 5
            elif rakas in oldal:
                gep = 5
            else:
                if gep == 1:
                    gep = 9
                elif gep == 3:
                    gep = 7
                elif gep == 7:
                    gep = 3
                else:
                    gep = 1
            foglalt.append(gep)
            szamitogép.append(gep)
            if gep == 1:
                egy = "x"
            elif gep == 2:
                ketto = "x"
            elif gep == 3:
                harom = "x"
            elif gep == 4:
                negy = "x"
            elif gep == 5:
                ot = "x"
            elif gep == 6:
                hat = "x"
            elif gep == 7:
                het = "x"
            elif gep == 8:
                nyolc = "x"
            else:
                kilenc = "x"
            turn += 1
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        while turn == 3:
            rakas = int(input("Hova szeretnél tenni?(1-9)\n"))
            foglalt.append(rakas)
            ember.append(rakas)
            if rakas == 1:
                egy = "o"
            elif rakas == 2:
                ketto = "o"
            elif rakas == 3:
                harom = "o"
            elif rakas == 4:
                negy = "o"
            elif rakas == 5:
                ot = "o"
            elif rakas == 6:
                hat = "o"
            elif rakas == 7:
                het = "o"
            elif rakas == 8:
                nyolc = "o"
            elif rakas == 9:
                kilenc = "o"
            else:
                print("Elbasztad")
            turn += 1
            os.system('cls')
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        time.sleep(2)
        os.system('cls')
        #44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
        while turn == 4:
            if rakas == 1:
                gep = 9
            elif rakas == 3:
                gep = 7
            elif rakas == 7:
                gep = 3
            elif 9 in ember and 1 in ember:
                gep = random.choice(oldal)
            elif rakas == 2:
                gep = 8
            elif rakas == 4:
                gep = 6
            elif rakas == 6:
                gep = 4
            elif rakas == 8:
                gep = 2
            elif 9 in ember and 1 not in ember:
                gep = 1
            foglalt.append(gep)
            szamitogép.append(gep)
            if gep == 1:
                egy = "x"
            elif gep == 2:
                ketto = "x"
            elif gep == 3:
                harom = "x"
            elif gep == 4:
                negy = "x"
            elif gep == 5:
                ot = "x"
            elif gep == 6:
                hat = "x"
            elif gep == 7:
                het = "x"
            elif gep == 8:
                nyolc = "x"
            else:
                kilenc = "x"
            turn += 1
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        #5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
        while turn == 5:
            rakas = int(input("Hova szeretnél tenni?(1-9)\n"))
            foglalt.append(rakas)
            ember.append(rakas)
            if rakas == 1:
                egy = "o"
            elif rakas == 2:
                ketto = "o"
            elif rakas == 3:
                harom = "o"
            elif rakas == 4:
                negy = "o"
            elif rakas == 5:
                ot = "o"
            elif rakas == 6:
                hat = "o"
            elif rakas == 7:
                het = "o"
            elif rakas == 8:
                nyolc = "o"
            elif rakas == 9:
                kilenc = "o"
            else:
                print("Elbasztad")
            turn += 1
            os.system('cls')
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        time.sleep(2)
        os.system('cls')
        #66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        while turn == 6:
            if rakas == 1:
                gep = 9
            elif rakas == 3:
                gep = 7
            elif rakas == 7:
                gep = 3
            elif rakas == 9:
                gep = 1
            elif gep == 2 and rakas != 3:
                gep = 3
            elif gep == 2 and rakas == 3:
                gep = 7
            elif gep == 8 and rakas != 7:
                gep = 7
            elif gep == 8 and rakas == 7:
                gep = 3
            foglalt.append(gep)
            szamitogép.append(gep)
            if gep == 1:
                egy = "x"
            elif gep == 2:
                ketto = "x"
            elif gep == 3:
                harom = "x"
            elif gep == 4:
                negy = "x"
            elif gep == 5:
                ot = "x"
            elif gep == 6:
                hat = "x"
            elif gep == 7:
                het = "x"
            elif gep == 8:
                nyolc = "x"
            else:
                kilenc = "x"
            turn += 1
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        #777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        while turn == 7:
            rakas = int(input("Hova szeretnél tenni?(1-9)\n"))
            foglalt.append(rakas)
            ember.append(rakas)
            if rakas == 1:
                egy = "o"
            elif rakas == 2:
                ketto = "o"
            elif rakas == 3:
                harom = "o"
            elif rakas == 4:
                negy = "o"
            elif rakas == 5:
                ot = "o"
            elif rakas == 6:
                hat = "o"
            elif rakas == 7:
                het = "o"
            elif rakas == 8:
                nyolc = "o"
            elif rakas == 9:
                kilenc = "o"
            else:
                print("Elbasztad")
            turn += 1
            os.system('cls')
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")

        time.sleep(2)
        os.system('cls')
        #888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        while turn == 8:
            if rakas == 1 or rakas == 3 or rakas == 7 or rakas == 9:
                gep = 5
            foglalt.append(gep)
            szamitogép.append(gep)
            if gep == 1:
                egy = "x"
            elif gep == 2:
                ketto = "x"
            elif gep == 3:
                harom = "x"
            elif gep == 4:
                negy = "x"
            elif gep == 5:
                ot = "x"
            elif gep == 6:
                hat = "x"
            elif gep == 7:
                het = "x"
            elif gep == 8:
                nyolc = "x"
            else:
                kilenc = "x"
            turn += 1
            print(f"{egy} | {ketto} | {harom}\n----------\n{negy} | {ot} | {hat}\n----------\n{het} | {nyolc} | {kilenc}")


        jatek = input("Szeretnél újra játszani? (y/n)\n")

else:
    print("ok.")
    os.system('cls')