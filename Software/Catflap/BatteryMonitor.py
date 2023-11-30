from machine import Pin, Timer, ADC, PWM
import time
import math

def BatteryMonitor(BatteryCapacity, AverageCurrent):
        BAT_MON_EN = Pin(22, Pin.OUT)
        BAT_MON = ADC(Pin(26))
        Warning_lamp = PWM(Pin(4, Pin.OUT))
        Warning_lamp.freq(5000)

        BAT_MON_EN.value(1)	#Enable the pin to be able to measure the voltage
        time.sleep(0.001) # Delay 1ms in order to get a stable reading, don't know if necessary
        BatteryValue = BAT_MON.read_u16() # Read the Value from the voltage devider circuit BAT_MON
        BAT_MON_EN.value(0)	# Turn off the pin to save power because we don't need to have the mosfet on all the time.
        
        BatteryCapacity = BatteryCapacity # Battery capacity in mAh, inargument
        AverageCurrent = AverageCurrent # Average current consumption in mAh
        
        BatteryLOW_THRESHOLD_VOLTAGE = 3.6 # Setting a LOW voltage threshold
        BatteryLOW_THRESHOLD_Value = BatteryLOW_THRESHOLD_VOLTAGE*220000*65536/(560000*3.3)
        
        # Doing a if statement that tell if the battery is under/over a selected value.
        if BatteryValue < BatteryLOW_THRESHOLD_Value: 
            BatteryLOW = 1	# Turn on the LOWBattery indicator to tell if its low battery or not.
            Warning_lamp.duty_u16(5000)	# Turn on a lamp to indicate low battery
        else:
            BatteryLOW = 0
            Warning_lamp.duty_u16(0)
        
        BatteryVoltage = BatteryValue*3.3*560000/(65536*220000) # Change to 560000 to compensate, now the voltage is more accurate
        BatteryPercentage = (BatteryVoltage-3.6)/.0276 # Vmax=4*1.59=6.36 Vmin=0.9*4=3.6 0.0276=(Vmax-VMin)/100 	LINEAR.. :(
        
        # Claming max and min percentage if battery is to high or to low.
        if BatteryPercentage < 0:		
            BatteryPercentage = 0
        if BatteryPercentage > 100:
            BatteryPercentage = 100


        BV = BatteryVoltage
        #BatteryPercentageNEW =-0.2027*math.pow(BV,7)+1.8740*math.pow(BV,6)-7.2717*math.pow(BV,5)+15.1045*math.pow(BV,4)-18.0211*math.pow(BV,3)+12.4596*math.pow(BV,2)-5.2252*BV+6.3595
        BatteryPercentageNEW = -0.1029*math.pow(BV,2)-0.6416*BV+5.9508
        # BatteryPercentageNEW =math.pow(BatteryVoltage,7)
        BatteryValue = BatteryValue
        BatteryLOW = BatteryLOW
        BatteryDays = BatteryCapacity*BatteryPercentage*0.01/(AverageCurrent*24)
        
        return BatteryVoltage, BatteryPercentage, BatteryPercentageNEW, BatteryValue, BatteryLOW, BatteryDays

#BatteryVoltage, BatteryPercentage, BatteryPercentageNEW, BatteryValue, BatteryLOW, BatteryDays = BatteryMonitor()

#print(BatteryVoltage)
#print(BatteryPercentage)
#print(BatteryValue)
#print(BatteryLOW)


# Simple Voltage devider circuit with two resistors R1 = 330k and R2 = 220k
# 16 bit measure 65536 values
# Voltage at Bat_Mon = V_Bat*220k/(220k+330k)
# V_Raspberry=3.3V The value at ADC range on the Raspberry
# Value at Bat_Mon = V_Bat*220k*2^16/((220k+330k)*V_Raspberry)

# From value to V_Bat
# V_Bat = Bat_Mon*V_Raspberry*(220k+330k)/(220k*2^16)


# Tested 5V from ppk2 to test values 

# 5.0V = 38889 38857 39081 38921 38761 38901.8
# 4.9V = 38249 38473 38121 37961 38025 38196.2
# 4.8V = 37577 37721 37497 37369 37449 37522.6
# 4.7V = 36504 36776 36808 36824 36760 36734.4
# 4.6V = 36104 36040 35784 36184 36152 36052.8
# 4.5V = 35112 35416 35288 35288 35400 35300.8
# 4.4V = 34440 34712 34568 34440 34600 34552
# 4.3V = 33960 33848 33736 33752 33416 33742.4
# 4.2V = 33112 33160 33160 33064 33080 33115.2
# 4.1V = 32295 32199 32135 32311 32215 32231
# 4.0V = 31639 31495 31591 31527 31655 31581.4
# 3.9V = 30775 30807 30839 30855 30759 30807
# 3.8V = 29767 29655 29623 29671 29719 29687
# 3.7V = 29063 29351 28903 29031 29063 29082.2
# 3.6V = 28262 28246 28294 28246 28470 28303.6
# 3.5V = 27622 27510 27526 27606 27558 27564.4
# 3.4V = 26966 26966 26950 26934 26966 26956.4
# 3.3V = 26278 26432 26198 26150 26182 26248
# 3.2V = 25622 25430 25414 25478 25478 25484.4

