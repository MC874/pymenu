import math

class colors:
	RED_BG = '\033[41m\033[1m'
	GREEN_BG = '\033[0;102m'
	GREEN = '\033[1;92m'
	ENDC = '\033[m'

List = [
		25,18,25,
		15,17,17,
		17,25,17,25,17,25,
		17,20,27,20,25,32,25,10,
		20,13,20,
		13,20,13,20,13,20,
		10,15,13,20,20,1,5,5,
		2,4,5,5,5,5,7,8,7,4,10,5.5,8.5,6,10,10
		]

print('''
[Paket Soto]									
1) Soto Kikil + Nasi = 25K						
2) Soto Ayam + Nasi	= 10K					
3) Soto Babat Usus + Nasi = 25K						

[Paket Nasi]									
4) Nasi Goreng Original = 15K				
5) Nasi Goreng Pelangi = 17K					
6) Nasi Goreng Spesial = 17K				

[Paket Ayam]									
7) Ayam Geprek Nasi	= 17K						
8) Ayam Kampung Geprek + Nasi = 25K
9) Ayam Saos Tiram Nasi = 17K			
10) Ayam Kampung Saos Tiram + Nasi = 25K
11) Ayam Mozarella + Nasi [Gak Ada] = 17K		
12) Ayam Kampung Mozarella + Nasi [Gak Ada] = 25k
												
[Paket Lain]									
13) Pecel Lele + Nasi = 17K
14) Nasi Timbel Kumplit = 20K
15) Nasi Timbel Kampung Kumplit = 27K
16) Rendang Kumplit = 20K
17) Ayam Bakar Kumplit = 25K
18) Ayam Bakar Kampung Kumplit = 32K
19) Ikan Bakar Kumplit = 25K
20) Nasi Biasa + Telor = 10K

[Satuan Soto]
21) Soto Kikil = 20K
22) Soto Ayam = 13K
23) Soto Babat = 20K

[Satuan Ayam]
24) Ayam Geprek = 13K
25) Ayam Kampung Geprek = 20K
26) Ayam Saos Tiram = 13K
27) Ayam Kampung Saos Tiram = 20K
28) Ayam Mozarella = 13K
29) Ayam Kampung Mozarella = 20K

[Satuan Lain]
30) Pecel Lele = 10K
31) Rendang = 15K
32) Ayam Bakar = 13K
33) Ayam Kampung Bakar = 20K
34) Ikan Bakar = 20K
35) Tahu/Tempe = 1K
36) Nasi = 5K
37) Telor Dadar = 5K

[Minuman]
38) Aqua Kecil = 2K
39) Aqua Besar = 4K
40) Sprite = 5K
41) Coca Cola = 5K
42) Fanta = 5K
43) Teh Pucuk = 5K
44) Larutan Kaleng = 7K
45) Adem Sari = 8K
46) Pocari Sweat = 7K
47) Teh Kotak = 4K
48) Mogu - Mogu = 10K
49) Pulpy Orange = 5.5K
50) You C 1000 = 8.5K
51) Kratindaeng = 6K
52) Juice = 10K
53) Sop Buah = 10K
''')
ans = input(' Pilih Menu: ')
total = 0
result = [int(x) for x in ans.split(', ')]
for i in result:
	total = total + List[i-1]
print('Total Harga: ' + colors.GREEN_BG + f' {str(total)} ' + colors.ENDC )
print()
uang = input(' Masukan Uang (Tanpa Ribu): ')
kembalian = int(uang) - int(total)
print('Kembalian: '+ colors.RED_BG + f' {str(kembalian)} ' + colors.ENDC)
