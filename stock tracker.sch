EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title "Stock-tracker"
Date "2021-07-21"
Rev ""
Comp ""
Comment1 "Drawn By: Blake Henriques Stephenson"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Switch:SW_Push Btn1
U 1 1 60CC81E0
P 5750 6500
F 0 "Btn1" H 5750 6785 50  0000 C CNN
F 1 "SW_Push" H 5750 6694 50  0000 C CNN
F 2 "" H 5750 6700 50  0001 C CNN
F 3 "~" H 5750 6700 50  0001 C CNN
	1    5750 6500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Btn2
U 1 1 60CC98E0
P 5750 6950
F 0 "Btn2" H 5750 7235 50  0000 C CNN
F 1 "SW_Push" H 5750 7144 50  0000 C CNN
F 2 "" H 5750 7150 50  0001 C CNN
F 3 "~" H 5750 7150 50  0001 C CNN
	1    5750 6950
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push Btn3
U 1 1 60CCA076
P 5750 7400
F 0 "Btn3" H 5750 7685 50  0000 C CNN
F 1 "SW_Push" H 5750 7594 50  0000 C CNN
F 2 "" H 5750 7600 50  0001 C CNN
F 3 "~" H 5750 7600 50  0001 C CNN
	1    5750 7400
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R1
U 1 1 60CFEEBB
P 6550 6950
F 0 "R1" V 6345 6950 50  0000 C CNN
F 1 "1k" V 6436 6950 50  0000 C CNN
F 2 "" V 6590 6940 50  0001 C CNN
F 3 "~" H 6550 6950 50  0001 C CNN
	1    6550 6950
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R1
U 1 1 60CFF45B
P 6700 6500
F 0 "R1" V 6495 6500 50  0000 C CNN
F 1 "1k" V 6586 6500 50  0000 C CNN
F 2 "" V 6740 6490 50  0001 C CNN
F 3 "~" H 6700 6500 50  0001 C CNN
	1    6700 6500
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R2
U 1 1 60D03EB0
P 6250 6800
F 0 "R2" H 6318 6846 50  0000 L CNN
F 1 "10k" H 6318 6755 50  0000 L CNN
F 2 "" V 6290 6790 50  0001 C CNN
F 3 "~" H 6250 6800 50  0001 C CNN
	1    6250 6800
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R2
U 1 1 60D041CD
P 6400 6350
F 0 "R2" H 6468 6396 50  0000 L CNN
F 1 "10k" H 6468 6305 50  0000 L CNN
F 2 "" V 6440 6340 50  0001 C CNN
F 3 "~" H 6400 6350 50  0001 C CNN
	1    6400 6350
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R1
U 1 1 60CFE0ED
P 6400 7400
F 0 "R1" V 6195 7400 50  0000 C CNN
F 1 "1k" V 6286 7400 50  0000 C CNN
F 2 "" V 6440 7390 50  0001 C CNN
F 3 "~" H 6400 7400 50  0001 C CNN
	1    6400 7400
	0    -1   1    0   
$EndComp
Wire Wire Line
	6400 6950 6250 6950
Wire Wire Line
	6250 6950 5950 6950
Connection ~ 6250 6950
Wire Wire Line
	6550 6500 6400 6500
Wire Wire Line
	5950 6500 6400 6500
Connection ~ 6400 6500
Connection ~ 6100 7400
Wire Wire Line
	5950 7400 6100 7400
Wire Wire Line
	6250 7400 6100 7400
$Comp
L Device:R_US R2
U 1 1 60D03A5F
P 6100 7250
F 0 "R2" H 6168 7296 50  0000 L CNN
F 1 "10k" H 6168 7205 50  0000 L CNN
F 2 "" V 6140 7240 50  0001 C CNN
F 3 "~" H 6100 7250 50  0001 C CNN
	1    6100 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 7400 5550 7400
Wire Wire Line
	5550 6950 5400 6950
Connection ~ 5400 6950
Wire Wire Line
	5400 6950 5400 7400
Wire Wire Line
	5550 6500 5400 6500
Wire Wire Line
	5400 6500 5400 6950
Wire Wire Line
	5400 6050 5400 6500
Connection ~ 5400 6500
$Comp
L power:GND Pin06
U 1 1 60D1B5BC
P 6400 6200
F 0 "Pin06" H 6322 6117 50  0000 R CNN
F 1 "GND" H 6322 6208 50  0000 R CNN
F 2 "" H 6400 6200 50  0001 C CNN
F 3 "" H 6400 6200 50  0001 C CNN
	1    6400 6200
	-1   0    0    1   
$EndComp
$Comp
L power:GND Pin06
U 1 1 60D2086E
P 6250 6650
F 0 "Pin06" H 6172 6567 50  0000 R CNN
F 1 "GND" H 6172 6658 50  0000 R CNN
F 2 "" H 6250 6650 50  0001 C CNN
F 3 "" H 6250 6650 50  0001 C CNN
	1    6250 6650
	-1   0    0    1   
$EndComp
$Comp
L power:GND Pin06
U 1 1 60D20D1E
P 6100 7100
F 0 "Pin06" H 6022 7017 50  0000 R CNN
F 1 "GND" H 6022 7108 50  0000 R CNN
F 2 "" H 6100 7100 50  0001 C CNN
F 3 "" H 6100 7100 50  0001 C CNN
	1    6100 7100
	-1   0    0    1   
$EndComp
Text Notes 5250 5350 0    79   ~ 0
LCD display
Wire Wire Line
	6650 4900 6650 4700
Wire Wire Line
	6600 4900 6650 4900
$Comp
L power:GND Pin6
U 1 1 60D3990F
P 6650 4700
F 0 "Pin6" H 6572 4617 50  0000 R CNN
F 1 "GND" H 6572 4708 50  0000 R CNN
F 2 "" H 6650 4700 50  0001 C CNN
F 3 "" H 6650 4700 50  0001 C CNN
	1    6650 4700
	-1   0    0    1   
$EndComp
Wire Wire Line
	6200 3600 6200 3450
Wire Wire Line
	6200 5200 6200 5550
Connection ~ 5600 4600
Wire Wire Line
	5600 5000 5800 5000
Wire Wire Line
	5600 4600 5600 5000
$Comp
L power:+5V Pin?
U 1 1 60D36300
P 6200 5550
F 0 "Pin?" H 6288 5633 50  0000 L CNN
F 1 "+5V" H 6288 5542 50  0000 L CNN
F 2 "" H 6200 5550 50  0001 C CNN
F 3 "" H 6200 5550 50  0001 C CNN
	1    6200 5550
	-1   0    0    1   
$EndComp
$Comp
L power:GND Pin6
U 1 1 60D35653
P 6200 3450
F 0 "Pin6" H 6122 3367 50  0000 R CNN
F 1 "GND" H 6122 3458 50  0000 R CNN
F 2 "" H 6200 3450 50  0001 C CNN
F 3 "" H 6200 3450 50  0001 C CNN
	1    6200 3450
	-1   0    0    1   
$EndComp
$Comp
L Device:R_POT_US RV
U 1 1 60D30D54
P 5100 4700
F 0 "RV" H 5033 4746 50  0000 R CNN
F 1 "R_POT_US" H 5033 4655 50  0000 R CNN
F 2 "" H 5100 4700 50  0001 C CNN
F 3 "~" H 5100 4700 50  0001 C CNN
	1    5100 4700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 4600 5800 4600
Wire Wire Line
	5250 4700 5800 4700
Wire Wire Line
	5100 4400 5100 4550
Wire Wire Line
	5600 4600 5600 4350
$Comp
L power:+5V Pin02
U 1 1 60D29F17
P 5100 4400
F 0 "Pin02" H 5188 4483 50  0000 L CNN
F 1 "+5V" H 5188 4392 50  0000 L CNN
F 2 "" H 5100 4400 50  0001 C CNN
F 3 "" H 5100 4400 50  0001 C CNN
	1    5100 4400
	1    0    0    -1  
$EndComp
$Comp
L power:GND Pin06
U 1 1 60D28BE7
P 5600 4350
F 0 "Pin06" H 5522 4267 50  0000 R CNN
F 1 "GND" H 5522 4358 50  0000 R CNN
F 2 "" H 5600 4350 50  0001 C CNN
F 3 "" H 5600 4350 50  0001 C CNN
	1    5600 4350
	-1   0    0    1   
$EndComp
$Comp
L Display_Character:WC1602A DS?
U 1 1 60CC47D1
P 6200 4400
F 0 "DS?" H 6200 5381 50  0000 C CNN
F 1 "WC1602A" H 6200 5290 50  0000 C CNN
F 2 "Display:WC1602A" H 6200 3500 50  0001 C CIN
F 3 "http://www.wincomlcd.com/pdf/WC1602A-SFYLYHTC06.pdf" H 6900 4400 50  0001 C CNN
	1    6200 4400
	-1   0    0    1   
$EndComp
$Comp
L MCU_Module:RaspberryPi-CM3 U?
U 1 1 60C94D24
P 8250 5500
F 0 "U?" H 8250 2111 50  0000 C CNN
F 1 "RaspberryPi-CM3" H 8250 2020 50  0000 C CNN
F 2 "" H 7650 8900 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/computemodule/datasheets/rpi_DATA_CM_1p0.pdf" H 7650 8900 50  0001 C CNN
	1    8250 5500
	1    0    0    -1  
$EndComp
$Comp
L power:+5V Pin02
U 1 1 60D18FAD
P 5400 6050
F 0 "Pin02" H 5488 6133 50  0000 L CNN
F 1 "+5V" H 5488 6042 50  0000 L CNN
F 2 "" H 5400 6050 50  0001 C CNN
F 3 "" H 5400 6050 50  0001 C CNN
	1    5400 6050
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 6100 6950 6100
Wire Wire Line
	6950 6100 6950 6500
Wire Wire Line
	6950 6500 6850 6500
Wire Wire Line
	7250 6200 7000 6200
Wire Wire Line
	7000 6200 7000 6950
Wire Wire Line
	7000 6950 6700 6950
Wire Wire Line
	7250 6300 7050 6300
Wire Wire Line
	7050 6300 7050 7400
Wire Wire Line
	6550 7400 7050 7400
Wire Wire Line
	6600 4800 7000 4800
Wire Wire Line
	7000 4700 7250 4700
Wire Wire Line
	6600 5000 7100 5000
Wire Wire Line
	7100 4000 7250 4000
Wire Wire Line
	6600 4000 6900 4000
Wire Wire Line
	6900 4300 7250 4300
Wire Wire Line
	6600 3900 6850 3900
Wire Wire Line
	6850 4400 7250 4400
Wire Wire Line
	6600 3800 6800 3800
Wire Wire Line
	6800 4500 7250 4500
Wire Wire Line
	7000 4800 7000 4700
Wire Wire Line
	7100 5000 7100 4000
Wire Wire Line
	6600 4100 7250 4100
Wire Wire Line
	6900 4000 6900 4300
Wire Wire Line
	6850 3900 6850 4400
Wire Wire Line
	6800 3800 6800 4500
$EndSCHEMATC
