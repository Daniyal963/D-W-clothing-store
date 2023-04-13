from tailorweb import *
from tailorweb.models import *
db.drop_all()
db.create_all()

user = User(id=1,first_name='admin',last_name='admin',email='admin',password='admin',role='ADMIN')
db.session.add(user)
db.session.commit()

cat1 = Category(id=1,name='Basic',gender='female',description='Basics are all what you want for a university wear, office wear, formal meeting and even at a formal event but all what you have to do is to pair it with a nice jewelry, formal stilettos and also a bold lip color won’t go wrong with it. At D&W, we also have wide range of kurtas that you can mix-n-match with different bottoms to create your own look. Straight-cut, flared, short or asymmetrical, we have everything you want. Shop for the stunning range of bottom wear and club it with your choice of top wear to get the desired look.',pic='logreg3.jpg')
db.session.add(cat1)
size1 = [db.session.add(Categorysize(id=1,category_id=1,size='XS')),db.session.add(Categorysize(id=2,category_id=1,size='S')),db.session.add(Categorysize(id=3,category_id=1,size='M')),db.session.add(Categorysize(id=4,category_id=1,size='L')),db.session.add(Categorysize(id=5,category_id=1,size='XL'))]
db.session.commit()

cat2 = Category(id=2,name='Shirts',gender='female',description='Take on the latest trends in ladies’ shirts with this inspired collection. From classic, crisp white shirts to off-duty checked designs, explore the new season additions in shirts and blouses. Our runway inspired designs range from contemporary colors and oversized fits to intricat2e detailing and bold printed blouses. They can be very informal, with a t-shirt and blue jeans forming a basic ensemble, or it may consist of tailored formal garments with western accents.',pic='logreg3.jpg')
db.session.add(cat2)
size2 = [db.session.add(Categorysize(id=6,category_id=2,size='XS')),db.session.add(Categorysize(id=7,category_id=2,size='S')),db.session.add(Categorysize(id=8,category_id=2,size='M')),db.session.add(Categorysize(id=9,category_id=2,size='L')),db.session.add(Categorysize(id=10,category_id=2,size='XL'))]
db.session.commit()


cat3 = Category(id=3,name='Kurti',gender='female',description='Casual wear is all about simplicity and stylish comfort. Fabrics that are no fuss, soft and breathable are what you should be aiming for. Silk kurtis with skinny jeans or tights are fun options you can experiment with this season. Pair it up with some funky accessories and you’ve got a look like no other. You can pair your kurti with a jeans or a nice bottom wear and with a white color of sneakers. ',pic='logreg3.jpg')
db.session.add(cat3)
size3 = [db.session.add(Categorysize(id=11,category_id=3,size='XS')),db.session.add(Categorysize(id=12,category_id=3,size='S')),db.session.add(Categorysize(id=13,category_id=3,size='M')),db.session.add(Categorysize(id=14,category_id=3,size='L')),db.session.add(Categorysize(id=15,category_id=3,size='XL'))]
db.session.commit()


cat4 = Category(id=4,name='Churidars/Tights',gender='female',description="These are an evergreen bottom that can be clubbed with a variety of kurtas. Churidar plays an important role when it comes to traditional dressing and therefore, you just can't miss this must-have bottom. You can collect as many fashion bottoms as you want but nothing can beat the charm of churidars. While stitching, churidars are cut longer than the length of the leg so that the excess length falls loosely over the leg in ripples or folds. On the other hand, tights are ankle-length bottoms that can easily complement your casual as well as traditional look. Being comfortable & easy to wear, these are available in different shades and colors",pic='logreg3.jpg')
db.session.add(cat4)
size4 = [db.session.add(Categorysize(id=16,category_id=4,size='XS')),db.session.add(Categorysize(id=17,category_id=4,size='S')),db.session.add(Categorysize(id=18,category_id=4,size='M')),db.session.add(Categorysize(id=19,category_id=4,size='L')),db.session.add(Categorysize(id=20,category_id=4,size='XL'))]
db.session.commit()

cat5 = Category(id=5,name='Embroided',gender='female',description='Embroidery is the craft of decorating fabric or other materials using a needle to apply thread or yarn. Embroidery may also incorporate other materials such as pearls, beads, quills, and sequins.Embroidery can also be classified by the similarity of appearance. In drawn thread work and cutwork, the foundation fabric is deformed or cut away to create holes that are then embellished with embroidery, often with thread in the same color as the foundation fabric.',pic='logreg3.jpg')
db.session.add(cat5)
size5 = [db.session.add(Categorysize(id=21,category_id=5,size='XS')),db.session.add(Categorysize(id=22,category_id=5,size='S')),db.session.add(Categorysize(id=23,category_id=5,size='M')),db.session.add(Categorysize(id=24,category_id=5,size='L')),db.session.add(Categorysize(id=25,category_id=5,size='XL'))]
db.session.commit()





p1 = Product(id=1,name='Product Sample 1',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p1)
p1pics = [db.session.add(ProductPics(id=1,product_id=1,pic='embroidered.jpg')),db.session.add(ProductPics(id=2,product_id=1,pic='embroidered.jpg')),db.session.add(ProductPics(id=3,product_id=1,pic='embroidered.jpg')),db.session.add(ProductPics(id=4,product_id=1,pic='embroidered.jpg'))]
db.session.commit()
p1cat = [db.session.add(ProductCategory(id=1,product_id=1,category_id=5)),db.session.add(ProductCategory(id=2,product_id=1,category_id=3))]
db.session.commit()

p2 = Product(id=2,name='Product Sample 2',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p2)
p2pics = [db.session.add(ProductPics(product_id=2,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=2,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=2,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=2,pic='embroidered.jpg'))]
db.session.commit()
p2cat = [db.session.add(ProductCategory(product_id=2,category_id=5)),db.session.add(ProductCategory(product_id=2,category_id=3))]
db.session.commit()

p3 = Product(id=3,name='Product Sample 3',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p3)
p3pics = [db.session.add(ProductPics(product_id=3,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=3,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=3,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=3,pic='embroidered.jpg'))]
db.session.commit()
p3cat = [db.session.add(ProductCategory(product_id=3,category_id=5)),db.session.add(ProductCategory(product_id=3,category_id=3))]
db.session.commit()




p4 = Product(id=4,name='Product Sample 4',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p4)
p4pics = [db.session.add(ProductPics(product_id=4,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=4,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=4,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=4,pic='embroidered.jpg'))]
db.session.commit()
p4cat = [db.session.add(ProductCategory(product_id=4,category_id=5)),db.session.add(ProductCategory(product_id=4,category_id=3))]
db.session.commit()


p5 = Product(id=5,name='Product Sample 5',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p5)
p5pics = [db.session.add(ProductPics(product_id=5,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=5,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=5,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=5,pic='embroidered.jpg'))]
db.session.commit()
p5cat = [db.session.add(ProductCategory(product_id=5,category_id=5)),db.session.add(ProductCategory(product_id=5,category_id=3))]
db.session.commit()

p6 = Product(id=6,name='Product Sample 6',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p6)
p6pics = [db.session.add(ProductPics(product_id=6,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=6,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=6,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=6,pic='embroidered.jpg'))]
db.session.commit()
p6cat = [db.session.add(ProductCategory(product_id=6,category_id=1)),db.session.add(ProductCategory(product_id=6,category_id=2))]
db.session.commit()


p7 = Product(id=7,name='Product Sample 7',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p7)
p7pics = [db.session.add(ProductPics(product_id=7,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=7,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=7,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=7,pic='embroidered.jpg'))]
db.session.commit()
p7cat = [db.session.add(ProductCategory(product_id=7,category_id=1)),db.session.add(ProductCategory(product_id=7,category_id=2))]
db.session.commit()



p8 = Product(id=8,name='Product Sample 8',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p8)
p8pics = [db.session.add(ProductPics(product_id=8,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=8,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=8,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=8,pic='embroidered.jpg'))]
db.session.commit()
p8cat = [db.session.add(ProductCategory(product_id=8,category_id=1)),db.session.add(ProductCategory(product_id=8,category_id=2))]
db.session.commit()


p9 = Product(id=9,name='Product Sample 9',description='This is a sample product and bla blab lab laba lbalba',price='2,900',main_image='embroidered.jpg',popular=False)
db.session.add(p9)
p9pics = [db.session.add(ProductPics(product_id=9,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=9,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=9,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=9,pic='embroidered.jpg'))]
db.session.commit()
p9cat = [db.session.add(ProductCategory(product_id=9,category_id=1)),db.session.add(ProductCategory(product_id=9,category_id=2))]
db.session.commit()

p10 = Product(id=10,name='Product Sample 10',description='This is a sample product and bla blab lab laba lbalba',price='2,1000',main_image='embroidered.jpg',popular=False)
db.session.add(p10)
p10pics = [db.session.add(ProductPics(product_id=10,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=10,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=10,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=10,pic='embroidered.jpg'))]
db.session.commit()
p10cat = [db.session.add(ProductCategory(product_id=10,category_id=1)),db.session.add(ProductCategory(product_id=10,category_id=2))]
db.session.commit()

p11 = Product(id=11,name='Product Sample 11',description='This is a sample product and bla blab lab laba lbalba',price='2,1100',main_image='embroidered.jpg',popular=False)
db.session.add(p11)
p11pics = [db.session.add(ProductPics(product_id=11,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=11,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=11,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=11,pic='embroidered.jpg'))]
db.session.commit()
p11cat = [db.session.add(ProductCategory(product_id=11,category_id=4)),db.session.add(ProductCategory(product_id=11,category_id=5))]
db.session.commit()

p12 = Product(id=12,name='Product Sample 12',description='This is a sample product and bla blab lab laba lbalba',price='2,1200',main_image='embroidered.jpg',popular=False)
db.session.add(p12)
p12pics = [db.session.add(ProductPics(product_id=12,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=12,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=12,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=12,pic='embroidered.jpg'))]
db.session.commit()
p12cat = [db.session.add(ProductCategory(product_id=12,category_id=4)),db.session.add(ProductCategory(product_id=12,category_id=5))]
db.session.commit()

p13 = Product(id=13,name='Product Sample 13',description='This is a sample product and bla blab lab laba lbalba',price='2,1300',main_image='embroidered.jpg',popular=False)
db.session.add(p13)
p13pics = [db.session.add(ProductPics(product_id=13,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=13,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=13,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=13,pic='embroidered.jpg'))]
db.session.commit()
p13cat = [db.session.add(ProductCategory(product_id=13,category_id=4)),db.session.add(ProductCategory(product_id=13,category_id=5))]
db.session.commit()

p14 = Product(id=14,name='Product Sample 14',description='This is a sample product and bla blab lab laba lbalba',price='2,1400',main_image='embroidered.jpg',popular=False)
db.session.add(p14)
p14pics = [db.session.add(ProductPics(product_id=14,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=14,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=14,pic='embroidered.jpg')),db.session.add(ProductPics(product_id=14,pic='embroidered.jpg'))]
db.session.commit()
p14cat = [db.session.add(ProductCategory(product_id=14,category_id=4)),db.session.add(ProductCategory(product_id=14,category_id=5))]
db.session.commit()







