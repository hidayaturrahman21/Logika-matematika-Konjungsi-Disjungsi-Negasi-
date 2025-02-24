# MENAMPILKAN JUDUL TABEL 
print ("TABEL KEBENARAN DISJUNGSI")
print ("_____________________________")
#MENAMPILKAN HEADER TABEL
print ("| P\t|Q\t|P OR Q|")
print ("_____________________________")

#MENGGUNAKAN OPERATOR LOGIKA 'OR'
for P in [True,False]: #LOOP T UNTUK P
    for Q in [True,False]: #LOP II UNTUK Q
        Disjungsi = P or Q #MELAKUKAN OPERASI P OR Q 
        print(f"{P}\t{Q}\t{Disjungsi}") #MENCETAK HASIL
