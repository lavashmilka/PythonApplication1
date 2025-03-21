# from datetime import *
# from calendar import *
# from math import *
# from time import strptime

# #Ülesanne 1
# tana=date.today() 
# print(f"Tere! Täna on {tana}")

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

# päev=tana.day
# kuu=tana.month
# aasta=tana.year

# print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")

# paevad=monthrange(2025,2)[1]
# onjaanud=paevad-päev
# print(f"kuu lõpuni on jäänud {onjaanud} päevad")

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
#                 print("Esimene sümbol pole õige")
#                 continue
#             print("2-7 s. kontroll")

#         else:
#             print("Isikukood on numbrid.")
#     except:
#         print("Viga andmetega")
#         int(ik_list[3]+ik_list[4])in range(1-13):
#              print("4,5 sümbolid pole ok")


# haigla={
#     range(1,10):"Kuressaare Haigla"
#     range(11,19):("Tartu Ülikooli Naistekliinik, Tartumaa, Tartu")
#     range(21,220):("Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla")
#     range(221,270):("Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)")
#     range(271,370):("Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla")
#     range(371,420):("Narva Haigla")
#     range(421,470):"Pärnu Haigla"
#     range(471,490):"Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
#     range(491,520):"Järvamaa Haigla (Paide)"
#     range(521,570):"Rakvere, Tapa haigla"
#     range(571,600):"Valga Haigla"
#     range(601,650):"Viljandi Haigla"
#     range(651,700):"Lõuna-Eesti Haigla (Võru), Põlva Haigla " 
# }
# hospital_code=[]
# if 1 <= int(hospital_code) <= 10:
#             hospital = "Kuressaare Haigla"
# elif 11 <= int(hospital_code) <= 19:
#             hospital = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
# elif 21 <= int(hospital_code) <= 220:
#             hospital = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
# elif 221 <= int(hospital_code) <= 270:
#             hospital = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
# elif 271 <= int(hospital_code) <= 370:
#             hospital = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
# elif 371 <= int(hospital_code) <= 420:
#             hospital = "Narva Haigla"
# elif 421 <= int(hospital_code) <= 470:
#             hospital = "Pärnu Haigla"
# elif 471 <= int(hospital_code) <= 490:
#             hospital = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
# elif 491 <= int(hospital_code) <= 520:
#             hospital = "Järvamaa Haigla (Paide)"
# elif 521 <= int(hospital_code) <= 570:
#             hospital = "Rakvere, Tapa haigla"
# elif 571 <= int(hospital_code) <= 600:
#             hospital = "Valga Haigla"
# elif 601 <= int(hospital_code) <= 650:
#             hospital = "Viljandi Haigla"
# elif 651 <= int(hospital_code) <= 700:
#             hospital = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
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
                print("Esimene sümbol pole õige")
                continue
            print("2-7 s. kontroll")
            if int(ik_list[1]+ik_list[2]) in range(0,100):
                print("2,3 sümbolid on ok")
                #!!! aasta=...
                if int(ik_list[3]+ik_list[4])in range(1,13):
                    print("4,5 sübolid on ok")
                    if int(ik_list[5]+ik_list[6])in range(1,32) and int(ik_list[3]+ik_list[4]) in range(1,13,2) or int(ik_list[5]+ik_list[6]) in range(1,31) and int(ik_list[3]+ik_list[4]) in range(4,13,2) or int(ik_list[5]+ik_list[6]) in range(1,30) and int(ik_list[3]+ik_list[4])==2:
                        print("6,7 sümbolid on ok")
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
                        print("6,7 sümbolid pole ok")
                        continue
                else:
                    print("4,5 sümbolid pole ok")
                continue
            else:
             print("2,3 sümbolid pole ok")
        else:
            print("Isikukood on numbrid.")
    except:
        print("Viga andmetega")







