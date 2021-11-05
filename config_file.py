# Moving from User Equipment to gNB
s_path1 = r'F:\Testcases\Locker\UE'
d_path1 = r'F:\Testcases\Locker\gNB'

# Moving from gNB TO User Equipment
s_path2 = r'F:\Testcases\Locker\gNB'
d_path2 = r'F:\Testcases\Locker\UE'

# Validating paths
path1 = r'F:\Testcases\Locker\gNB\Request.txt'
path2 = r'F:\Testcases\Locker\UE\Response.txt'
path3 = r'F:\Testcases\Locker\UE\PDU SESSION ESTABLISHMENT REQUEST.txt'
path4 = r'F:\Testcases\Locker\5GC\SMF'
path5 = r'F:\Testcases\Locker\5GC\SMF\PDU SESSION ESTABLISHMENT ACCEPT.txt'
path6 = r'F:\Testcases\Locker\UE'
path7 = r'F:\Testcases\Locker\5GC\SC\SC_msg.txt'
path8 = r'F:\Testcases\Locker\5GC\SMSGMSC'
path9 = r'F:\Testcases\Locker\5GC\SMSGMSC\GMSC_rout_request.txt'
path10 = r'F:\Testcases\Locker\5GC\UDM'
path11 = r'F:\Testcases\Locker\5GC\UDM\UDM_rout_response.txt'
path12 = r'F:\Testcases\Locker\5GC\SMSGMSC'
path13 = r'F:\Testcases\Locker\5GC\SMSGMSC\GMSC_msg1.txt'
path14 = r'F:\Testcases\Locker\5GC\SMSF'
path15 = r'F:\Testcases\Locker\5GC\SMSF\SMSF_msg1.txt'
path16 = r'F:\Testcases\Locker\5GC\AMF'
path17 = r'F:\Testcases\Locker\5GC\AMF\AMF_msg1.txt'
path18 = r'F:\Testcases\Locker\5GC\SMSF'
path19 = r'F:\Testcases\Locker\5GC\SMSF\SMSF_msg2.txt'
path20 = r'F:\Testcases\Locker\5GC\AMF'
path21 = r'F:\Testcases\Locker\5GC\AMF\AMF_msg2.txt'
path22 = r'F:\Testcases\Locker\UE'
path23 = r'F:\Testcases\Locker\UE\UE_msg.txt'
path24 = r'F:\Testcases\Locker\5GC\AMF'
path25 = r'F:\Testcases\Locker\5GC\AMF\AMF_msg3.txt'
path26 = r'F:\Testcases\Locker\5GC\SMSF'
path27 = r'F:\Testcases\Locker\UE\UE_msg1.txt'
path28 = r'F:\Testcases\Locker\5GC\AMF'
path29 = r'F:\Testcases\Locker\5GC\AMF\AMF_msg4.txt'
path30 = r'F:\Testcases\Locker\5GC\SMSF'
path31 = r'F:\Testcases\Locker\5GC\SMSF\SMSF_msg3.txt'
path32 = r'F:\Testcases\Locker\5GC\SC'
path33 = r'F:\Testcases\Locker\5GC\SMSF\SMSF_msg4.txt'
path34 = r'F:\Testcases\Locker\5GC\AMF'
path35 = r'F:\Testcases\Locker\5GC\AMF\AMF_msg5.txt'
path36 = r'F:\Testcases\Locker\UE'
path37 = r'F:\Testcases\Locker\gNB\RRC_Report.txt'
path38 = r'F:\Testcases\Locker\UE'
path39 = r'F:\Testcases\Locker\gNB\RRC_Report1.txt'
path40 = r'F:\Testcases\Locker\UE'
path41 = r'F:\Testcases\Locker\gNB\RRC_Report2.txt'
path42 = r'F:\Testcases\Locker\UE'
path43 = r'F:\Testcases\Locker\gNB\RRC_Report3.txt'
path44 = r'F:\Testcases\Locker\UE'
#Messages
msg1 = "Random Access Preamble Transmission (Msg1)"
msg2 = "Random Access Response (MSG2) Report"
msg3 = "UE Identification Message (MSG3) Report"
msg4 = "Contention Resolution Message (MSG4) Report"

#Filenames
file1 = 'Request.txt'
file2 = 'Response.txt'

#Passwords for locking and unlocking
pw = 'abhishek'
pw1 = str(input("Enter your password for unlocking: "))
pw2 = str(input("Enter the password for locking:"))
dir_path = r"F:\Testcases"
Loc = 'Locker'

# Serving Cell Specifications
Qrxlevmeas = -102.38    #Measured Cell RX level value(RSRP)
Qrxlevmin = -110     #Minimum Required RX level in the cell(dBm)
Qrxlevminoffset = 0   #offset to the signalled Qrxlevmin taken into account in the Srxlev evaluation as a result of periodic search for higher priority PLMN.
Qqualmeas = -8.75  # Measured cell quality value ( RSRQ)
Qqualmin = -34   #Minimum required quality level in the cell(dB)
Qqualminoffset = 0   ##offset to the signalled Qqualmin taken into account in the Squal evaluation as a result of periodic search for higher priority PLMN.
PeMax= 23   #Max Tx power level an UE may use when transmitting on the uplink in the cell(dBm)
PpowerClass = 23  #Max RF output power of the UE(dBm) according to the UE power class
Pcompensation = 0 # max(PeMax - PpowerClass, 0 ) dB

# Intra Cell Specifications
Qrxlevmeas1 = float(input('Enter the RSRP Value of intra cell in dBm (preferred between -156 to -31'))
Qrxlevmin1 = -110
Qrxlevminoffset1 = 0
Qqualmeas1 = float(input('Enter the RSRQ Value of intra cell in dBm'))
Qqualmin1 = -34
Qqualminoffset1 = 0

# Handover Specifications ( all values are in milliseconds)
Td_required = float(input('CASE-1.31: Enter the transmission time (in milliseconds) of UE required for new uplink PRACH channel'))
Td_rrc = 10                  # Maximum RRC Procedure delay in milliseconds
k = 20                       # additional constant defined as per 3gpp 15 release
T_rs = 5                     # in ms
Td_delta = 5                 # it is equal to Trs = 5 ms for unknown configurations (i.e not knowing about SSB or SMTC configurations)
x = 4                        # assuming FR1 > 3 GHz PS Cell carrier frequency(case of FR1)
x1 = 8                       # case of FR2
Td_iu = (x * 10) + 10        # interruption uncertainty
Td_iu1 = (x1 * 10) + 10
Td_search = (T_rs + 2)       # time required to search the target cell when it is not already known ( taking intra cell case)

Td_required1 = float(input('CASE-1.32: Enter the transmission time (in milliseconds) of UE required for new uplink PRACH channel'))
k1 = 40
Td_search1 = ((3*T_rs) + 2)  # taking inter cell case

Td_required2 = float(input('CASE-1.33: Enter the transmission time (in milliseconds) of UE required for new uplink PRACH channel'))
Td_processing = 15       # can be upto 20 ms
Td_search2 = ((8*T_rs) + 2)  # taking intra cell case

Td_required3 = float(input('CASE-1.34: Enter the transmission time (in milliseconds) of UE required for new uplink PRACH channel'))
Td_processing1 = 15       # can be upto 20 ms
Td_search3 = ((8*3*T_rs) + 2)  # taking inter cell case

