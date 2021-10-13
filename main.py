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
		
			return pd.DataFrame(datatable)

# this opening technic, using fixed width file form pandas
def qr(namafile, namaout):
	print("Open File")
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
	df1["AMOUNT"] = df1['AMOUNT'].astype(int)

	#temp = (df1.iloc[:,8]).str.contains('PYM TELKOMSEL|PYM INDOSAT|PYM TELKOM|PYM SMARTFREN|PYM XPLOR|BILL MNCVISION|AETRA AIR|FIRST MEDIA|PYM PLN|PYM JKNKIS|BILL INDOSAT M2|DONASI KAFEGAMA|OTO SMART TELECOM|SMART MOBILE 8|PERISAI PLUS|MEDCARE|FUTURE PLAN|KIDS CARE|PERSONAL SHIELD|FAMILY CARE|JAMINAN BELANJA|DREAD DISEASE|EARLY PROTECTION|FAMILY PROTECTION|CRITICAL PROTECTION|HEALTHYDENT|HEALTYLIFE|FAMILY GUARD|PRIMARY|FAM.HEALT|PERSONAL SHIELD|FAMILY HEALTH CARE+|KIDS HEALTH CARE|JAMINAN BELANJA|DREAD DISEASE|SMART TRAVELLER|MULTI PROTECTION|PERLINDUNGAN ABSOLUT|ALLISYA PROTEKSIKU|ALLISYA KESEHATANKU|SOLUSI PRESTASI|SIMPONI|HOSPITAL INCOME|PERDANA|PRECIOUS CARE|MEDIKA DANA|PROTEKSI JUNIOR|ULTIMATE PROTECTION|TRIP PLUS|HOSPITAL CARE|HEALTH & FUND|PROTEKSI PRIMA|PA PROTECTION|ACTIVE PLUS|SAFE MEDICAL|MAXI HEALTH PROTECT|SMART GUARD|CAR SAFE|DENTAL INSURANCE|DIGITAL PROTECTION|RENCANA EXTRA|ACADEMY CASH|SAFETY LIFE|AXA LIFE IND|BENGKEL CROSSFIT|BHINNEKA|BNI LIFE|CBN-RECURRING|CIGNA|PLAN INTERNATIONAL|EQUITY LIFE|GENERALI|PERKUMPULAN ICW|JAGADIRI|ASURANSI JIWASRAYA|LBH JAKARTA|EMPIRE FIT|NEOFITNESS|QALISTAHUMANCARE|RUMAH YATIM|AJSMSIG|SAVETHECHILDREN-REC|THALASSAEMIA|YKAN|URBAN FITNESS|DONASI WALHI|WINETMEDIA|WWF INDONESIA|YKAKI|RUMAH1HATI|ALODOKTER|TRACASTRA|IKIGAI|FITNESS-REC|TELE TRAVEL|NCB|REFUND|KOR|KLAIMPERLINDUNGAN ABS|ALLISYA KESEHATA|ALLISYA PROTEKSIKU|MULTI PROTECTION|SIMPONI|ACTIVE PLUS|ACTIVE PLUS FT|SAFE MEDICAL PLAN|SAFEMEDICALPLAN FT|FUTURE PLAN|MAXI HEALTH PROTEC|MAXIHEALTHPROTECTFT|ASURANSI MEDCARE PLUS|PA PROTECT PLUS FT|PA PROTECTION PLUS|PERISAI PLUS|PERISAI PLUS|PROTEKSI PRIMA|PROTEKSI PRIMA FT|KOR PAP|PROTEKSI Pr|HOSPITAL INCOME|PERDANA|PRECIOUS CARE|MEDIKA DANA|PROTEKSI JUNIOR|ULTIMATE PROTECTION|TRIP PLUS|HOSPITAL CARE|HEALTH & FUND|SMART GUARD INS|CAR SAFE INS|DENTAL INSURANCE P|DIGITAL PROTEC|DENTAL INS PLAN F|CRITICAL PROTE|DREAD DISEASE SHIE|BNI FAMILY GUARD|ASURANSI FAM.HEALT|FAMILY HEALTH CAR|FAMILY PROTECTION|HEALTHYDENT|HEALTHYLIFE|JAMINAN BELANJA X|KIDS HEALTH CARE|PERSONAL SHIELD|PERSONAL SHIELD XT|ASURANSI PRIMARY C|SOLUSI PRESTASI\DREAD DISEASE PLUS|EARLY PROTECTION P|FAMILY CARE PLUS|HEALTHY EXTRA PLUS|JAMINAN BELANJA PL|KIDS CARE PLUS|PERSONAL SHIELD PL|SMART TRAVELLER PL|SMARTTRAVELLER+FT|ACADEMY CASH|ACADEMY CASH FT|ACADEMY CASH|PERISAI PLUS|RENCANA EXTRA DINI|RENCANAEXTRADINIFT|SAFETY LIFE|SAFETY LIFE FT|ACADEMY CASH|REN EXT D|ACADEMY CASH|ACADEMY CASH FT|ACADEMY CASH|PERISAI PLUS|RENCANA EXTRA DINI|RENCANAEXTRADINIFT|SAFETY LIFE|SAFETY LIFE FT|BILL PYM JKNKIS|BILL PYM INDOSAT|BILL INDOSAT M2|DONASI KAFEGAMA|BILL FIRST MEDIA|BILL MNCVISION|BILL PYM PLN|KORBILLPL|BILL PYM SMARTFREN|SMART MOBILE 8|OTO SMART TELECOM|BILL PYM TELKOM|BILL AETRA AIR|BILL PYM XPLOR|BILL PYM TELKOMSEL')
	#temp = (df1.iloc[:,8]).str.contains('DREAD|SMARTT|SMART TR|MEDCARE|DENTAL INS|PERLINDUNGAN ABS|ALLISYA KESEHATA|ALLISYA PROTEKSIKU|MULTI PROTECTION|SIMPONI|ACTIVE PLUS|ACTIVE PLUS FT|SAFE MEDICAL PLAN|SAFEMEDICALPLAN FT|FUTURE PLAN|MAXI HEALTH PROTEC|MAXIHEALTHPROTECTFT|ASURANSI MEDCARE PLUS|PA PROTECT PLUS FT|PA PROTECTION PLUS|PERISAI PLUS|PERISAI PLUS|PROTEKSI PRIMA|PROTEKSI PRIMA FT|KOR PAP|PROTEKSI Pr|HOSPITAL INCOME|PERDANA|PRECIOUS CARE|MEDIKA DANA|PROTEKSI JUNIOR|ULTIMATE PROTECTION|TRIP PLUS|HOSPITAL CARE|HEALTH & FUND|SMART GUARD INS|CAR SAFE INS|DENTAL INSURANCE P|DIGITAL PROTEC|DENTAL INS PLAN F|CRITICAL PROTE|DREAD DISEASE SHIE|BNI FAMILY GUARD|ASURANSI FAM.HEALT|FAMILY HEALTH CAR|FAMILY PROTECTION|HEALTHYDENT|HEALTHYLIFE|JAMINAN BELANJA X|KIDS HEALTH CARE|PERSONAL SHIELD|PERSONAL SHIELD XT|ASURANSI PRIMARY C|SOLUSI PRESTASI\DREAD DISEASE PLUS|EARLY PROTECTION P|FAMILY CARE PLUS|HEALTHY EXTRA PLUS|JAMINAN BELANJA PL|KIDS CARE PLUS|PERSONAL SHIELD PL|SMART TRAVELLER PL|SMARTTRAVELLER+FT|ACADEMY CASH|ACADEMY CASH FT|ACADEMY CASH|PERISAI PLUS|RENCANA EXTRA DINI|RENCANAEXTRADINIFT|SAFETY LIFE|SAFETY LIFE FT|ACADEMY CASH|REN EXT D|ACADEMY CASH|ACADEMY CASH FT|ACADEMY CASH|PERISAI PLUS|RENCANA EXTRA DINI|RENCANAEXTRADINIFT|SAFETY LIFE|SAFETY LIFE FT|BILL PYM JKNKIS|BILL PYM INDOSAT|BILL INDOSAT M2|DONASI KAFEGAMA|BILL FIRST MEDIA|BILL MNCVISION|BILL PYM PLN|KORBILLPL|BILL PYM SMARTFREN|SMART MOBILE 8|OTO SMART TELECOM|BILL PYM TELKOM|BILL AETRA AIR|BILL PYM XPLOR|BILL PYM TELKOMSEL')
	
	
	#df1True=(df1.iloc[:,14])str.contains('710000647|710000266|014000095|710000795|710000803|710000332|710000886|710000829|710000894|014000160|014000053|710000241|710000118|715000097|715000022|710000092|702000027|714000072|014000061|715000071|710000068|710000415|710000423|710000993|706000023|014000012|710000514|710000324|715000048|715000196|710001223|715000212|714000163')
	#temp = (df1.iloc[:,14]).str.contains('710000647|710000266| 014000095| 710000795| 710000803| 710000332| 710000886| 710000829| 710000894| 014000160| 014000053| 710000241| 710000118| 715000097| 715000022| 710000092| 702000027| 714000072| 014000061| 715000071| 710000068| 710000415| 710000423| 710000993| 706000023| 014000012| 710000514| 710000324| 715000048| 715000196| 710001223| 715000212| 714000163')
	##temp = (df1.iloc[:,8]).str.contains('ADJUST|BIAYA|BY|CB|CHARGE|CR|CREDIT|GRATIS|HAPUS|HPS|KOR|NCB|PEMBEBASAN|PENYELESAIAN|REDEBET|REFUND|SLD')
	#dfA=df[df[""].str.contains("Base-24")]
	#temp = df1['Transaction_Description'].str.contains('TELKOMSEL|INDOSAT|TELKOM|SMARTFREN|XPLOR|MNCVISION|AETRA AIR|FIRST MEDIA|PLN|JKNKIS|INDOSAT M2|DONASI KAFEGAMA|OTO SMART TELECOM|SMART MOBILE 8|ASURANSI MEDCARE PLUS|FUTURE PLAN|HEALTHY EXTRA PLUS|KIDS CARE PLUS|PERSONAL SHIELD PL|FAMILY CARE PLUS|JAMINAN BELANJA PL|DREAD DISEASE PLUS|EARLY PROTECTION P|FAMILY PROTECTION|CRITICAL PROTECTION|HEALTHYDENT|BNI FAMILY GUARD|ASURANSI PRIMARY C|ASURANSI FAM.HEALT|PERSONAL SHIELD|PERSONAL SHIELD XT|FAMILY HEALTH CARE+|KIDS HEALTH CARE|JAMINAN BELANJA X-|DREAD DISEASE SHIE|SMART TRAVELLER PLUS|MULTI PROTECTION|PERLINDUNGAN ABSOLUT|ALLISYA PROTEKSIKU|ALLISYA KESEHATANKU|SOLUSI PRESTASI|SIMPONI|HOSPITAL INCOME|PERDANA|PRECIOUS CARE|MEDIKA DANA|PROTEKSI JUNIOR|ULTIMATE PROTECTION|TRIP PLUS|HOSPITAL CARE|HEALTH & FUND|PROTEKSI PRIMA|PA PROTECTION PLUS|ACTIVE PLUS|SAFE MEDICAL PLAN|MAXI HEALTH PROTECT|SMART GUARD INSURANCE|CAR SAFE INSURANCE|DENTAL INSURANCE PLAN|DIGITAL PROTECTION|RENCANA EXTRA DINI|ACADEMY CASH|SAFETY LIFE|AXA LIFE  IND-REC|BENGKEL CROSSFIT-REC|BHINNEKALIFE LINK-REC|BHINNEKALIFE KONVEN-REC|BNI LIFE-REC|BNI LIFE PA|CBN-RECURRING|CIGNA|PLAN INTERNATIONAL-REC|EQUITY LIFE-REC|GENERALI|PERKUMPULAN ICW - REC|JAGADIRI-REC|ASURANSI JIWASRAYA - REC|LBH JAKARTA-REC|EMPIRE FIT CLUB-REC|NEO FITNESS-REC|QALISTAHUMANCARE-REC|RUMAH YATIM IND-REC|AJSMSIG-RECURRING|SAVETHECHILDREN-REC|THALASSAEMIA IND-REC|YKAN-REC|YKAN-REC2 OTHERS|URBAN FITNESS-REC|DONASI-WALHI|WINETMEDIA-REC|WWF INDONESIA-REC|YKAKI-REC|RUMAH1HATI-REC|ALODOKTER-REC|TRACASTRA-REC|IKIGAI FITNESS-REC|TELE TRAVEL|NCB|REFUND|KOR|KLAIM')
	#df1True = df1.loc[temp,:]
	#df1['A']= ""
	#df1['A']= df1['Transaction_Description'].str.contains('TELKOMSEL|INDOSAT|TELKOM|SMARTFREN|XPLOR|MNCVISION|AETRA AIR|FIRST MEDIA|PLN|JKNKIS|INDOSAT M2|DONASI KAFEGAMA|OTO SMART TELECOM|SMART MOBILE 8|ASURANSI MEDCARE PLUS|FUTURE PLAN|HEALTHY EXTRA PLUS|KIDS CARE PLUS|PERSONAL SHIELD PL|FAMILY CARE PLUS|JAMINAN BELANJA PL|DREAD DISEASE PLUS|EARLY PROTECTION P|FAMILY PROTECTION|CRITICAL PROTECTION|HEALTHYDENT|BNI FAMILY GUARD|ASURANSI PRIMARY C|ASURANSI FAM.HEALT|PERSONAL SHIELD|PERSONAL SHIELD XT|FAMILY HEALTH CARE+|KIDS HEALTH CARE|JAMINAN BELANJA X-|DREAD DISEASE SHIE|SMART TRAVELLER PLUS|MULTI PROTECTION|PERLINDUNGAN ABSOLUT|ALLISYA PROTEKSIKU|ALLISYA KESEHATANKU|SOLUSI PRESTASI|SIMPONI|HOSPITAL INCOME|PERDANA|PRECIOUS CARE|MEDIKA DANA|PROTEKSI JUNIOR|ULTIMATE PROTECTION|TRIP PLUS|HOSPITAL CARE|HEALTH & FUND|PROTEKSI PRIMA|PA PROTECTION PLUS|ACTIVE PLUS|SAFE MEDICAL PLAN|MAXI HEALTH PROTECT|SMART GUARD INSURANCE|CAR SAFE INSURANCE|DENTAL INSURANCE PLAN|DIGITAL PROTECTION|RENCANA EXTRA DINI|ACADEMY CASH|SAFETY LIFE|AXA LIFE  IND-REC|BENGKEL CROSSFIT-REC|BHINNEKALIFE LINK-REC|BHINNEKALIFE KONVEN-REC|BNI LIFE-REC|BNI LIFE PA|CBN-RECURRING|CIGNA|PLAN INTERNATIONAL-REC|EQUITY LIFE-REC|GENERALI|PERKUMPULAN ICW - REC|JAGADIRI-REC|ASURANSI JIWASRAYA - REC|LBH JAKARTA-REC|EMPIRE FIT CLUB-REC|NEO FITNESS-REC|QALISTAHUMANCARE-REC|RUMAH YATIM IND-REC|AJSMSIG-RECURRING|SAVETHECHILDREN-REC|THALASSAEMIA IND-REC|YKAN-REC|YKAN-REC2 OTHERS|URBAN FITNESS-REC|DONASI-WALHI|WINETMEDIA-REC|WWF INDONESIA-REC|YKAKI-REC|RUMAH1HATI-REC|ALODOKTER-REC|TRACASTRA-REC|IKIGAI FITNESS-REC|TELE TRAVEL|NCB|REFUND|KOR|KLAIM')
	#df1["Terminal_ID"] = df1["Terminal_ID"].astype(str)
	#df1["Issuer"] = df1["Issuer"].astype(str)
	#df1["SW_ISSUER"] = df1["SW_ISSUER"].astype(str)
	#df1["Nominal"].replace(",","", regex=True, inplace=True)
	#df1["Nominal"].replace(".","", regex=True, inplace=True)
	#df1["Nominal"] = df1['Nominal'].astype(str)
	#df1["Nominal"] = df1['Nominal'].astype(int)
	#df1["Tanggal_Trx"] = pd.to_datetime(df1["Tanggal_Trx"])
	#df1["Tanggal_Trx"] = df1["Tanggal_Trx"].dt.strftime('%m/%d/%Y')

	#df1["No."] = df1["No."].astype(str)

	#df1['KETERANGAN']=""

	#newcol = ["Account_Number", "Last_Tran", "Transaction_Date", "Transaction_Code", "Amount", "Reference_Number", "SRC_CDE", "P_B", "Transaction_Description", "R_A", "Interchange_Ref_Number", "A"]
	#df1= df1.reindex(columns= newcol)


	#df1.to_csv("qrcsv.txt", header=False)

	print()
	print("Save Data to Excel ...")
	print("Please Wait. this might take a cup of tea  :D")

	# namafileOutput = "qrHasil.xlsx"
	#df1outcut=pd.DataFrame(df1True)

	to_fwf(df1,namaout)

	#np.savetxt("hasil.txt", df1outcut, )
	#df1outcut.to_excel(excelout, index=False, header=True)
	#df1outcut.to_csv("hasil.txt", index=False, header=True)
	print()
	print("Done !")


#############################################################################################
#	Program untuk XD
#############################################################################################



def to_fwf(df, fname):
	rows = df.values.tolist()
	#data = [, , , , , , , , , , , , , line[87:96]]
	template = " {:<6} {:<1} {:4} {:<3} {:4} {:<11} {:<6} {:<19} {:<1} {:<11} {:<1} {:6} {:<1} {:<18}"
	data = '\n'.join([template.format(*row) for row in rows])
	data = "\n" + data
	open(fname, "w").write(data)


if __name__ == '__main__':
	
	qr("BND350250821.txt", "Hasil.txt")
	#xd("CP8055.txt", "Hasil.xlsx")
