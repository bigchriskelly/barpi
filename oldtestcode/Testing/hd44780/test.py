import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("Kveik Light IPA 7.8%", 1)
lcd.lcd_display_string("1.4C 28.3 Pints left", 2)
lcd.lcd_display_string("Kveik Cider 8%", 3)
lcd.lcd_display_string("1.8C 12.3 Pints left", 4)
