# MENAMPILKAN JUDUL TABEL
print("TABEL KEBENARAN NOT P DISJUNGSI Q ")
print("_______________________________________")

# MENAMPILKAN HEADER TABEL
print("| P\t| Q\t| ¬P or Q |")
print("_______________________________________")

# MENGGUNAKAN OPERATOR LOGIKA 'NOT P OR Q'
for P in [True, False]:  # LOOP I UNTUK P
    for Q in [True, False]:  # LOOP II UNTUK Q
        implikasi = not P or Q  # MELAKUKAN OPERASI P or Q
        print(f"| {P}\t| {Q}\t| {implikasi}  |")  # MENCETAK HASIL 
