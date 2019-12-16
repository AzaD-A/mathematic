# created by azad
# follow me on IG @p8z4
import math
import sys
from os import system

zhmeryarbanner = '''
     __                __             
    /_ |      _       /_ |    ______ 
    | |     _| |_     | |    |______|
    | |    |_   _|    | |     ______ 
    | |      |_|      | |    |______|
    |_|               |_|            
    with azad                               
                    '''
system('clear')
yakabanner = '''
    ███╗   ███╗    ██╗       ██████╗███╗   ███╗
    ████╗ ████║    ╚██╗     ██╔════╝████╗ ████║
    ██╔████╔██║     ╚██╗    ██║     ██╔████╔██║
    ██║╚██╔╝██║     ██╔╝    ██║     ██║╚██╔╝██║
    ██║ ╚═╝ ██║    ██╔╝     ╚██████╗██║ ╚═╝ ██║
    ╚═╝     ╚═╝    ╚═╝       ╚═════╝╚═╝     ╚═╝
    with azad :
    '''
system('clear')
mathebanner = ''' 
                  _   _                          _   _      
                 | | | |                        | | (_)     
  _ __ ___   __ _| |_| |__   ___ _ __ ___   __ _| |_ _  ___ 
 | '_ ` _ \ / _` | __| '_ \ / _ \ '_ ` _ \ / _` | __| |/ __|
 | | | | | | (_| | |_| | | |  __/ | | | | | (_| | |_| | (__ 
 |_| |_| |_|\__,_|\__|_| |_|\___|_| |_| |_|\__,_|\__|_|\___|
 with azad :)                                                                                                                   
'''
def math1():
    print(mathebanner + '''
    •1• --> Zhmeryar
    •2• --> Yaka Gorini m-dm-cm-mm
    •3• --> Yasay Shewakan 2 duri 
    •4• --> Pewany Barstay Lasht Bzana
    •0• --> Darchun    
    ''')
    math1 = input(' Kamayan halabazherit : ')
    if math1 == '1':
        zhmeryar()
    elif math1 == '2':
        yaka()
    elif math1 == '3':
        yasa()   
    elif math1 == '4':
        kesh()
    elif math1 == '0':
        sys.exit()
    else:
        print('''
    Tkaya Zhmarayaki Drust Hallbzhera u Dubara Bikarawa!!!''')
def yaka():
    system('clear')
    print(yakabanner)
    print('''
    #####################################################################
    #                            1 : m bo dm                            #
    #                            2 : m bo cm                            #
    #                            3 : m bo mm                            #
    #####################################################################
    #           4 : dm bo  m         {0}         7 : cm bo  m           #
    #           5 : dm bo cm     bo garanawa     8 : cm bo dm           #
    #           6 : dm bo mm      bo sarata      9 : cm bo mm           #
    #####################################################################
    #                            10 : mm bo  m                          #
    #                            11 : mm bo dm                          #
    #                            12 : mm bo cm                          #
    #####################################################################
    ''')

    mathe = input(' zhmarayak halbzhera : ')
    print(' _____________________________________________________________________')
    if mathe == '1':
        a = input(' {+} m chanda : ')
        x = float(a) * 10
        print(' _____________________________________________________________________')
        print(f" [!] dm = {x}")
    elif mathe == '2':
        a = input(' {+} m chanda : ')
        x = float(a) * 100
        print(' _____________________________________________________________________')
        print(f" [!] cm = {x}")
    elif mathe == '3':
        a = input(' {+} m chanda : ')
        x = float(a) * 1000
        print(' _____________________________________________________________________')
        print(f" [!] mm = {x}")
    elif mathe == '4':
        a = input(' {+} dm chanda : ')
        x = float(a) / 10
        print(' _____________________________________________________________________')
        print(f" [!] m = {x}")    
    elif mathe == '5':
        a = input(' {+} dm chanda : ')
        x = float(a) * 10
        print(' _____________________________________________________________________')
        print(f" [!] cm = {x}")
    elif mathe == '6':
        a = input(' {+} dm chanda : ')
        x = float(a) * 100
        print(' _____________________________________________________________________')
        print(f" [!] mm = {x}")
    elif mathe == '7':
        a = input(' {+} cm chanda : ')
        x = float(a) / 100
        print(' _____________________________________________________________________')
        print(f" [!] m = {x}")    
    elif mathe == '8':
        a = input(' {+} cm chanda : ')
        x = float(a) / 10
        print(' _____________________________________________________________________')
        print(f" [!] dm = {x}")    
    elif mathe == '9':
        a = input(' {+} cm chanda : ')
        x = float(a) * 10
        print(' _____________________________________________________________________')
        print(f" [!] mm = {x}")    
    elif mathe == '10':
        a = input(' {+} mm chanda : ')
        x = float(a) / 1000
        print(' _____________________________________________________________________')
        print(f" [!] m = {x}")   
    elif mathe == '11':
        a = input(' {+} mm chanda : ')
        x = float(a) / 100
        print(' _____________________________________________________________________')
        print(f" [!] dm = {x}")   
    elif mathe == '12':
        a = input(' {+} m chanda : ')
        x = float(a) / 10
        print(' _____________________________________________________________________')
        print(f" [!] cm = {x}")
    elif mathe == '0':
        system('clear')
        math1()
    else:
        print('''
    Tkaya Zhmarayaki Drust Hallbzhera u Dubara Bikarawa!!!''')
def zhmeryar(): 
    system('clear')
    print(zhmeryarbanner)
    print('''
    #########################################################
    #       #           Zhmeryary Kurdi             #       #
    #      #                                         #      #
    #     #                                           #     #
    #    #                                             #    #
    #   #                     {1} +                     #   #
    #  #                      {2} -                      #  #
    # #                       {3} x                       # #
    ##                        {4} ÷                        ##
    #                         {0} bo garanawa bo sarata     # 
    #########################################################
    ''')
    zhmeryar = input(' Zhmarayak Halbzhera :  ')
    print(' +==+==+==+==+==+==+==+')
    if zhmeryar == '1':
        x = input(' {1} zhmaray yakam : ')
        y = input(' {2} zhmaray dwam : ')
        z = float(x) + float(y)
        print(f" [!] Anjamaka : {z} ")
    elif zhmeryar == '2':
        a = input(' {1} zhmaray yakam : ')
        b = input(' {2} zhmaray dwam : ')
        c = float(a) - float(b)
        print(f" [!] Anjamaka : {c} ") 
    elif zhmeryar == '3':
        m = input(' {1} zhmaray yakam : ')
        n = input(' {2} zhmaray dwam : ')
        o = float(m) * float(n)
        print(f" [!] Anjamaka : {o} ")       
    elif zhmeryar == '4':
        r = input(' {1} zhmaray yakam : ')
        s = input(' {2} zhmaray dwam : ')
        t = float(r) / float(s)
        print(f" [!] Anjamaka : {t} ")        
    elif zhmeryar == '0':
        system('clear')
        math1()
    else: 
        print('''
    Tkaya Zhmarayaki Drust Hallbzhera u Dubara Bikarawa!!!''')  
class yasa:
    def __init__(yasa1):
        system('clear')    
        print('''
                             
                    
         ##            ###########         ######        #####################
        ####           ###########       ##########      #####################
       ######          ###########      ############     #####################
      ########         ###########      ############     #####################
     ##########        ###########       ##########      #####################
    ############       ###########         ######        #####################
     
    {1} :- Yasay Se Gosha
    
    {2) :- Yasay Chwar Gosha
    
    {3) :- Yasay Bazna
    
    {4) :- Yasay Lakesha 
    
    {0} :- Bo Garanawa

        ''')
        
        aza = input(' Danayak Halbzhera : ')
        system('clear')
        if aza == '1':
            print('''                     
              #     
             # #    
            #   #   
           #     #    
          #       #  
         #         #
        #############  
 
    {1} :- Yasay Rubar
    
    {2) :- Yasay Pythagoras
    
    {0} :- Bo Garanawa
            ''')
            azakurd = input(' {+} Danayak Halbzhera : ')
            print(' =-=-=-=-=-=-=-=-=-=-=-=')
            if azakurd == '1':
                barzy = input(' {1} barzy chanda : ')
                print(' =-=-=-=-=-=-=-=-=-=-=-=')
                bnka = input(' {2} bnka chanda : ')
                zher = float(barzy) * float(bnka) * 0.5
                print(' =-=-=-=-=-=-=-=-=-=-=-=')
                print(f" Anjamaka : {zher}")
            elif azakurd == '0':
                math1()
            elif azakurd == '2':
                system('clear')
                print('''
    --------------v--------------
    -------------vvv-------------
    ------------vvvvv------------
    -----------vvvvvvv-----------
    ----------vvvvvvvvv----------
    ---------vvvvvvvvvvv---------
    --------vvvvvvvvvvvvv--------
    
    {1} :- Dozinaway Zhe
    
    {2) :- Dozinaway La
    
        ''')
                azagyan = input(' {+} Danayak Halbzhera : ')
                if azagyan == '1':
                    system('clear')
                    print('''
    ####################################################
    ##########          Yasay Yakam          ###########
    ###########                             ############
    ############      bo Dozinaway zhe     #############
    #############                         ##############
    ##############                       ###############
    ####################################################
             Tkaya Am Yasaya Bo Dozinaway zhe!
    ''')
                    a = input(' {1} yakam La chanda : ')
                    print(' +=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    b = input(' {2} dwam La chanda : ')
                    print(' +=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    c = float(a) * float(a) 
                    d = float(b) * float(b) 
                    nop = float(c) + float(d)
                    h = math.sqrt(nop)
                    z = h
                    print(' =-=-=-=-=-=-=-=-=-=-=-=')            
                    print(f" [!] Anjamaka : {z}")
                elif azagyan == '2':
                    system('clear')
                    print('''
    ####################################################
    ##########          Yasay Yakam          ###########
    ###########                             ############
    ############     bo Dozinaway Laya     #############
    #############                         ##############
    ##############    {0} bo garanawa    ###############
    ####################################################
         Tkaya Am Yasaya Bo Dozinaway Laya!(kurtaka)
      Tkaya Sarata Zhmara gawraka Bnusa Inja Bchukaka!!!        
             ''')
                    azad = input(' {1} Yakam La chanda : ')
                    print(' =-=-=-=-=-=-=-=-=-=-=-=')           
                    ahmad = input(' {2} Dwam La chanda : ')
                    print(' =-=-=-=-=-=-=-=-=-=-=-=')       
                    mhamad = float(azad) * float(azad)
                    kurd = float(ahmad) * float(ahmad)
                    kurdish = float(mhamad) - float(kurd)
                    kurde = math.sqrt(kurdish)
                    print(f" [!] anjamaka : {kurde}")
                
        if aza == '2':
                print('''
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
    ------#######################------
                ''')
                azakam = input(' [1] Drezhi chanda : ')
                print(' =-=-=-=-=-=-=-=-=-=-=-=')
                avakam = float(azakam) * float(azakam)
                azoka = print(f" [!] Anjamaka : {avakam}")
        if aza == '3':
                print('''
             , - ~ ~ ~ - ,
         , '               ' ,
       ,                       ,
      ,                         ,
     ,                           ,
     ,       U  =  PI x d         ,
     ,                           ,
      ,                         ,
       ,                       ,
         ,                  , '
           ' - , _ _ _ ,  '
        
    {1} :- Dozinaway Ba -D-
    
    {2) :- Dozinaway Ba -R-
                  
    ''')
                azadp = input(' [+] danyak halbzhera : ')
                if azadp == '1':
                    print(' =-=-=-=-=-=-=-=-=-=-=-=')            
                    d = input(' [+] d chanda : ')
                    x = float(d) * 3.1415
                    print(' =-=-=-=-=-=-=-=-=-=-=-=')                
                    print(f" [!] Anjamaka = {x}")
                elif azadp == '2':
                    r = input(' [+] danayak halbzhera :  ')
                    xr = float(r) * 2 * 3.1415
                    print(f" [!] Anjamaka = {xr}")
                else:
                    print('''
        Tkaya Zhmarayaki Drust Hallbzhera u Dubara Bikarawa!!!''')  
                    
                    
        if aza == '4':
                        print('''
    ------###############################------
    ------###############################------
    ------###############################------
    ------###############################------
    ------###############################------
    ------###############################------
    ------###############################------
                            
                        
        ''')
                        avok = input(' [+] drezhi chanda : ')
                        print(' =-=-=-=-=-=-=-=-=-=-=-=')
                        avka = input(' [+] pani chanda : ')
                        print(' =-=-=-=-=-=-=-=-=-=-=-=')
                        av = float(avok) * float(avka)
                        print(f" [!] anjamaka {av}")
        if aza == '0':
                        math1()
def kesh():
    system('clear')
    print('''

     ████████╗ █████╗ ██████╗  █████╗ ███████╗██╗   ██╗
     ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══███╔╝██║   ██║
        ██║   ███████║██████╔╝███████║  ███╔╝ ██║   ██║
        ██║   ██╔══██║██╔══██╗██╔══██║ ███╔╝  ██║   ██║
        ██║   ██║  ██║██║  ██║██║  ██║███████╗╚██████╔╝
        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ 
     with azad                                                 
    
    [1]-Pewany Barstay Lasht Bzana
    [0]-Garanawa ''')
    x = input(' kamayan : ')
    print(' =-=-=-=-=-=-=-=-=-=-=-=')
    if x == '1':
        balla = input(' {+} ballat chanda : ')
        print(' =-=-=-=-=-=-=-=-=-=-=-=')
        qabara = input(' {+} chand kiloit : ')
        print( ' =-=-=-=-=-=-=-=-=-=-=-=')
        barzy = int(balla) / 100 * int(balla)
        kesh = int(qabara) / int(barzy) * 100
        print(f" [!] Anjamaka : {kesh}")
        print(' =-=-=-=-=-=-=-=-=-=-=-=')
        print(''' 
        [-] 16 kesht zor zor lawaza
        [-] 17 > 17 kesht zor lawaza
        [-] 17 > 18.5 kesht lawaza
        [=] 18.5 > 25 asait
        [+] 25 > 30 kesht qalawa
        [+] 30 > 35 kesht zor qalawa
        [+] 35 > 40 kesht zor zor qalawa
        ''')
    elif x == '0':
        system('clear')
        math1()
    else:
        print(' Tkaya Zhmarayaki Drust Hallbzhera u Dubara Bikarawa!!! ')
    

































 
 
 
 
 
if __name__ == "__main__":
    math1()
  
