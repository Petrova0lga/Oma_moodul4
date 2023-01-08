from datetime import datetime


def kas_isikukood_valid(isikukood: str):
    """Isikukoodi kontroll number
    On vaja isikukood sisestada
    :param str ik: Inimese isikukood
    :rtype: var Märamata tüüp
    """

    ik_list = list(isikukood)
    s = 0
    for i in range(0, 10):
        s += (i % 9 + 1) * int(ik_list[i])
        # print(f"{i % 9 + 1}*{int(ik_list[i])}+", end="")
    # print(s)
    s = s - (s // 11) * 11
    # print(s)

    if s == int(ik_list[10]):
        vastus = s
    else:
        vastus = "Kontroll number on vale"
    return vastus


def haigla_nimi(ik3: int):
    """Haigla 3 isikukoodi numbri alusel
    :param int ik3: Isikukoodi 3 numbrid
    :rtype: str Haigla ja koht
    """
    if 1 <= ik3 <= 10:
        return "Kuressaare Haigla"
    elif 11 <= ik3 <= 19:
        return "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= ik3 <= 220:
        return "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221 <= ik3 <= 270:
        return "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= ik3 <= 370:
        return "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= ik3 <= 420:
        return "Narva Haigla"
    elif 421 <= ik3 <= 470:
        return "Pärnu Haigla"
    elif 471 <= ik3 <= 490:
        return "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491 <= ik3 <= 520:
        return "Järvamaa Haigla (Paide)"
    elif 521 <= ik3 <= 570:
        return "Rakvere, Tapa haigla"
    elif 571 <= ik3 <= 600:
        return "Valga Haigla"
    elif 601 <= ik3 <= 650:
        return "Viljandi Haigla"
    elif 651 <= ik3 <= 700:
        return "Lõuna-Eesti Haigla (Võru), Põlva Haigla"

    return "Haigla"


def sugu_numbrist(ik1: int) -> str:
    """
    """
    return "naine" if ik1 % 2 == 0 else "mees"


def aasta_numbrist(num: int):
    if int(num) in [1, 2]:
        return 1800
    elif int(num) in [3, 4]:
        return 1900

    return 2000

def kas_sugu_number_valid(sugu_num):
    if int(sugu_num) not in [1, 2, 3, 4, 5, 6]:
        print("Esimene sümbol/arv on vale ")
        raise Exception("")

def format_kuupaev(kuupaev: int):
    if kuupaev < 10:
        return "0" + str(kuupaev)
    return str(kuupaev)

def parse_isikukood(ik: str):
    if len(ik) != 11:
        print("Sümbolite arv peab 11 olema ")
        raise Exception("")

    ik_list = list(ik)  # ik_list["4","9","9"...,...]

    if not all([ik_num.isdigit() for ik_num in ik_list]):
        print("Andmetüüp on vale, On vaja numbreid sisestada")
        raise Exception("")

    kas_sugu_number_valid(ik_list[0])

    a = aasta_numbrist(ik_list[0])
    aasta = a + int(ik_list[1] + ik_list[2])
    kuu = int(ik_list[3] + ik_list[4])
    paev = int(ik_list[5] + ik_list[6])

    datetime(aasta, kuu, paev)
    vastus = kas_isikukood_valid(ik)

    if type(vastus) != int:
        print(vastus)
        raise Exception("")

    haigla = haigla_nimi(int(ik[7:10]))
    sugu = sugu_numbrist(int(ik_list[0]))
    tekst = "See on {sugu}, tema sünnipäev on {sp} ja sünnikoht: {sk}\n"
    sp = format_kuupaev(paev) + "." + format_kuupaev(kuu) + "." + str(aasta)
    return tekst.format(sugu=sugu, sp=sp, sk=haigla)

