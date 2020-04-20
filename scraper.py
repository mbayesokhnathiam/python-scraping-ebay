import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# On crée une instance du web-driver Firefox et on va sur la page de eBay.fr pour tester
fp = webdriver.FirefoxProfile
driver = webdriver.Firefox(fp)
driver.get("http://www.ebay.fr")

# On crée une instance du web-driver Chromium Browser et on va sur la page de eBay.fr pour tester
# Commande pour installer chromium-driver: sudo apt-get install chromium-chromedriver
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# driver.get("http://www.ebay.fr")

# En fonction de notre connection et des performance de notre machine il faudra attendre
# que la page charge avant de passer à la suite
time.sleep(10)


# On recupere la bar de recherche, on la remplit avec "iphone" puis on appuie "Entrez"
search_bar = driver.find_element_by_name("_nkw")
search_bar.send_keys("iphone")
search_bar.send_keys(Keys.ENTER)


is_last_page = False
while not is_last_page:
    offers = driver.find_elements_by_css_selector("div#ResultSetItems ul li.sresult")
    for offer in offers:
        title = offer.find_element_by_css_selector("h3.lvtitle a").get_attribute("title")
        print("Titre : ",title)
        image = offer.find_element_by_css_selector("div.lvpicinner img.img").get_attribute("src")
        print("Image : ",image)
        price = offer.find_element_by_css_selector("li.lvprice span").text
        print("Prix : ",price)
        print("")
    next_page = driver.find_element_by_css_selector("table#Pagination a.next")
    is_last_page = next_page.get_attribute("arial-disabled")
    if is_last_page == "true" or is_last_page == "True":
        is_last_page = True
    else:
        next_page.click()
    time.sleep(10)