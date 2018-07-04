from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
import os
import difflib

# req = Request('https://thehimalayantimes.com/world/iran-urges-muslims-to-develop-sciences-to-shake-off-us-hegemony/', headers={'User-Agent': 'Mozilla/5.0'})
# urlopen(req).read()
# html = urlopen(req).read()
# #html = urlopen("www..").read()

# soup = BeautifulSoup(html)
# myTitle = soup.html.head.title


# for each in range(0,10):
#     paragraph = soup.find('p').getText()
#     print(paragraph)

# print(myTitle)
os.system("chcp 65001")

ratio = difflib.SequenceMatcher(None, "hello ani ke cha ta jane haina ta usa ho ki newzealand huh broo ahhah ", "ke")
print(ratio.ratio())