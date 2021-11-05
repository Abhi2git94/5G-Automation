*** Settings ***
# Documentation     This is first test script
Library     os
Resource     ${EXEC_DIR}/Res/attach_keyword.robot
Variables    ${EXEC_DIR}/VariableFiles/config_file.py
Library      ${EXEC_DIR}/Lib/attach_test.py



*** Test Cases ***
Test_cases
     Unlocking
     Moving1
     Moving2
     Validation
     CellReselection
     RRCREJECT3
     MTSMS3
     Locking

Test_case_handover
     FR1toFR1
     FR2toFR1
     FR2toFR2
     FR1toFR2

*** Keywords ***

Moving1
    moving_UE
Moving2
    Moving_gNB
Validation
    UE_validation
    Response_gNB_Validation

Unlocking
    unlock
Locking
    lock

CellReselection
    Reselection_intracell

RRCREJECT3
    RRC_Reject

MTSMS3
    MT_SMS

FR1toFR1
    handover_FR1toFR1
FR2toFR1
    handover_FR2toFR1
FR2toFR2
    handover_FR2toFR2
FR1toFR2
    handover_FR1toFR2






