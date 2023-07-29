import requests
from bs4 import BeautifulSoup

# URL halaman web yang berisi tabel
url = 'http://server.getsensync.com/project/menu/qua/sparing3.php?id=sparing02'

# Mengambil konten halaman web menggunakan Requests
response = requests.get(url)

# Membuat objek BeautifulSoup untuk parsing HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Mengidentifikasi tabel dengan menggunakan tag <table>
table = soup.find('table')

# Mengambil baris ke-2 dari tabel (indeks dimulai dari 0)
row_index = 1
row = table.findAll('tr')[row_index]

# Mengambil elemen <td> ke-2 dari baris tersebut (indeks dimulai dari 0)
td_index = 1
td = row.findAll('td')[td_index]

# Mengekstrak teks dari elemen <td>
ph = td.text.strip()

tanggal_index = 0
tanggal = row.findAll('td')[tanggal_index]

# Mengekstrak teks dari elemen <td>
tanggal = tanggal.text.strip()

tss_index = 2
tss = row.findAll('td')[tss_index]

# Mengekstrak teks dari elemen <td>
tss = tss.text.strip()

cod_index = 3
cod = row.findAll('td')[cod_index]

# Mengekstrak teks dari elemen <td>
cod = cod.text.strip()

nh3n_index = 4
nh3n = row.findAll('td')[nh3n_index]

# Mengekstrak teks dari elemen <td>
nh3n = nh3n.text.strip()

# Cetak data
print("============= POLYSTER ==============")
print("Tanggal:"+tanggal)
print("pH:"+ph)
print("TSS:"+tss)
print("COD:"+cod)
print("NH3N:"+nh3n)
print("=====================================")
type_var1 = type(ph)
baru = float(ph)
baru2 = type(baru)
# Cetak hasil
print("Tipe data var1:", type_var1)
print("Data Baru:", baru)
print("Type: ",baru2)