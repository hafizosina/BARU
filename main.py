import pandas as pd
import numpy as np
import re
from tabulate import tabulate

def openQr(namafile):
	with open(namafile, "r") as f:
			datamentah = []
			datatable = []
			newIndex = 0
			noMerchant = 0
			Tanggal = 0
			for i, line in enumerate(f):
				line = line.rstrip()
				if len(line) > 0 and line[0] == "1": newIndex = i
				if len(line) > 0 and line[0] == " ": line = line[1:]

				# data = [line]
				if i>=newIndex and i<=newIndex+9:
					data = re.split(r'\s{2,}', line)
					if i==newIndex+1: 
						noMerchant = data[0]
						noMerchant = noMerchant.split()[0]
					if i==newIndex+2: 
						# print(data)
						namaCabang = data[0]
					if i==newIndex+8:
						Tanggal_ = data[0]
						Tanggal_ = Tanggal_.split()[3]
						
				else:
					data = re.split(r'\s{1,}', line)
					# if len(data) == 10 and len(line)>81:
					# 	data.insert(1," ")
				



				# print(data)
				
				datamentah.append(data)
				if len(data)>=10 and len(line)>81 and data[1]!="BATCH":
					data = [line[0:6], line[6:7], line[9:13],line[14:17], line[18:22], line[23:31], line[33:38], line[39:58], line[59:60], line[61:72], line[72:73], line[78:84], line[85:86], line[87:96]]
					#print(data)
					data.append(noMerchant)
					data.append(namaCabang)
					data.append(Tanggal_)
					datatable.append(data)
					# print(data)
		
			return pd.DataFrame(datatable)




def openData(namafile):
	with open(namafile, "r") as f:
		datamentah = []
		datatable = []
		newIndex = 0
		noMerchant = 0
		for i, line in enumerate(f):
			line = line.rstrip()
			if len(line) > 0 and line[0] == "1": newIndex = i
			if len(line) > 0 and line[0] == " ": line = line[1:]

			# data = [line]
			if i>=newIndex and i<=newIndex+9:
				data = re.split(r'\s{2,}', line)
				if i==newIndex+1: 

					noMerchant = data[0]
					noMerchant = noMerchant.split()[0]
					# print(noMerchant)
				if i==newIndex+2: 
					namaCabang = data[0]
			else:
				data = re.split(r'\s{1,}', line)
				# if len(data) == 10 and len(line)>81:
				# 	data.insert(1," ")

			# print(data)
			
			datamentah.append(data)
			if len(data)>=10 and len(line)>81 and data[1]!="BATCH":
				# DISINI JUGA ADA PERUNAHAN POSISI PENOMORAN
				data = [line[1:5], line[6:7], line[8:13],line[14:17], line[18:22], line[23:31], line[32:38], line[39:58], line[59:60], line[61:72], line[73:74], line[75:83], line[84:96]]
				# print(data)
				data.append(noMerchant)
				data.append(namaCabang)
				datatable.append(data)
		return pd.DataFrame(datatable)

# this opening technic, using fixed width file form pandas
def qr(namafile, namaout):
	print("Open File")
	# data= openData(namafile)
	data= openQr(namafile)

	df1 = pd.DataFrame(data)
	df1.iloc[:,7].replace("-","", regex=True, inplace=True)
	df1.iloc[:,9].replace(",","", regex=True, inplace=True)
	df1.iloc[:,9].replace(",","", regex=True, inplace=True)
	df1.iloc[:,9].replace(",","", regex=True, inplace=True)
	df1.iloc[:,9].replace(",","", regex=True, inplace=True)
	#  Ini order header dari file mentah
	columns = ["0O-BATCH","IDK" , "BATCH", "SEQ", "TYPE", "TXN-DATE", "AUTH", "CARD_NUMBER", "EH", "AMOUNT", "OP", "RATE", "OH", "DISC.AMT", "No_Merchant", "Nama_Cabang", "Tanggal_"]
	#  Ini order header yang diatur
	df1.columns = columns
	df1["AMOUNT"] = df1["AMOUNT"].astype(int)


	# dfOut = pd.DataFrame.empty()
	kumpulanData = []
	listmID = ["000000318",]
	for mID in listmID:
		kumpulanData.extend(df1[df1['No_Merchant'] == mID].values.tolist())
	print(kumpulanData)
	dfOut = pd.DataFrame(kumpulanData)
	dfOut.columns = columns

	# dfOut = pd.DataFrame(kumpulanData)
	# print(dfOut)





	print()
	print("Save Data to Excel ...")
	print("Please Wait. this might take a cup of tea  :D")

	# to_fwf(dfOut,namaout)
	dfOut.to_excel("hasil.xlsx", index=False, header=True)
	# df1.to_fwf("hasil.txt", index=False, header=True)
	print()
	print("Done !")


#############################################################################################
#	Program untuk XD
#############################################################################################



def to_fwf(df, fname):
	# print(df.columns.tolist())
	headers = df.columns.tolist()
	rows = df.values.tolist()
	#data = [, , , , , , , , , , , , , line[87:96]]
	formatHeader = " {:<6} {:<1} {:4} {:<3} {:4} {:<11} {:<6} {:<19} {:<1} {:<11} {:<1} {:6} {:<1} {:<18} {:<9} {:<15} {:<8}"
	template = " {:<6} {:<1} {:4} {:<3} {:4} {:<11} {:<6} {:<19} {:<1} {:<11} {:<1} {:6} {:<1} {:<18} {:<9} {:<15} {:<8}"
	data = '\n'.join([template.format(*row) for row in rows])
	header = formatHeader.format(*headers)
	print(header)
	data = header + data
	open(fname, "w").write(data)


if __name__ == '__main__':
	
	qr("coba.txt", "Hasil.txt")
	#xd("CP8055.txt", "Hasil.xlsx")
