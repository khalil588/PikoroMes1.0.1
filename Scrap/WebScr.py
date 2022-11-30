
import os
import time
import  pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import Constant as cnst

class Scrapper2 (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper2,self).__init__()
        self.implicitly_wait(30)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()





    def getData(self, x,y):
        lst = []
        time.sleep(5)
        table = self.find_element(by=By.CSS_SELECTOR, value='#parc > table')
        rows = table.find_elements(by=By.TAG_NAME, value="tr")

        for z in range(1,(len(rows))):
            i=z+1
            row = rows[z]

            value_list = row.find_elements(By.TAG_NAME, "td")
            l = {}
            l[cnst.Columns[0]] = x
            l[cnst.Columns[1]] = y
            j = 1
            for v in value_list:
                j += 1
                if j < 7 :
                    l[cnst.Columns[j]] = v.text
                else :
                    my_element = self.find_element(by=By.XPATH,value='//*[@id="parc"]/table/tbody/tr[' + str(i) + ']/td[6]/a')
                    l[cnst.Columns[j]] = my_element.get_attribute('href')
            print(l)
            lst.append(l)

        return lst


    def land_first_page(self, x):
        df1 = pd.DataFrame()
        link = cnst.link
        self.get(link)
        select = Select(self.find_element(by=By.XPATH, value='//*[@id="univ"]'))
        select.select_by_value(x)
        uni = select.first_selected_option.text
        time.sleep(5)
        select = Select(self.find_element(by=By.XPATH, value='//select[@id="etablisement"]'))
        l = select.options
        for i in l[1:]:
            print(i.text)
            select.select_by_visible_text(i.text)
            df = pd.DataFrame.from_dict(self.getData(uni,i.text))
            df1 = df1.append(df)
        print(len(df1))
        return df1

