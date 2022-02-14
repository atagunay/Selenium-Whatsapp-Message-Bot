from __future__ import absolute_import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Assigned chrome driver to the wd
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# mesajın yazıldığı dosya okuma modunda açılır
f = open("messages.txt", "r", encoding="utf-8")
text = f.readline()  # Dosyanın ilk satırı okunur


def start():
    flag = False  #Mesajın 1 kere atılması için kontrol değişkeni

    driver.implicitly_wait(3) # Eğer google chrome açılmazsa 3 saniye fazladan beklenir
    driver.get("https://web.whatsapp.com/")  # Whatsapp web sayfasına gidilir

    # Kullanıcı wp ' ye giriş yapıp mesaj atacağı kişiyi seçmesi için bir bekleme inputu konmuştur
    input("If you login Whatsapp and select your contact please enter a character and press enter: ")

    # Find text input
    text_input = driver.find_element(By.XPATH,
         value="/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")

    while flag == False:
        text_input.click()  # Mesaj atılacak kısma tıkla
        try:
            # Online olup olmama durumunu gösteren ögeyi bul
            online_situation = driver.find_element(By.XPATH,
                      value="/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]")
            if (online_situation.text in ['çevrimiçi', 'online']) and not flag: # Eğer bulunan öge çevrimiçi ise
                flag = True
                text_input.send_keys(text) # mesajı yaz
                text_input.send_keys(Keys.ENTER) # enter a bas
        except:  # eğer try bloğunda bir hata ile karşılaşılırsa flagi false olarak devam etti
            flag = False
        sleep(5)  #Döngünün sürekli kontrol etmesine gerek yok. O yüzden 5sn' de bir kontrol etsin.

# Fonksiyonun çağrılması
start()
