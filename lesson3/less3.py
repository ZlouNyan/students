# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 09:28:15 2021

@author: kuzma.m
"""

import pyvisa as visa 
import time



# ����������� � SNVNA
rm = visa.ResourceManager()
rm = visa.ResourceManager('@py')
#Connect to a Socket on the local machine at 5025
#Use the IP address of a remote machine to connect to it instead
try:
    CMT = rm.open_resource('TCPIP0::localhost::5025::SOCKET')
except:
    print("Failure to connect to VNA!")
    print("Check network settings")

#The VNA ends each line with this. Reads will time out without this
CMT.read_termination='\n'
#Set a really long timeout period for slow sweeps
CMT.timeout = 100000
##############################################

#�������� ������ � �����
CMT.write(f'CALC1:PAR:COUN 2')
time.sleep(1)

#��������� ����������� ��������� S11 �� ������� 2 �� S22
CMT.write(f'CALC:PAR2:DEF S22')
time.sleep(1)

#�������� ������ �� ������
CMT.write(f'CALC:MARK1:ACT')

CMT.write(f'CALC:MARK2:ACT')
time.sleep(1)

#�������� ������� ������� �� ��� ������� ���
CMT.write(f'CALC:MARK1:X 3000000000') #3 ����

CMT.write(f'CALC:MARK2:X 3500000000') #3,5 ����
time.sleep(1)

#�������� �������� ���� ��� ����
marker_check = CMT.query('CALC:MARK?')
if marker_check: CMT.write(f'CALC:MARK OFF')
time.sleep(1)

#�������� �������
CMT.write(f'CALC1:PAR:COUN 1')

#��� ���� ��������� ������� �� lesson2

#������� 16 ����� � �����
CMT.write(f'CALC:PAR:COUN 16')
trace_count = CMT.query('CALC:PAR:COUN?')
print('����� ��������: ', trace_count)

#�������� ������ � ���� 1 ������ s11, 2 ������ s22...16 ������ s1616
#count = 1
#while count <= trace_count:
   # CMT.write(f'CALC:PAR2:DEF S{c}')
   # count += 1
#�� ������ ������ �������� 2 ������� 1 GHz � 5.5 GHz

#������ ������ ������ �������� � ���� S ����� ������ (����� ������-1)

#������� � ������� ��� ������
#������ 
#������ �1 = s11
