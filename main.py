from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🔧 Configuração do navegador
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 🌐 Acessa o Google
driver.get("https://www.google.com/")
time.sleep(2)  # Aguarda a página carregar

# 🧠 Encontra o campo de busca e digita "Messi"
try:
    campo_pesquisa = driver.find_element(By.CLASS_NAME, "gLFyf")
    campo_pesquisa.send_keys("Messi Best Skills")
    campo_pesquisa.send_keys(Keys.RETURN)  # Pressiona Enter
    print("✅ Pesquisa realizada com sucesso!")
except Exception as e:
    print(f"❌ Erro: {e}")

# Aguarda um pouco para ver o resultado
time.sleep(9)

# Encerra o navegador
driver.quit()
