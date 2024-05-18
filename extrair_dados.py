import time
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
url = "https://steamdb.info/sales/"
driver.get(url)
dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'DataTables_Table_0_length')))
dropdown.click()
option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'option[value="-1"]')))
option.click()
time.sleep(3)
data = []
table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table#DataTables_Table_0')))
rows = table.find_elements(By.CSS_SELECTOR, 'tr')
for row in rows:
    cols = row.find_elements(By.CSS_SELECTOR, 'td')
    cols_text = [col.text for col in cols]
    data.append(cols_text)
df = pd.DataFrame(data)
df.to_parquet('dados.parquet', engine='pyarrow')
driver.quit()
