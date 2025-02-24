# MENAMPILKAN JUDUL TABEL
print("TABEL KEBENARAN NEGASI")
print("_____________________________")

# MENAMPILKAN HEADER TABEL
print("| P\t| Q\t| NOT P |")
print("_____________________________")

# MENGGUNAKAN OPERATOR LOGIKA 'NOT'
for P in [True, False]:  # LOOP I UNTUK P
    for Q in [True, False]:  # LOOP II UNTUK Q
        Negasi = not P  # MELAKUKAN OPERASI NEGASI P
        print(f"| {P}\t| {Q}\t| {Negasi} |")  # MENCETAK HASIL
