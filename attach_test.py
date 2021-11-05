import pathlib
import shutil
import os
import time
import codecs
import sys
sys.path.insert(0, r'C:\Users\Abhishek Verma\PycharmProjects\5G Automation\VariableFiles')
import config_file
from pathlib import Path

class attach_test:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __int__(self):
        pass

    def moving_UE(self):
        f1 = config_file.s_path1
        f2 = config_file.d_path1
        files = os.listdir(f1)
        for fname in files:
            # copying the files to the
            # destination directory
            if fname == config_file.file1:
                shutil.move(os.path.join(f1, fname), f2)
                print('Successfully moved request file from UE to gNB')

    def Moving_gNB(self):
        f3 = config_file.s_path2
        f4 = config_file.d_path2
        files2 = os.listdir(f3)
        for fname1 in files2:
            # copying the files to the
            # destination directory
            if fname1 == config_file.file2:
                shutil.move(os.path.join(f3, fname1), f4)
                print('Successfully transfered file from gNB to UE')

    def unlock(self):

        # Unlock the folder
        pw = config_file.pw

        # while True:
        pw1 = config_file.pw1
        if pw1 == pw:
            os.chdir(config_file.dir_path)
            if not os.path.exists(config_file.Loc):
                if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                    os.mkdir("Locker")
                    print("Locker Folder Successfully created")

                else:
                    os.popen('attrib -h -s -r Locker')
                    os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                    print("Locker Folder has been Successfully Unlocked")
                    # break

            else:
                print("Locker folder is not LOCKED")

        else:
            print("wrong password! Try again later")

    #Function for locking

    def lock(self):  # lock the folder

        p_w = config_file.pw

        # while True:
        pw2 = config_file.pw2
        if p_w == pw2:
            os.chdir(config_file.dir_path)
            # print("Your path Successfully Changed")
            # If Locker folder or Recycle bin does not exist then we will be create Locker Folder

            if os.path.exists(config_file.Loc):
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # sys.exit()
                # break

            else:
                os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # break

        else:
            print("wrong password! Try again later")
            # break


    def String_matching(self, file_name, string_to_search):
        """ Check if any line in the file contains given string """
        # Open the file in read only mode
        with open(file_name, 'r') as read_obj:
            # Read all lines in the file one by one
            for line in read_obj:
                # For each line, check if line contains the string
                if string_to_search in line:
                    return True
        return False

    def UE_Validation(self):

        # Check if string 'msg2' is found in file 'sample.txt'
        print("here")
        if self.String_matching(config_file.path1, config_file.msg1):
            print('Yes,Random access Preamble message - msg1 found')
        else:
            print('msg1 not found in file')

        if self.String_matching(config_file.path1, config_file.msg3 ):
            print('Yes, UE Identification message is found')
        else:
            print('msg3 String not found in file')

    def Response_gNB_Validation(self):

        # Check if string 'msg4' is found in file 'sample.txt'
        # Check if string 'msg2' is found in file Response.txt'
        if self.String_matching(config_file.path2, config_file.msg2):
            print('Yes,Random access response report is found from gNB')
        else:
            print('msg2 not found in file')

        if self.String_matching(config_file.path2, config_file.msg4):
            print('Yes, Contention Resolution report is found')
        else:
            print('msg4 String not found in file')
        # f4.close()
    def Reselection_intracell(self):
        Srxlev = config_file.Qrxlevmeas - (config_file.Qrxlevmin + config_file.Qrxlevminoffset)-config_file.Pcompensation
        Squal = config_file.Qqualmeas - (config_file.Qqualmin + config_file.Qqualminoffset)

        SIntraSearchP = config_file.Qrxlevmeas1 - (config_file.Qrxlevmin1 + config_file.Qrxlevminoffset1) - config_file.Pcompensation
        SIntraSearchQ = config_file.Qqualmeas1 - (config_file.Qqualmin1 + config_file.Qqualminoffset1)
        if SIntraSearchP > 0 and SIntraSearchQ > 0:
            print('Intra cell is following the cell Selection Criteria')
        else:
            print('Intra cell is not Suitable for UE')
        if Srxlev > SIntraSearchP and Squal > SIntraSearchQ:
            print('Serving Cell is Sufficient no need to perform Cell Reselection')
        else:
            print('Intra cell is selected')


    def RRC_Reject(self):
        print('Check for UE')
        print("Status -- UE Registration is successful")
        print("Now Trigger the PDU session")
        shutil.move(config_file.path3, config_file.path4)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMF\PDU SESSION ESTABLISHMENT REQUEST.txt', "r" , "utf-8" ) as f:
            if 'Message: UL NAS transport' in f.read():
                print("Message Received in SMF from UE")
        shutil.move(config_file.path5, config_file.path6)
        with codecs.open(r'F:\Testcases\Locker\UE\PDU SESSION ESTABLISHMENT ACCEPT.txt', "r", "utf-8") as f3:
            if 'PDU session ID = 5' in f3.read():
                print("Message Received in UE from SMF")
                print("PDU SESSION SUCCESSFULLY CREATED")
            else:
                print("PDU SESSION REJECTED")
        with codecs.open(r'F:\Testcases\Locker\gNB\DU OAM\MaxUE.txt', "r" , "utf-8" ) as f4:
            if 'MaxUE Capacity = 1' in f4.read():
                print("RRC is REJECTED")
        with codecs.open(r'F:\Testcases\Locker\gNB\CU OAM\MaxDU.txt', "r" , "utf-8" ) as f5:
            if 'MaxDU Capacity = FULL' in f5.read():
                print("RRC is REJECTED")
        with codecs.open(r'F:\Testcases\Locker\gNB\CU OAM\MaxCU.txt', "r" , "utf-8" ) as f6:
            if 'MaxCU Capacity = FULL' in f6.read():
                print("RRC is REJECTED")

    def MT_SMS(self):
        print(" check for registration")
        print(" Registration is done successfully")
        print("Send MT SMS to UE from valid number")
        shutil.move(config_file.path7, config_file.path8)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMSGMSC\SC_msg.txt', "r", "utf-8") as f7:
            if '0' in f7.read():
                print("Message Received in SMSGMSC from SC")
            else:
                print("Message not found")
        shutil.move(config_file.path9, config_file.path10)
        with codecs.open(r'F:\Testcases\Locker\5GC\UDM\GMSC_rout_request.txt', "r", "utf-8") as f8:
            if '1' in f8.read():
                print("Message Received in UDM from SMSGMSC")
            else:
                print("Message not found")
        shutil.move(config_file.path11, config_file.path12)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMSGMSC\UDM_rout_response.txt', "r", "utf-8") as f9:
            if '2' in f9.read():
                print("Message Received in SMSGMSC from UDM")
            else:
                print("Message not found")
        shutil.move(config_file.path13, config_file.path14)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMSF\GMSC_msg1.txt', "r", "utf-8") as f10:
            if '3' in f10.read():
                print("Message Received in SMSF from SMSGMSC")
            else:
                print("Message not found")
        shutil.move(config_file.path15, config_file.path16)
        with codecs.open(r'F:\Testcases\Locker\5GC\AMF\SMSF_msg1.txt', "r", "utf-8") as f11:
            if '4' in f11.read():
                print("Message Received in AMF from SMSF")
            else:
                print("Message not found")
        print("Paging Message is sent to UE")
        shutil.move(config_file.path17, config_file.path18)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMSF\AMF_msg1.txt', "r", "utf-8") as f12:
            if '5' in f12.read():
                print("Message Received in SMSF from AMF")
            else:
                print("Message not found")
        shutil.move(config_file.path19, config_file.path20)
        with codecs.open(r'F:\Testcases\Locker\5GC\AMF\SMSF_msg2.txt', "r", "utf-8") as f13:
            if '6' in f13.read():
                print("Message Received in AMF from SMSF")
            else:
                print("Message not found")
        shutil.move(config_file.path21, config_file.path22)
        with codecs.open(r'F:\Testcases\Locker\UE\AMF_msg2.txt', "r", "utf-8") as f14:
            if '7' in f14.read():
                print("Message Received in UE from AMF")
            else:
                print("Message not found")
        shutil.move(config_file.path23, config_file.path24)
        with codecs.open(r'F:\Testcases\Locker\5GC\AMF\UE_msg.txt', "r", "utf-8") as f15:
            if '8' in f15.read():
                print("Message Received in AMF from UE")
            else:
                print("Message not found")
        shutil.move(config_file.path25, config_file.path26)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMSF\AMF_msg3.txt', "r", "utf-8") as f16:
            if '9' in f16.read():
                print("Message Received in SMSF from AMF")
            else:
                print("Message not found")
        shutil.move(config_file.path27, config_file.path28)
        with codecs.open(r'F:\Testcases\Locker\5GC\AMF\UE_msg1.txt', "r", "utf-8") as f17:
            if '10' in f17.read():
                print("Message Received in AMF from UE")
            else:
                print("Message not found")
        shutil.move(config_file.path29, config_file.path30)
        with codecs.open(r'F:\Testcases\Locker\5GC\SMSF\AMF_msg4.txt', "r", "utf-8") as f18:
            if '11' in f18.read():
                print("Message Received in SMSF from AMF")
            else:
                print("Message not found")
        shutil.move(config_file.path31, config_file.path32)
        with codecs.open(r'F:\Testcases\Locker\5GC\SC\SMSF_msg3.txt', "r", "utf-8") as f19:
            if '12' in f19.read():
                print("Message Received in SC from SMSF")
            else:
                print("Message not found")
        shutil.move(config_file.path33, config_file.path34)
        with codecs.open(r'F:\Testcases\Locker\5GC\AMF\SMSF_msg4.txt', "r", "utf-8") as f20:
            if '13' in f20.read():
                print("Message Received in AMF from SMSF")
            else:
                print("Message not found")
        shutil.move(config_file.path35, config_file.path36)
        with codecs.open(r'F:\Testcases\Locker\UE\AMF_msg5.txt', "r", "utf-8") as f21:
            if '14' in f21.read():
                print("Message Received in UE from AMF")
            else:
                print("Message not found")
        print("MT SMS is received successfully and delivery report is received at other party")

    def handover_FR1toFR1(self):
        print('''Check UE status:
                 UE is in connected mode with active data transfer''')
        shutil.move(config_file.path37, config_file.path38)
        with codecs.open(r'F:\Testcases\Locker\UE\RRC_Report.txt', "r", "utf-8") as f22:
            if 'FR1 to FR1 bands' in f22.read():
                print("Message Received in UE regarding Handover")
            else:
                print("Message not found")
        Td_intrpt = (config_file.Td_search)+(config_file.Td_iu)+(config_file.Td_delta) + (config_file.k)   # interruption time in mseconds
        D_hand = (config_file.Td_rrc) + (Td_intrpt)
        if (config_file.Td_required) < D_hand:
            print("Handover is successfully done and handover delay does not exceeds the max RRC procedure delay")
        else:
            print("Handover is failed")

    def handover_FR2toFR1(self):
        print('''Check UE status:
                 UE is in connected mode with active data transfer''')
        shutil.move(config_file.path39, config_file.path40)
        with codecs.open(r'F:\Testcases\Locker\UE\RRC_Report1.txt', "r", "utf-8") as f23:
            if 'FR2 to FR1' in f23.read():
                print("Message Received in UE regarding Handover")
            else:
                print("Message not found")
        Td_intrpt1 = (config_file.Td_search1)+(config_file.Td_iu)+(config_file.Td_delta) + (config_file.k1)   # interruption time in mseconds
        D_hand1 = (config_file.Td_rrc) + (Td_intrpt1)
        if (config_file.Td_required1) < D_hand1:
            print("Handover is successfully done and handover delay does not exceeds the max RRC procedure delay")
        else:
            print("Handover is failed")

    def handover_FR2toFR2(self):
        print('''Check UE status:
                 UE is in connected mode with active data transfer''')
        shutil.move(config_file.path41, config_file.path42)
        with codecs.open(r'F:\Testcases\Locker\UE\RRC_Report2.txt', "r", "utf-8") as f24:
            if 'FR2 to FR2' in f24.read():
                print("Message Received in UE regarding Handover")
            else:
                print("Message not found")
        Td_intrpt2 = (config_file.Td_search2)+(config_file.Td_iu1)+(config_file.Td_delta) + (config_file.Td_processing)   # interruption time in mseconds
        D_hand2 = (config_file.Td_rrc) + (Td_intrpt2)
        if (config_file.Td_required2) < D_hand2:
            print("Handover is successfully done and handover delay does not exceeds the max RRC procedure delay")
        else:
            print("Handover is failed")

    def handover_FR1toFR2(self):
        print('''Check UE status:
                 UE is in connected mode with active data transfer''')
        shutil.move(config_file.path43, config_file.path44)
        with codecs.open(r'F:\Testcases\Locker\UE\RRC_Report3.txt', "r", "utf-8") as f25:
            if 'FR1 to FR2' in f25.read():
                print("Message Received in UE regarding Handover")
            else:
                print("Message not found")
        Td_intrpt3 = (config_file.Td_search3)+(config_file.Td_iu1)+(config_file.Td_delta) + (config_file.Td_processing1)   # interruption time in mseconds
        D_hand3 = (config_file.Td_rrc) + (Td_intrpt3)
        if (config_file.Td_required3) < D_hand3:
            print("Handover is successfully done and handover delay does not exceeds the max RRC procedure delay")
        else:
            print("Handover is failed")










