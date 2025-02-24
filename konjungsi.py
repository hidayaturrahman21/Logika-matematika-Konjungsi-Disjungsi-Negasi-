# MENAMPILKAN JUDUL TABEL 
print ("TABEL KEBENARAN KONJUNGSI")
print ("_____________________________")
#MENAMPILKAN HEADER TABEL
print ("|P\t|Q\t|P AND Q|")
print ("_____________________________")

#MENGGUNAKAN OPERATOR LOGIKA 'AND'
for P in [True,False]: #LOOP T UNTUK P
    for Q in [True,False]: #LOP II UNTUK Q
        Konjungsi = P and Q #MELAKUKAN OPERASI P AND Q 
        print(f"{P}\t{Q}\t{Konjungsi}") #MENCETAK HASIL

