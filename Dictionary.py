import re
import urllib.request
try:
    x="https://www.dictionary.com/browse/"
    print("                                 Dictionary!")
    y=input("Enter your word: ")
    x=x+y
    data = urllib.request.urlopen(x).read()
    data1 = data.decode("utf-8")
    m = re.search('meta name="description" content="',data1)
    start = m.end()
    end=start+150
    newStr=data1[start:end]
    m=re.search("See more.",newStr)
    end=m.start()-1
    definition=newStr[0:end]
    print(definition)
except:
    print("Sorry, your word is not in the dictionary...")
