import requests
import os
from bs4 import BeautifulSoup

# Clear Console On Windows/Linux
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Format PosLaju Tracking Number To Be Accurate
def formatPL(tr):
    length = 2
    status = False
    los = []
    for i in range(0, len(tr), length):
        los.append(tr[i:length+i])
    
    if los[0] == 'PL' and len(tr) == 14:
        status = True
    else:
        status = False

    return status

def exit():
    ex = str(input("\nDo You Want To Continue? (Y/N):"))
    ex = ex.upper()

    print("\n")
    if ex == 'Y':
        cls()
        main()
    else:
        return

def main():
    print("#########################")
    print("# PosLaju Tracker v0.1 #")
    print("# Coded By Noor Aiman  #")
    print("########################\n")

    tr_num = str(input("Tracking Number: "))
    tr_num = tr_num.upper()

    if(formatPL(tr_num)):
        url = "https://sendparcel.poslaju.com.my/open/trace"
        payload = {"tno":tr_num}
        res = requests.session()
        header = {
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        res = requests.get(url,payload, headers = header, timeout=5)
        html_data = res.content

        # Get Table Row and Columns
        table_data = [[cell.text for cell in row("td")]
            for row in BeautifulSoup(html_data, features="lxml")("tr")]

        if len(table_data) > 0:
            table_data.pop(0)   # Pop First Item - Contain Nothing

            for date,status,place in table_data:
                print("\nStatus: ", status)
                print("Place: ", place)
                print("Date: ", date)

        else:
            print("\nStatus: Tracking Not Found")

    else:
        print("Wrong Format!")
    
    exit()


main()