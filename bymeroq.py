import random
import string
from cryptography.fernet import Fernet
from colorama import Fore, Style, init

# colorama'yı terminalde düzgün çalışması için başlat
init(autoreset=True)

# Güçlü şifre oluşturucu
def güçlü_sifre_olusturucu():
    try:
        sifre_uzunlugu = int(input("Şifre uzunluğunu girin (Örneğin 12): "))
        if sifre_uzunlugu <= 0:
            print(Fore.RED + "Lütfen pozitif bir sayı girin.")
            return
        karakterler = string.ascii_letters + string.digits + string.punctuation
        sifre = ''.join(random.choice(karakterler) for _ in range(sifre_uzunlugu))
        print(Fore.GREEN + f"Oluşturulan güçlü şifre: {sifre}")
    except ValueError:
        print(Fore.RED + "Lütfen geçerli bir sayı girin.")

# Dosya şifreleme
def dosya_sifreleme():
    dosya_adi = input(Fore.CYAN + "Şifre K0yacagınız dosyanın ismini yazın (örn: github.com/charliecpln.txt): ")
    key = Fernet.generate_key()
    sifreleyici = Fernet(key)

    try:
        with open(dosya_adi, 'rb') as file:
            dosya_verisi = file.read()

        sifreli_veri = sifreleyici.encrypt(dosya_verisi)

        with open(dosya_adi + ".encrypted", 'wb') as sifreli_dosya:
            sifreli_dosya.write(sifreli_veri)

        print(Fore.GREEN + f"Dosya şifrelendi. Şifrelenmiş dosya: {dosya_adi}.encrypted")
        print(Fore.YELLOW + f"Bu dosyayı çözmek için anahtar: {key.decode()}")
    except FileNotFoundError:
        print(Fore.RED + "Dosya bulunamadı. Lütfen dosya adını kontrol edin.")

# Mesaj şifreleme
def mesaj_sifreleme():
    mesaj = input(Fore.CYAN + "Şifrelenecek mesajı girin: ")
    key = Fernet.generate_key()
    sifreleyici = Fernet(key)

    sifreli_mesaj = sifreleyici.encrypt(mesaj.encode())

    print(Fore.GREEN + f"Şifrelenmiş mesaj: {sifreli_mesaj.decode()}")
    print(Fore.YELLOW + f"Bu mesajı çözmek için anahtar: {key.decode()}")

# Bilgilendirme Menüsü
def bilgilendirme_menusu():
    print(Fore.MAGENTA + """
    ------------------------------
             BİLGİLENDİRME
    ------------------------------
            @Bilgilendirme:

    1. Güçlü şifreler oluşturabilirsiniz.
    2. Bu Program @Bymeroq Tarafından Yapılmıştır.
    3. Dosya şifreleme ve şifre çözme işlemleri yapabilirsiniz.
    4. Mesajları şifreleyip güvenle saklayabilirsiniz.

    Devam etmek için 'Enter' tuşuna basın.
    ------------------------------
    """)
    input()

# Ana Menü
def ana_menu():
    # @Bymeroq yazısı için renkler
    print(Fore.YELLOW + """
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @                         @
        @      """ + Fore.RED + "@Bymeroq" + Fore.YELLOW + """            @
        @                         @
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """)

    while True:
        print(Fore.CYAN + "\nAna Menü:")
        print(Fore.CYAN + "1. Güçlü Şifre Oluşturucu")
        print(Fore.MAGENTA + "Github.com/charliecpln")
        print(Fore.CYAN + "2. Dosya Şifreleme")
        print(Fore.CYAN + "3. Mesaj Şifreleme")
        print(Fore.CYAN + "4. Bilgilendirme")
        print(Fore.CYAN + "5. Çıkış")

        secim = input(Fore.CYAN + "Bir seçenek seçin: ")

        if secim == "1":
            güçlü_sifre_olusturucu()
        elif secim == "2":
            dosya_sifreleme()
        elif secim == "3":
            mesaj_sifreleme()
        elif secim == "4":
            bilgilendirme_menusu()
        elif secim == "5":
            print(Fore.RED + "Çıkış yapılıyor...")
            break
        else:
            print(Fore.RED + "Geçersiz seçim, lütfen tekrar deneyin.")

# Programı başlatırken doğrudan ana menüyü göster
ana_menu()

input("Programdan çıkmak için 'Enter' tuşuna basın...")
