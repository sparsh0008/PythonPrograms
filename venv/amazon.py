from bs4 import BeautifulSoup
import urllib
import urllib.request
import os

def performScraping(urlReceived, folderName, number):
    count = 1
    page = urllib.request.urlopen(urlReceived)
    soup = BeautifulSoup(page, "html5lib")

    for image in soup.findAll('img'):
        if(count <= number):
            try:
                 count = count + 1
                 nameoffile = image.get('alt')
                 nameoffile = nameoffile.replace('/', '-')

                 img = image.get('src')
                 tempCheck = img.split('.')
                 check = str(tempCheck[len(tempCheck) - 1])

                 if (check == "jpg" or check == "jpeg" or check == "png"):
                     if (check == "jpg" or check == "jpeg"):
                         imagetype = ".jpeg"
                     else:
                         imagetype = ".png"
                 folderindividualname = "Images/" + folderName + "/"
                 if not os.path.exists(folderindividualname):
                     os.makedirs(folderindividualname)
                 imagefile = open(folderindividualname + nameoffile +imagetype ,'wb')
                 imagefile.write(urllib.request.urlopen(img).read())
                 imagefile.close()

                 print(tempCheck)
            except Exception as e:
                print("there is an error: {0}".format(repr(e)))
                continue



def getFolderName(wholeName):
    tempList = wholeName.split(" ")
    tempName = ""

    for i in range(1, len(tempList)):
        tempName = tempName + " " + tempList[i]

    return tempName

def main():
    std_url = "https://www.amazon.com/s?k="

    number = input("Enter the number of product images you want: ")
    product = input("Enter the product name: ")

    lines = [number + ' ' + product]

    folderName = getFolderName(lines[0])

    keywords = lines[0].split(" ")

    for j in range(1, len(keywords)):
        std_url = std_url + keywords[j] + '+'

    std_url = std_url[:-1]

    performScraping(std_url, folderName, int(number))

if __name__ == '__main__':
    main()
