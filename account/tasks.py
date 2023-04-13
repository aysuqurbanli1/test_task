from django.conf import settings
from celery import shared_task
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from account.models import Instagram




@shared_task
def instagram_data():
    a=Instagram.objects.all().first()

    username = a.username
    password = a.password

    chrome = webdriver.Chrome()
    url = "https://www.instagram.com/"
    chrome.get(url)

    
    try:
        username_field=WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.NAME,'username')))
        username_field.send_keys(username)

        

        password_field=WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.NAME,'password')))
        password_field.send_keys(password)

        

        login_button=WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')))

        login_button.click()

        time.sleep(15)

        chrome.get("https://www.instagram.com/" + username)

        time.sleep(5)

        ul=WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.TAG_NAME,'ul')))


        items=ul.find_elements(By.TAG_NAME,'li')
        follower=items[1].find_element(By.TAG_NAME,'span').text
        following=items[2].find_element(By.TAG_NAME,'span').text
        
        print(follower)
        print(following)

        try:
            instagram_data=Instagram.objects.get(username=username)
            if instagram_data:
                instagram_data.follower=follower
                instagram_data.following=following
                instagram_data.save()

        except:
            Instagram.objects.create(username=username, follower=follower,following=following)


    except TimeoutException:
        time.sleep(5)
        print("Done")
    chrome.quit()







