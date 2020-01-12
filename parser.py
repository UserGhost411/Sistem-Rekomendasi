arrdata = []
completedata = []
countload = 0
current_harga = 0
arrpilihan = []
arrdata = open("tiket_pesawat.txt", "r")
for x in arrdata:
	if (countload):
		completedata.append(x.replace("\n","").split("\t"))
	countload += 1
print(countload,"data berhasil diload")
asal = "jakarta"#input("masukan asal:")
tujuan = "denpasar"#input("masukan tujuan:")
jumlahpng = 2
i = 0
for x in completedata:
	if(x[1].lower()==asal and x[2].lower()==tujuan):
		i+=1
		print("{}.{:<10}\t{}-{}\t{}".format(i,x[0],x[1],x[2],x[3]))
		arrpilihan.append(x)
pilih = int(input("Pilihin aku dong:"))
harganet = jumlahpng*int(arrpilihan[pilih-1][3])
print("total harga Tiket: ({} x {}) + 10% = RP{}".format(jumlahpng,arrpilihan[pilih-1][3],harganet+(harganet*0.1)))
hargapesawat = harganet+(harganet*0.1)
arrdata = open("harga_hotel.txt", "r")
completedata = []
countload = 0 
for x in arrdata:
	completedata.append(x.replace("\n","").split("\t"))
	countload += 1
i = 0
rekom = []
for x in completedata:
	if(x[0].lower()==tujuan):
		for xx in x:
			if(i):
				rekom.append([int(xx.replace('.00',"").replace(',',"").replace('"',"").strip()),completedata[0][i]])
			i+=1
rekom.sort()
for x in rekom:		
	print("{}\t\t{}".format(x[1],x[0]))
hotelid = input("Masukan Hotel (Aplhabet):")
for x in rekom:		
	if(hotelid.upper()==x[1][6]):
		hargahotel = int(x[0])
print("Total Biaya:")
print("Rp{} + Rp{} = Rp{}".format(hargapesawat,hargahotel,hargahotel+hargapesawat))
