# from datetime import *
# from calendar import *
# from math import *
# from time import strptime

# #�lesanne 1
# tana=date.today() 
# print(f"Tere! T�na on {tana}")

# # 27/12/2022
# tana1 = tana.strftime("%d/%m/%Y")
# print(tana1)

# # December 27, 2022
# tana2 = tana.strftime("%B %d, %Y")
# print(tana2)

# # 12/27/22
# tana3 = tana.strftime("%m/%d/%y")
# print(tana3)

# # Dec-27-2022
# tana4 = tana.strftime("%b-%d-%Y")
# print(tana4)

# p�ev=tana.day
# kuu=tana.month
# aasta=tana.year

# print(f"P�ev on {p�ev}, \nKuu on {kuu}, \nAasta on {aasta}")

# paevad=monthrange(2025,2)[1]
# onjaanud=paevad-p�ev
# print(f"kuu l�puni on j��nud {onjaanud} p�evad")

# paev1=monthrange(2025,2)[1]
# paev2=monthrange(2025,3)[1]
# paev3=monthrange(2025,4)[1]
# paev4=monthrange(2025,5)[1]
# paev5=monthrange(2025,6)[1]
# paev6=monthrange(2025,7)[1]
# paev7=monthrange(2025,8)[1]


# while True:
#     try:
#         isikukood=input("Sisesta teie isikukood: ")
#         if isikukood.isdigit() and len(isikukood)==11:
#             ik_list=list(isikukood)
#             print(ik_list)
#             if int(ik_list[0]) in [1,3,5]:
#                 sugu="Mees"
#             elif int(ik_list[0]) in [2,4,6]:
#                 sugu="Naine"
#             else:
#                 print("Esimene s�mbol pole �ige")
#                 continue
#             print("2-7 s. kontroll")

#         else:
#             print("Isikukood on numbrid.")
#     except:
#         print("Viga andmetega")
#         int(ik_list[3]+ik_list[4])in range(1-13):
#              print("4,5 s�mbolid pole ok")


# haigla={
#     range(1,10):"Kuressaare Haigla"
#     range(11,19):("Tartu �likooli Naistekliinik, Tartumaa, Tartu")
#     range(21,220):("Ida-Tallinna Keskhaigla, Pelgulinna s�nnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla")
#     range(221,270):("Ida-Viru Keskhaigla (Kohtla-J�rve, endine J�hvi)")
#     range(271,370):("Maarjam�isa Kliinikum (Tartu), J�geva Haigla")
#     range(371,420):("Narva Haigla")
#     range(421,470):"P�rnu Haigla"
#     range(471,490):"Pelgulinna S�nnitusmaja (Tallinn), Haapsalu haigla"
#     range(491,520):"J�rvamaa Haigla (Paide)"
#     range(521,570):"Rakvere, Tapa haigla"
#     range(571,600):"Valga Haigla"
#     range(601,650):"Viljandi Haigla"
#     range(651,700):"L�una-Eesti Haigla (V�ru), P�lva Haigla " 
# }
# hospital_code=[]
# if 1 <= int(hospital_code) <= 10:
#             hospital = "Kuressaare Haigla"
# elif 11 <= int(hospital_code) <= 19:
#             hospital = "Tartu �likooli Naistekliinik, Tartumaa, Tartu"
# elif 21 <= int(hospital_code) <= 220:
#             hospital = "Ida-Tallinna Keskhaigla, Pelgulinna s�nnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
# elif 221 <= int(hospital_code) <= 270:
#             hospital = "Ida-Viru Keskhaigla (Kohtla-J�rve, endine J�hvi)"
# elif 271 <= int(hospital_code) <= 370:
#             hospital = "Maarjam�isa Kliinikum (Tartu), J�geva Haigla"
# elif 371 <= int(hospital_code) <= 420:
#             hospital = "Narva Haigla"
# elif 421 <= int(hospital_code) <= 470:
#             hospital = "P�rnu Haigla"
# elif 471 <= int(hospital_code) <= 490:
#             hospital = "Pelgulinna S�nnitusmaja (Tallinn), Haapsalu haigla"
# elif 491 <= int(hospital_code) <= 520:
#             hospital = "J�rvamaa Haigla (Paide)"
# elif 521 <= int(hospital_code) <= 570:
#             hospital = "Rakvere, Tapa haigla"
# elif 571 <= int(hospital_code) <= 600:
#             hospital = "Valga Haigla"
# elif 601 <= int(hospital_code) <= 650:
#             hospital = "Viljandi Haigla"
# elif 651 <= int(hospital_code) <= 700:
#             hospital = "L�una-Eesti Haigla (V�ru), P�lva Haigla"
# else:
#       hospital = "Tundmatu haigla"

while True:
    try:
        isikukood=input("Sisesta teie isikukood: ")
        if isikukood.isdigit() and len(isikukood)==11:
            ik_list=list(isikukood)
            print(ik_list)
            if int(ik_list[0]) in [1,3,5]:
                sugu="Mees"
            elif int(ik_list[0]) in [2,4,6]:
                sugu="Naine"
            else:
                print("Esimene s�mbol pole �ige")
                continue
            print("2-7 s. kontroll")
            if int(ik_list[1]+ik_list[2]) in range(0,100):
                print("2,3 s�mbolid on ok")
                #!!! aasta=...
                if int(ik_list[3]+ik_list[4])in range(1,13):
                    print("4,5 s�bolid on ok")
                    if int(ik_list[5]+ik_list[6])in range(1,32) and int(ik_list[3]+ik_list[4]) in range(1,13,2) or int(ik_list[5]+ik_list[6]) in range(1,31) and int(ik_list[3]+ik_list[4]) in range(4,13,2) or int(ik_list[5]+ik_list[6]) in range(1,30) and int(ik_list[3]+ik_list[4])==2:
                        print("6,7 s�mbolid on ok")
                        print("Kontrollnumber")
                        # summa=0
                        # for i, s in enumerate(ik_list):  #i=0,1,2,3,4,5.. s="3,"1"....
                        #    summa+=(i+1)*int(s)
                        # aste1=[1,2,3,4,5,6,7,8,9,1]
                        # aste2=[3,4,5,6,7,8,9,1,2,3]
                        # ik_n_list=[4,7,6,1,0,2,3,4,5]
                        # for s in range(ik_list):
                        #     ik_n_list.append(int(s))
                        sum1=int(ik_list[0])*1+int(ik_list[1])*2+int(ik_list[2])*3+int(ik_list[3])*4+int(ik_list[4])*5+int(ik_list[5])*6+int(ik_list[6])*7+int(ik_list[7])*8+int(ik_list[8])*9+int(ik_list[9])*1
                        sum2=round(sum1/11)
                        sum3=sum2*11
                        sum8=sum1-sum3
                        print(sum8)
                        sum4=int(ik_list[0])*3+int(ik_list[1])*4+int(ik_list[2])*5+int(ik_list[3])*6+int(ik_list[4])*7+int(ik_list[5])*8+int(ik_list[6])*9+int(ik_list[7])*1+int(ik_list[8])*2+int(ik_list[9])*3
                        sum5=round(sum4/11)
                        sum6=sum5*11
                        sum7=sum4-sum6
                        print(sum7)
                    else:
                        print("6,7 s�mbolid pole ok")
                        continue
                else:
                    print("4,5 s�mbolid pole ok")
                continue
            else:
             print("2,3 s�mbolid pole ok")
        else:
            print("Isikukood on numbrid.")
    except:
        print("Viga andmetega")







