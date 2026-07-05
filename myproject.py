import requests
from bs4 import BeautifulSoup
import time
import csv
url='http://books.toscrape.com'
#below, is to mask the script so it doesn't get rejected by the server

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64: x64) ApplleWebKit/537.36(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
response= requests.get(url, headers=headers) #will return everything on that webpage not just html.

with open('Scraped_books.csv','w',encoding='utf-8-sig',newline='') as file:
    writer= csv.writer(file)
    writer.writerow(['Book Title','Price(£)','Link','Status'])#creates the head columns

    soup= BeautifulSoup(response.text,'html.parser')
    books= soup.find_all('article', class_='product_pod')
    for book in books:
        book_title= book.find('h3').a.text
        book_price= book.find('p',class_='price_color').text
        new_price= float(book_price[2:]) #to remove the £ sign
        book_link= book.a.get('href')
        availability= book.find('p', class_='instock availability').text.strip()

        writer.writerow([book_title, new_price, book_link, availability])
        time.sleep(2)# initiates a polite 2 second wait
file.close()
print('CSV File Saved!')
