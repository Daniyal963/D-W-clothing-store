import os
import sqlite3
from shutil import copy
from tailorweb import *
from tailorweb.models import *
import random

path = r'C:\\Users\\EliteBook 8770w i7\\Desktop\\Semester 5\\Web Designing And Development\\Project\\Final svgs'


conn = sqlite3.connect('site.db')
c = conn.cursor()
price = [2500,3500,8799,1255,4609,2244,5599,1100,1200,1900,2300,9999,5999,4999,3999,2999,1999,7999,6999,8999,9877,9234]
for root, dirs, files in os.walk(path):
    for file in files:
        # query = c.execute('INSERT INTO design_image (code,name,image) VALUES(?,?,?) ',
        #                   (file.split('.')[0],'Combination',file))
        # conn.commit()

        p1 = Product(name='Design', description=file.split('.')[0],
                     price=random.choice(price), main_image=file, popular=False)
        db.session.add(p1)

        db.session.commit()
        db.session.add(ProductCategory(product_id=p1.id, category_id=12))
        db.session.commit()


        # copy(os.path.join(root, file), os.getcwd()+"\\static\\data2\\")


#


##############Change viewport

# #36 36 200 200
# from bs4 import BeautifulSoup as BS
# path = r'C:\\Users\\EliteBook 8770w i7\\Desktop\\Semester 5\\Web Designing And Development\\Project\\OnlineTaylor\\tailorweb\\static\data2'
# c=0
# for root, dirs, files in os.walk(path):
#     for file in files:
#         with open(os.path.join(root, file),'r') as f:
#             text = f.read()
#         soup = BS(text,'lxml')
#         x = soup.find('svg',attrs={'xmlns':'http://www.w3.org/2000/svg'})
#         try:
#             v = x['viewbox']
#         except:
#             print(file)
