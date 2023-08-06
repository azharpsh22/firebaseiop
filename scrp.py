import requests
from bs4 import BeautifulSoup
import time


def indotaiseia():
# Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
        td_index = 1
        td = row3.findAll('td')[td_index]

        # Mengekstrak teks dari elemen <td>
        ph = td.text.strip()

        tanggal_index = 0
        tanggal = row3.findAll('td')[tanggal_index]

        # Mengekstrak teks dari elemen <td>
        tanggal = tanggal.text.strip()

        tss_index = 2
        tss = row3.findAll('td')[tss_index]

        # Mengekstrak teks dari elemen <td>
        tss = tss.text.strip()

        cod_index = 3
        cod = row3.findAll('td')[cod_index]

        # Mengekstrak teks dari elemen <td>
        cod = cod.text.strip()

        nh3n_index = 4
        nh3n = row3.findAll('td')[nh3n_index]

        # Mengekstrak teks dari elemen <td>
        nh3n = nh3n.text.strip()

        debit_index = 5
        debit = row3.findAll('td')[debit_index]

        # Mengekstrak teks dari elemen <td>
        debit = debit.text.strip()
        cktss = float(tss)
        ckcod = float(cod)
        ckph  = float(ph)
        cknh3 = float(nh3n)
        # Cetak data
        print("============= Indotasei ==============")
        print("                                           ")
        if cktss >= 30.00:
                cektss = "  \033[91mBAHAYA\033[0m"
        else:
                cektss = "  \033[92mAman\033[0m"
        if ckph >= 9.0 or ckph <= 6.00:
                cekph = "  \033[91mBAHAYA\033[0m"
        else:
                cekph = "  \033[92mAman\033[0m"
        if ckcod >= 115:
                cekcod = "  \033[91mBAHAYA\033[0m"
        else:
                cekcod = "  \033[92mAman\033[0m"
        if cknh3 >= 20.00:
                ceknh3 = "  \033[91mBAHAYA\033[0m"
        else:
                ceknh3 = "  \033[92mAman\033[0m"
        print("Tanggal:"+"   "+tanggal)
        print("pH:"+"   "+ph+cekph)
        print("TSS:"+"   "+tss+cektss)
        print("COD:"+"   "+cod+cekcod)
        print("NH3N:"+"   "+nh3n+ceknh3)
        print("Debit:"+"   "+debit)
        print("                                           ")


def ppolyster():
# Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
        td_index = 1
        td = row1.findAll('td')[td_index]

        # Mengekstrak teks dari elemen <td>
        ph = td.text.strip()

        tanggal_index = 0
        tanggal = row1.findAll('td')[tanggal_index]

        # Mengekstrak teks dari elemen <td>
        tanggal = tanggal.text.strip()

        tss_index = 2
        tss = row1.findAll('td')[tss_index]

        # Mengekstrak teks dari elemen <td>
        tss = tss.text.strip()

        cod_index = 3
        cod = row1.findAll('td')[cod_index]

        # Mengekstrak teks dari elemen <td>
        cod = cod.text.strip()

        nh3n_index = 4
        nh3n = row1.findAll('td')[nh3n_index]

        # Mengekstrak teks dari elemen <td>
        nh3n = nh3n.text.strip()

        debit_index = 5
        debit = row1.findAll('td')[debit_index]

        # Mengekstrak teks dari elemen <td>
        debit = debit.text.strip()
        cktss = float(tss)
        ckcod = float(cod)
        ckph  = float(ph)
        cknh3 = float(nh3n)
        # Cetak data
        print("============= Polyster ==============")
        print("                                           ")
        if cktss >= 30.00:
                cektss = "  \033[91mBAHAYA\033[0m"
        else:
                cektss = "  \033[92mAman\033[0m"
        if ckph >= 9.0 or ckph <= 6.00:
                cekph = "  \033[91mBAHAYA\033[0m"
        else:
                cekph = "  \033[92mAman\033[0m"
        if ckcod >= 115:
                cekcod = "  \033[91mBAHAYA\033[0m"
        else:
                cekcod = "  \033[92mAman\033[0m"
        if cknh3 >= 20.00:
                ceknh3 = "  \033[91mBAHAYA\033[0m"
        else:
                ceknh3 = "  \033[92mAman\033[0m"
        print("Tanggal:"+"   "+tanggal)
        print("pH:"+"   "+ph+cekph)
        print("TSS:"+"   "+tss+cektss)
        print("COD:"+"   "+cod+cekcod)
        print("NH3N:"+"   "+nh3n+ceknh3)
        print("Debit:"+"   "+debit)
        print("                                           ")

def bbesland():
# Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
        td_index = 1
        td = row2.findAll('td')[td_index]

        # Mengekstrak teks dari elemen <td>
        ph = td.text.strip()

        tanggal_index = 0
        tanggal = row2.findAll('td')[tanggal_index]

        # Mengekstrak teks dari elemen <td>
        tanggal = tanggal.text.strip()

        tss_index = 2
        tss = row2.findAll('td')[tss_index]

        # Mengekstrak teks dari elemen <td>
        tss = tss.text.strip()

        cod_index = 3
        cod = row2.findAll('td')[cod_index]

        # Mengekstrak teks dari elemen <td>
        cod = cod.text.strip()
  
        nh3n_index = 4
        nh3n = row2.findAll('td')[nh3n_index]

        # Mengekstrak teks dari elemen <td>
        nh3n = nh3n.text.strip()

        debit_index = 5
        debit = row2.findAll('td')[debit_index]

        # Mengekstrak teks dari elemen <td>
        debit = debit.text.strip()
        cktss = float(tss)
        ckcod = float(cod)
        ckph  = float(ph)
        cknh3 = float(nh3n)
        # Cetak data
        print("============= Besland ==============")
        print("                                    ")
        if cktss >= 30.00:
                cektss = "  \033[91mBAHAYA\033[0m"
        else:
                cektss = "  \033[92mAman\033[0m"
        if ckph >= 9.0 or ckph <= 6.00:
                cekph = "  \033[91mBAHAYA\033[0m"
        else:
                cekph = "  \033[92mAman\033[0m"
        if ckcod >= 115 or ckcod >= 60.00:
                cekcod = "  \033[91mBAHAYA\033[0m"
        else:
                cekcod = "  \033[92mAman\033[0m"
        if cknh3 >= 20.00 or cknh3 >= 3.00:
                ceknh3 = "  \033[91mBAHAYA\033[0m"
        else:
                ceknh3 = "  \033[92mAman\033[0m"
        print("Tanggal:"+"   "+tanggal)
        print("pH:"+"   "+ph+cekph)
        print("TSS:"+"   "+tss+cektss)
        print("COD:"+"   "+cod+cekcod)
        print("NH3N:"+"   "+nh3n+ceknh3)
        print("Debit:"+"   "+debit)
        print("                                           ")


def wwving1():
        # Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
        td_index = 1
        td = row4.findAll('td')[td_index]

        # Mengekstrak teks dari elemen <td>
        ph = td.text.strip()

        tanggal_index = 0
        tanggal = row4.findAll('td')[tanggal_index]

        # Mengekstrak teks dari elemen <td>
        tanggal = tanggal.text.strip()

        tss_index = 2
        tss = row4.findAll('td')[tss_index]

        # Mengekstrak teks dari elemen <td>
        tss = tss.text.strip()

        cod_index = 3
        cod = row4.findAll('td')[cod_index]

        # Mengekstrak teks dari elemen <td>
        cod = cod.text.strip()
  
        nh3n_index = 4
        nh3n = row4.findAll('td')[nh3n_index]

        # Mengekstrak teks dari elemen <td>
        nh3n = nh3n.text.strip()

        debit_index = 5
        debit = row4.findAll('td')[debit_index]

        # Mengekstrak teks dari elemen <td>
        debit = debit.text.strip()
        cktss = float(tss)
        ckcod = float(cod)
        ckph  = float(ph)
        cknh3 = float(nh3n)
        # Cetak data
        print("============= Weaving 01 ==============")
        print("                                    ")
        if cktss >= 30.00:
                cektss = "  \033[91mBAHAYA\033[0m"
        else:
                cektss = "  \033[92mAman\033[0m"
        if ckph >= 9.0 or ckph <= 6.00:
                cekph = "  \033[91mBAHAYA\033[0m"
        else:
                cekph = "  \033[92mAman\033[0m"
        if ckcod >= 115 or ckcod >= 60.00:
                cekcod = "  \033[91mBAHAYA\033[0m"
        else:
                cekcod = "  \033[92mAman\033[0m"
        if cknh3 >= 20.00 or cknh3 >= 3.00:
                ceknh3 = "  \033[91mBAHAYA\033[0m"
        else:
                ceknh3 = "  \033[92mAman\033[0m"
        print("Tanggal:"+"   "+tanggal)
        print("pH:"+"   "+ph+cekph)
        print("TSS:"+"   "+tss+cektss)
        print("COD:"+"   "+cod+cekcod)
        print("NH3N:"+"   "+nh3n+ceknh3)
        print("Debit:"+"   "+debit)
        print("                                           ")

def wwving2():
        # Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
        td_index = 1
        td = row5.findAll('td')[td_index]

        # Mengekstrak teks dari elemen <td>
        ph = td.text.strip()

        tanggal_index = 0
        tanggal = row5.findAll('td')[tanggal_index]

        # Mengekstrak teks dari elemen <td>
        tanggal = tanggal.text.strip()

        tss_index = 2
        tss = row5.findAll('td')[tss_index]

        # Mengekstrak teks dari elemen <td>
        tss = tss.text.strip()

        cod_index = 3
        cod = row5.findAll('td')[cod_index]

        # Mengekstrak teks dari elemen <td>
        cod = cod.text.strip()
  
        nh3n_index = 4
        nh3n = row5.findAll('td')[nh3n_index]

        # Mengekstrak teks dari elemen <td>
        nh3n = nh3n.text.strip()

        debit_index = 5
        debit = row5.findAll('td')[debit_index]

        # Mengekstrak teks dari elemen <td>
        debit = debit.text.strip()
        cktss = float(tss)
        ckcod = float(cod)
        ckph  = float(ph)
        cknh3 = float(nh3n)
        # Cetak data
        print("============= Weaving 02 ==============")
        print("                                    ")
        if cktss >= 30.00:
                cektss = "  \033[91mBAHAYA\033[0m"
        else:
                cektss = "  \033[92mAman\033[0m"
        if ckph >= 9.0 or ckph <= 6.00:
                cekph = "  \033[91mBAHAYA\033[0m"
        else:
                cekph = "  \033[92mAman\033[0m"
        if ckcod >= 115 or ckcod >= 60.00:
                cekcod = "  \033[91mBAHAYA\033[0m"
        else:
                cekcod = "  \033[92mAman\033[0m"
        if cknh3 >= 20.00 or cknh3 >= 3.00:
                ceknh3 = "  \033[91mBAHAYA\033[0m"
        else:
                ceknh3 = "  \033[92mAman\033[0m"
        print("Tanggal:"+"   "+tanggal)
        print("pH:"+"   "+ph+cekph)
        print("TSS:"+"   "+tss+cektss)
        print("COD:"+"   "+cod+cekcod)
        print("NH3N:"+"   "+nh3n+ceknh3)
        print("Debit:"+"   "+debit)
        print("                                           ")


def sspinning():
        # Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
        td_index = 1
        td = row6.findAll('td')[td_index]

        # Mengekstrak teks dari elemen <td>
        ph = td.text.strip()

        tanggal_index = 0
        tanggal = row6.findAll('td')[tanggal_index]

        # Mengekstrak teks dari elemen <td>
        tanggal = tanggal.text.strip()

        tss_index = 2
        tss = row6.findAll('td')[tss_index]

        # Mengekstrak teks dari elemen <td>
        tss = tss.text.strip()

        cod_index = 3
        cod = row6.findAll('td')[cod_index]

        # Mengekstrak teks dari elemen <td>
        cod = cod.text.strip()
  
        nh3n_index = 4
        nh3n = row6.findAll('td')[nh3n_index]

        # Mengekstrak teks dari elemen <td>
        nh3n = nh3n.text.strip()

        debit_index = 5
        debit = row6.findAll('td')[debit_index]

        # Mengekstrak teks dari elemen <td>
        debit = debit.text.strip()
        cktss = float(tss)
        ckcod = float(cod)
        ckph  = float(ph)
        cknh3 = float(nh3n)
        # Cetak data
        print("============= Spinning ==============")
        print("                                    ")
        if cktss >= 30.00:
                cektss = "  \033[91mBAHAYA\033[0m"
        else:
                cektss = "  \033[92mAman\033[0m"
        if ckph >= 9.0 or ckph <= 6.00:
                cekph = "  \033[91mBAHAYA\033[0m"
        else:
                cekph = "  \033[92mAman\033[0m"
        if ckcod >= 115 or ckcod >= 60.00:
                cekcod = "  \033[91mBAHAYA\033[0m"
        else:
                cekcod = "  \033[92mAman\033[0m"
        if cknh3 >= 20.00 or cknh3 >= 3.00:
                ceknh3 = "  \033[91mBAHAYA\033[0m"
        else:
                ceknh3 = "  \033[92mAman\033[0m"
        print("Tanggal:"+"   "+tanggal)
        print("pH:"+"   "+ph+cekph)
        print("TSS:"+"   "+tss+cektss)
        print("COD:"+"   "+cod+cekcod)
        print("NH3N:"+"   "+nh3n+ceknh3)
        print("Debit:"+"   "+debit)
        print("                                           ")
while True:
    # URL halaman web yang berisi tabel
    ##################### POlYSTER ######################################
    polyster = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=sparing02'

    # Mengambil konten halaman web menggunakan Requests
    response1 = requests.get(polyster)

    # Membuat objek BeautifulSoup untuk parsing HTML
    soup1 = BeautifulSoup(response1.text, 'html.parser')

    # Mengidentifikasi tabel dengan menggunakan tag <table>
    table1 = soup1.find('table')

    # Mengambil baris ke-2 dari tabel (indeks dimulai dari 0)
    row_index1 = 1
    row1 = table1.findAll('tr')[row_index1]

    ######################### BESLAND #############################

    besland = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=sparing05'

    # Mengambil konten halaman web menggunakan Requests
    response2 = requests.get(besland)

    # Membuat objek BeautifulSoup untuk parsing HTML
    soup2 = BeautifulSoup(response2.text, 'html.parser')

    # Mengidentifikasi tabel dengan menggunakan tag <table>
    table2 = soup2.find('table')

    # Mengambil baris ke-2 dari tabel (indeks dimulai dari 0)
    row_index2 = 1
    row2 = table2.findAll('tr')[row_index2]

    ##################### INDOTAISEI ##############################

    indotaisei = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=sparing06'

    # Mengambil konten halaman web menggunakan Requests
    response3 = requests.get(indotaisei)

    # Membuat objek BeautifulSoup untuk parsing HTML
    soup3 = BeautifulSoup(response3.text, 'html.parser')

    # Mengidentifikasi tabel dengan menggunakan tag <table>
    table3 = soup3.find('table')

    # Mengambil baris ke-3 dari tabel (indeks dimulai dari 0)
    row_index3 = 1
    row3 = table3.findAll('tr')[row_index3]

    #############################################################

    ##################### WEAVING 1 ##############################

    weaving1 = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=weaving01'

    # Mengambil konten halaman web menggunakan Requests
    response4 = requests.get(weaving1)

    # Membuat objek BeautifulSoup untuk parsing HTML
    soup4 = BeautifulSoup(response4.text, 'html.parser')

    # Mengidentifikasi tabel dengan menggunakan tag <table>
    table4 = soup4.find('table')

    # Mengambil baris ke-4 dari tabel (indeks dimulai dari 0)
    row_index4 = 1
    row4 = table4.findAll('tr')[row_index4]

    #############################################################

    ##################### WEAVING 2 ##############################

    weaving2 = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=weaving02'

    # Mengambil konten halaman web menggunakan Requests
    response5 = requests.get(weaving2)

    # Membuat objek BeautifulSoup untuk parsing HTML
    soup5 = BeautifulSoup(response5.text, 'html.parser')

    # Mengidentifikasi tabel dengan menggunakan tag <table>
    table5 = soup5.find('table')

    # Mengambil baris ke-5 dari tabel (indeks dimulai dari 0)
    row_index5 = 1
    row5 = table5.findAll('tr')[row_index5]

    #############################################################

    ##################### SPINNING ##############################

    spinning = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=spinning'

    # Mengambil konten halaman web menggunakan Requests
    response6 = requests.get(spinning)

    # Membuat objek BeautifulSoup untuk parsing HTML
    soup6 = BeautifulSoup(response6.text, 'html.parser')

    # Mengidentifikasi tabel dengan menggunakan tag <table>
    table6 = soup6.find('table')

    # Mengambil baris ke-6 dari tabel (indeks dimulai dari 0)
    row_index6 = 1
    row6 = table6.findAll('tr')[row_index6]

    #############################################################
    print("\033[94m******************************************\033[0m")
    print("--------------- SPARING -------------------")
    print("                                           ")
    ppolyster()
    bbesland()
    indotaiseia()
    print("-------------------------------------------")
    print("                                           ")
    print("--------------- SPARING PWK ---------------")
    print("                                           ")
    wwving1()
    wwving2()
    sspinning()
    print("-------------------------------------------")
    print("\033[94m******************************************\033[0m")
