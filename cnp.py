while True:
    cnp = input("Care e CNP-ul tau? ")
    if len(cnp) == 13 and cnp.isdigit():
        print("CNP valid, urmeaza verificarea...")
        break
    else:
        print("Introdu CNP-ul corect.")

def verificare_cnp(cnp):
    control = "279146358279"
    suma = 0

    for i in range(12):
        cifra_cnp = int(cnp[i])
        cifra_control = int(control[i])
        suma += cifra_cnp * cifra_control

    rest = suma % 11
    cifra_calculata = 1 if rest == 10 else rest

    return cifra_calculata == int(cnp[-1])


if verificare_cnp(cnp):
    print("CNP valid – cifra de control corecta!")
else:
    print("CNP invalid – cifra de control gresita!")


def informatii_cnp(cnp):
    S = int(cnp[0])
    AA = int(cnp[1:3])
    LL = int(cnp[3:5])
    ZZ = int(cnp[5:7])
    JJ = (cnp[7:9])

    if S in [1, 3, 5, 7, 9]:
        gen = "Maculin"
    if S in [1, 2]:
        an = 1900 + AA
    elif S in [3, 4]:
        an = 1800 + AA
    elif S in [5, 6]:
        an = 2000 + AA
    elif S in [7, 8, 9]:
        an = 1900 + AA


    judete = {
        "01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor",
        "06": "Bistrița-Năsăud", "07": "Botoșani", "08": "Brașov", "09": "Brăila", "10": "Buzău",
        "11": "Caraș-Severin", "12": "Cluj", "13": "Constanța", "14": "Covasna", "15": "Dâmbovița",
        "16": "Dolj", "17": "Galați", "18": "Gorj", "19": "Harghita", "20": "Hunedoara",
        "21": "Ialomița", "22": "Iași", "23": "Ilfov", "24": "Maramureș", "25": "Mehedinți",
        "26": "Mureș", "27": "Neamț", "28": "Olt", "29": "Prahova", "30": "Satu Mare",
        "31": "Sălaj", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timiș",
        "36": "Tulcea", "37": "Vaslui", "38": "Vâlcea", "39": "Vrancea", "40": "București",
        "41": "București Sector 1", "42": "București Sector 2", "43": "București Sector 3",
        "44": "București Sector 4", "45": "București Sector 5", "46": "București Sector 6",
        "51": "Călărași", "52": "Giurgiu"
    }

    judet = judete.get(JJ)

    print(f"Genul: {gen}")
    print(f"Data Nasterii: {ZZ:02d}.{LL:02d}.{an}")
    print(f"Judetul nasterii: {judet}")

informatii_cnp(cnp)
