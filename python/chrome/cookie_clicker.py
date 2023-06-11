from selenium import webdriver

import time

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/" # link que iremos acessar
        self.SITE_MAP = {
            "buttons": {
                "biscoito": {
                    "xpath": "/html/body/div/div[2]/div[15]/div[8]/button"
                },
                "upgrade": {
                    "xpath": "/html/body/div/div[2]/div[19]/div[3]/div[6]/div[$$NUMBER$$]"
                },
                "idiomas": {
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]"
                }
            }
        }

        # /html/body/div/div[2]/div[19]/div[3]/div[6]/div[2]
        # /html/body/div/div[2]/div[19]/div[3]/div[6]/div[3]
    
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe") # irá executar o driver do google chrome
        self.driver.maximize_window() # maximizar o navegador em tela cheia

    def abrirSite(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        print('fechando...')

    # def clicarNoCookie(self):
    #     self.driver.find_element(self.SITE_MAP["buttons"]["biscoito"]["xpath"]).click()

    # def pegaMelhorUpgrade(self):
    #     encontrei = False

    #     elementoAtual = 2

    #     while not encontrei:
    #         objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(elementoAtual))
    #         classe_objeto = self.driver.find_element(object).get_attribute("class")

    #         if not "enabled" in classe_objeto:
    #             encontrei = True
    #         else:
    #             elementoAtual += 1
    #     return elementoAtual - 1

    # def comprarUpgrade(self):
    #     objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace('$$NUMBER$$', str(self.pegaMelhorUpgrade()))
    #     self.driver.find_element(objeto).click()

biscoito = CookieClicker()
biscoito.abrirSite()

# i = 0

# while True:
#     if i % 500 == 0 and i != 0:
#         time.sleep(1)
#         biscoito.comprar_upgrade()
#         time.sleep(1)
#     biscoito.clicarNoCookie()
#     i += 1 