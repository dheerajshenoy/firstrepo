import requests
from bs4 import BeautifulSoup
from os import system

def fetch():
    url = "https://www.distrowatch.com"
    response = requests.get(url)
    if(response.status_code == 200):
        soup = BeautifulSoup(response.text,"html.parser")
        s1 = soup.find_all(class_="phr2")
        s2 = soup.find_all(class_="phr3")
        for i in range(len(s1)):
            print(str(i+1) + "." + s1[i].text + "(" + s2[i].text + ")")
    
if __name__ == "__main__":
    system("clear")
    print("DISTROWATCH best linux distro list:")
    fetch()
