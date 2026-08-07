import requests
from bs4 import  BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
   soup = BeautifulSoup(response.text,"html.parser")
   h_3_tags = soup.find_all("h3")
   titles=[]
   for tag in h_3_tags[:20]:
       a_tag= tag.find("a")
       book_title = a_tag.get("title") or a_tag.text.strip()
       titles.append(book_title)
       print(f"titles of the book are ")
       for index ,title in enumerate(titles,start=1):
          print(f"{index} {titles}")
    
else:
    print("error")       
###################
url1="http://books.toscrape.com/"
response = requests.get(url1)  
if response.status_code == 200:
      soup = BeautifulSoup(response.text,"html.parser")
      books = soup.find_all("article" ,class_ ="product_pod")
      cheap_books=[]
      min_price_of_book =25.99
      for book in books:
          a_tag1 = book.find("h3").find("a")
          bk_title = a_tag1.get("title").a_tag1.text.strip()
          raw_price = book.find("p", class_="price_color").text.strip()
          remove_symbol = raw_price.replace("£","")
          price = float(remove_symbol)
          if price< min_price_of_book:
              cheap_books.append({"title":bk_title,"price":price})
      for index ,item in enumerate(cheap_books, start=1):
        print(f"{index} {item['cheap_books']} ,£{item['price']:.2f}")
else:
    print("error")                   
          
##############
url2 = "http://books.toscrape.com/"
response1= requests.get(url2)
if response1.status_code== 200:
    soup = BeautifulSoup(response1.text,"html.parser")
    all_atags= soup.find_all("a")
    internal_links=[]
    for tag in all_atags :
        href = tag.get("href")
        if href:
            href=href.strip()
            if not href.splitlines(("http:// ,https://")) and href!= "#":
                if href not in internal_links:
                    internal_links.append(href)
file_name = "internal_links.txt"
with open(file_name,encoding="utf-8") as file:
    for link in internal_links:
        file.write(link + "\n")
print("succedfully  extracted { len{internal_links}} internal_links")
print("saved to file {file_name}")
for index ,items in enumerate(internal_links[:10], start=1):
    print(f"{index} ++++ {link}")         
else:
    print("error")          
                    
#################
url3="https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
headers = {
    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}  
response3= requests.get(url3 , headers=headers)

if   response.status_code==200:
    soup= BeautifulSoup(response3.text,"html.parser")
    
    table= soup.find("tables", class_="wikitable")
    headers_list=[]
    for th in table.find_all("th"):
        headers_list.append(th.text.strip())
    first_row = table.find()
    headers_list= [th.text.strip() for th in first_row.find_all("th")]
    row_data =[]
    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all(["th" ,"tr"])
        row = [cell.text.strip() for cell in cells]
        if row:
            row_data.append(row)
    df = pd.DataFrame(row_data)
    print("table is as folows")
    print(df.head(10))        
else:
    print("error")    
    
        
        
    
#########
url44="http://books.toscrape.com/"
response4=requests.get(url44)
if response.status_code==200:
    soup5 = BeautifulSoup(response4.text,"html.parser")
    books=soup5.find_all("article",class_="product-pod")   
    filtered_books=[]
    keyword= "secret"
    for book in books:
        a_tagg = book.find("h3").find("a")
        title5 = a_tagg.get("title")or a_tagg.text.strip()
        raw_pricee = book.find("p" ,class_="price_color").text.strip()
        clean_pricee = float(raw_pricee.replace("£","").repalce("A",""))
        if keyword.lower() in title5.lower():
            filtered_books.append({"title":title5, "clean_price":clean_pricee})
            
    if filtered_books:
        df= pd.DataFrame(filtered_books)
        csv_filtername = "filtered_books.csv"
        df.to_csv(csv_filtername,index= False,encoding="utf-8")
        print(f"Found {len(filtered_books)} book(s) matching keyword '{keyword}':\n")
        print(df)
        print(f"\nSaved results to '{csv_filtername}'.")
    else:
        print("no books found")
else:
    print("error")        
                      
            

        