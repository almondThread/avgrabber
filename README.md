avgrabber
=========

Tool for grab data from Avito.ru

Это пробный образец нового функционала.
Для демонстрации функционала нужно выполнить команды:

**C:\avgrabber> cli.py new project ps4 "PS4, playstation 4"**  
Project ps4 (query='PS4, playstation 4') has been created

**C:\avgrabber> cli.py update ps4**  
11.01.2015, Продам (обменяю) Need For Speed rivals на PS4, 1500, https://www.avito.ru/smolensk/igry_pristavki_i_programmy/prodam_obmenyayu_need_for_speed_rivals_na_ps4_458946716  
24.11.2014, Dendy Sega Xbox 360 Xbox One Playstation 3 4, 850, https://www.avito.ru/smolensk/igry_pristavki_i_programmy/dendy_sega_xbox_360_xbox_one_playstation_3_4_465943875
...

**C:\avgrabber> cli.py list updates ps4**  
Update 14.01.2015 10:11:36  
    11.01.2015, Продам (обменяю) Need For Speed rivals на PS4, 1500, https://www.avito.ru/smolensk/igry_pristavki_i_programmy/prodam_obmenyayu_need_for_speed_rivals_na_ps4_458946716  
    24.11.2014, Dendy Sega Xbox 360 Xbox One Playstation 3 4, 850, https://www.avito.ru/smolensk/igry_pristavki_i_programmy/dendy_sega_xbox_360_xbox_one_playstation_3_4_465943875  
    ...
