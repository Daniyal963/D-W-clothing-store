from flask import render_template,url_for,flash,redirect,request,abort,jsonify,session  #request is imported for query parameters in routes
from tailorweb import app,db,bcrypt,admin,mail
from tailorweb.models import *
from tailorweb.forms import *
from flask_login import login_user,current_user,logout_user,login_required
from flask_mail import Message
from functools import wraps
import os
import random
import secrets
from PIL import Image
import datetime
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView,expose,AdminIndexView
import pytz
from operator import itemgetter
from shutil import copy2
import copy
import json
import calendar as cal
from werkzeug.datastructures import ImmutableMultiDict
import ast
# from validate_email import validate_email


#-----------------------------------------------------------------------------------------------------------------------#
###########################                       MISC FUNCS                       ###################################
#-----------------------------------------------------------------------------------------------------------------------#

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if ((current_user.role != role) and (role != "ANY")):


                return redirect(url_for('unauthorized'))
            return fn(*args, **kwargs)


        return decorated_view


    return wrapper

@app.route('/test',methods=['GET','POST'])
def test():
    return render_template('test.html')

@app.route('/unauthorized',methods=['GET','POST'])
def unauthorized():
    if current_user.role == 'ADMIN':
        page = 'home'
    elif current_user.role == 'CUSTOMER':
        page = 'home'
    return render_template('unauthorized.html',page=page)




def save_picture(form_picture,path):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename) #form_picture is form data, filename will be the name of that file
    picture_fn = random_hex+f_ext
    picture_path = os.path.join(path,picture_fn) #this will get the path of the root directory of the package
    output_size = (800,800)
    i = Image.open(form_picture)
    i.thumbnail(output_size)



    i.save(picture_path) #this will save the picture in the path

    return picture_fn


#-----------------------------------------------------------------------------------------------------------------------#
###########################                       HOME PAGE                       ###################################
#-----------------------------------------------------------------------------------------------------------------------#
@app.route('/')
@app.route('/home')
def home():
    women_shop_now = Category.query.get(6),Category.query.get(9),Category.query.get(11)
    men_shop_now = Category.query.get(3),Category.query.get(4),Category.query.get(5)
    return render_template('home.html',women_shop_now=women_shop_now,men_shop_now=men_shop_now)





@app.route('/loginreg',methods=['GET','POST'])
def loginreg():
    if current_user.is_authenticated:
        if current_user.role == 'ADMIN':
            return redirect(url_for('home'))
        elif current_user.role == 'CUSTOMER':
            return redirect(url_for('home'))

    return render_template('loginreg.html')


@app.route('/design')
def design():
    if not current_user.is_authenticated:
        return redirect(url_for('loginreg'))
    designs = Design
    design_image = DesignImage
    designs_js = Design.return_all_obj()
    design_image_js = DesignImage.return_all_obj()
    desing_cat_id = Category.query.filter_by(name='design')[0].id

    sizes = Categorysize.query.filter_by(category_id=desing_cat_id)
    sizes_ids = [x.id for x in sizes]
    sizes_js = {}

    for k,v in Categorysize.return_all_obj().items():
        if k in sizes_ids:
            sizes_js[k]=v

    products = Product.query.filter_by(name='Design')
    products_ids = [x.id for x in products]
    products_js = {}
    for k,v in Product.return_all_obj().items():
        if k in products_ids:
            products_js[k]=v


    print(design_image_js)
    return render_template('design.html',designs=designs,design_image=design_image,designs_js=designs_js,design_image_js=design_image_js,sizes=sizes,sizes_js=sizes_js,products=products,products_js=products_js)


@app.route('/account')
def account():
    customers = Customer
    order = Order.query.all()
    products = Product
    orders = []
    for each in order:
        if each.customer_id==current_user.id:
            orders.append(each)
    return render_template('account.html',customers=customers,orders=orders,products=products)
#-----------------------------------------------------------------------------------------------------------------------#
###########################                       Login Register                      ###################################
#-----------------------------------------------------------------------------------------------------------------------#


@app.route('/loginver',methods=['GET','POST'])
def loginver():
    session['shoppingcart']=[]
    session['total'] = 0
    data = dict(request.form)
    email, password = data['email'], data['password']

    if email!='' and password!='':


        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            if email==user.email and password==user.password and user.role=='CUSTOMER':

                login_user(user)
                return jsonify({'val': True,'route':'home'})
            elif email==user.email and password==user.password and user.role=='ADMIN':
                login_user(user)
                return jsonify({'val':True,'route':'admin_panel'})

        else:
            print('hereeee')
            return jsonify({'val': 'You are not yet registered! Please register first!'})

    return jsonify({'val': 'Hmm, Something unexpected has happened. Try again.'})

@app.route('/regver',methods=['GET','POST'])
def regver():
    data = dict(request.form)
    fname,lname,address,phonenum,email,password = data['fname'],data['lname'],data['add'],data['pnum'],data['email'],data['password']
    if fname!='' and lname!='' and address!='' and phonenum!='' and email!='' and password!='':
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'val': 'Account already registered. Please login'})
        else:

            user = User(first_name = fname, last_name = lname,email=email,password=password,role='CUSTOMER')

            customer = Customer(first_name = fname, last_name = lname, email = email, password = password, address = address, phone = phonenum)

            db.session.add(user)
            db.session.add(customer)
            db.session.commit()
            customer.id = user.id
            db.session.commit()
            return jsonify({'val': 'Registered successfully, please login now :)'})



    return jsonify({'val': 'Hmm, Something unexpected has happened. Try again.'})

@app.route("/logout")
def logout():
    session['shoppingcart']=[]
    session['total'] = 0
    logout_user()
    return redirect(url_for('home'))

#-----------------------------------------------------------------------------------------------------------------------#
###########################                       Product-Order                      ###################################
#-----------------------------------------------------------------------------------------------------------------------#

@app.route("/productview/<product_type>")
def productview(product_type):
    if product_type=='men':
        title = 'For Men'
        categories_js = Category.return_filtered_js('male')
        products_js = Product.return_filtered_js('male')
        prod_pics_js = ProductPics.return_all_obj()
        categories_size_js = Categorysize.return_all_obj()

        categories = Category.return_filtered('male')
        products = Product.return_filtered('male')
        prod_pics = ProductPics.query.all()
        categories_size = Categorysize.query.all()

    elif product_type=='women':
        title = 'For Women'
        categories_js = Category.return_filtered_js('female')
        products_js = Product.return_filtered_js('female')
        prod_pics_js = ProductPics.return_all_obj()
        categories_size_js = Categorysize.return_all_obj()

        categories = Category.return_filtered('female')
        products = Product.return_filtered('female')
        prod_pics = ProductPics.query.all()
        categories_size = Categorysize.query.all()
    elif product_type=='popular':
        title = 'Our Popular Designs'
        categories_js = ['popular','male','female']
        products_js = Product.return_filtered_popular_js()
        prod_pics_js = ProductPics.return_all_obj()
        categories_size_js = Categorysize.return_all_obj()

        categories = ['popular','male','female']
        products = Product.return_filtered_popular()
        prod_pics = ProductPics.query.all()
        categories_size = Categorysize.query.all()
    elif product_type=='winter':
        title = 'Exclusive Winter Collection'
        categories_js = Category.return_filtered_name_js('winter')
        products_js = Product.return_filtered_name_js('winter')
        prod_pics_js = ProductPics.return_all_obj()
        categories_size_js = Categorysize.return_all_obj()

        categories = Category.return_filtered_name('winter')+['male','female']
        products = Product.return_filtered_name('winter')
        prod_pics = ProductPics.query.all()
        categories_size = Categorysize.query.all()
    else:
        title = ''
    # print(products_js.keys())
    # print(categories_js.keys())
    # print(products)
    # print(categories)

    return render_template('productview.html',title=title,categories_js=categories_js,products_js=products_js,prod_pics_js=prod_pics_js,categories_size_js=categories_size_js,categories=categories,products=products,prod_pics=prod_pics,categories_size=categories_size)

@app.route("/product/<product_id>")
def product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    product_pics = ProductPics.query.filter_by(product_id=product_id).all()
    sizes = Category.query.filter_by(id=ProductCategory.query.filter_by(product_id=product_id).all()[0].category_id).all()[0].sizes

    return render_template('product.html',product=product,product_pics=product_pics,sizes=sizes)

#-----------------------------------------------------------------------------------------------------------------------#
###########################                      Cart Logic                      ###################################
#-----------------------------------------------------------------------------------------------------------------------#

@login_required(role='CUSTOMER')
@app.route('/addtocart',methods=['GET','POST'])
def addtocart():
    print("Product Details : ")
    data = dict(request.form)
    print(data['prodid'])
    print(data['quantity'])
    print(data['size'])


    #Adding item to cart
    print(session)
    if 'shoppingcart' in session.keys():
        if {'prodid':data['prodid'],'quantity':data['quantity'],'size':data['size']} not in session['shoppingcart']:
            session['shoppingcart'].append({'prodid':data['prodid'],'quantity':data['quantity'],'size':data['size']})
            session['total'] += (int(Product.query.get(data['prodid']).price) * int(data['quantity']))
            session.modified = True

        else:
            pass
    else:
        session['shoppingcart']=[{'prodid':data['prodid'],'quantity':data['quantity'],'size':data['size']}]
        session['total'] = (int(Product.query.get(data['prodid']).price) * int(data['quantity']))
    print(session)

    return url_for('cart')
@login_required(role='CUSTOMER')
@app.route('/deletefromcart',methods=['GET','POST'])
def deletefromcart():
    data = dict(request.form)
    prod_id = data['prodid']
    to_remove = None
    for each in session['shoppingcart']:
        if int(each['prodid'])==int(prod_id):
            to_remove = each
    price = Product.query.get(int(prod_id)).price
    quant = int(to_remove['quantity'])
    session['shoppingcart'].remove(to_remove)
    session['total']-=(int(price)*quant)
    session.modified = True


    return jsonify({'price':session['total']})

#-----------------------------------------------------------------------------------------------------------------------#
###########################                       Order-Cart-Page                      ###################################
#-----------------------------------------------------------------------------------------------------------------------#

@login_required(role='CUSTOMER')
@app.route("/cart",methods=['GET','POST'])
def cart():
    categories_js = Category.return_all_obj()
    products_js = Product.return_all_obj()
    prod_pics_js = ProductPics.return_all_obj()
    categories_size_js = Categorysize.return_all_obj()

    categories = Category
    products = Product
    prod_pics = ProductPics
    categories_size = Categorysize


    customers = Customer
    return render_template('cart.html',categories_js=categories_js,products_js=products_js,prod_pics_js=prod_pics_js,categories_size_js=categories_size_js,categories=categories,products=products,prod_pics=prod_pics,categories_size=categories_size,customers=customers)

@login_required(role='CUSTOMER')
@app.route("/placeorder",methods=['GET','POST'])
def placeorder():
    data = dict(request.form)
    order = Order(customer_id=current_user.id,date=datetime.datetime.today().date(),status='Pending',total_price=session['total'],address_first=data['address-input-1'],address_second=data['address-input-2'],phone_first=data['telephone-1'],phone_second=data['telephone-2'],credit_card_num=data['credit-card-no'],credit_card_exp=data['credit-card-exp'],credit_card_name=data['credit-card-ccv'])
    db.session.add(order)
    db.session.commit()
    for each in range(len(session['shoppingcart'])):
        order_item = OrderItem(product_id=session['shoppingcart'][each]['prodid'],order_id=order.id,quantity=session['shoppingcart'][each]['quantity'],size_id=session['shoppingcart'][each]['size'])
        db.session.add(order_item)
        db.session.commit()


    cust = Customer.query.filter_by(id=current_user.id)[0]
    if not cust.credit_card_num:
        cust.credit_card_num = data['credit-card-no']
        cust.credit_card_exp = data['credit-card-exp']
        cust.credit_card_cvv = data['credit-card-ccv']
    db.session.commit()
    del session['shoppingcart']
    del session['total']
    session.modified=True
    return redirect(url_for('account'))

#-----------------------------------------------------------------------------------------------------------------------#
###########################                       Admin Panel                      ###################################
#-----------------------------------------------------------------------------------------------------------------------#

@login_required(role='ADMIN')
@app.route('/admin_panel',methods=['GET','POST'])
def admin_panel():
    categories_js = Category.return_all_obj()
    products_js = Product.return_all_obj()
    prod_pics_js = ProductPics.return_all_obj()
    categories_size_js = Categorysize.return_all_obj()
    orders_js = Order.return_all_obj()
    order_items_js = OrderItem.return_all_obj()
    design_js = Design.return_all_obj()
    design_images_js = DesignImage.return_all_obj()
    customers_js = Customer.return_all_obj()

    categories = Category
    products = Product
    prod_pics = ProductPics
    categories_size = Categorysize
    orders = Order
    order_items = OrderItem
    designs = Design
    design_images = DesignImage
    customers = Customer

    return render_template('admin-panel.html',categories_js=categories_js,products_js=products_js,prod_pics_js=prod_pics_js,categories_size_js=categories_size_js,orders_js=orders_js,order_items_js=order_items_js,design_js=design_js,design_images_js=design_images_js,customers_js=customers_js,
                           categories=categories,products=products,prod_pics=prod_pics,categories_size=categories_size,orders=orders,order_items=order_items,designs=designs,design_images=design_images,customers=customers)



@login_required(role='ADMIN')
@app.route('/addcategory',methods=['GET','POST'])
def addcategory():
    data = dict(request.form)
    name = data['category-name']
    gender = data['category-gender']
    desc = data['category-description']
    sizes = request.form.getlist('options-selected')
    imagefile = request.files.get('image-category', '')
    image = save_picture(imagefile, app.root_path + '/static/html_pics')

    category = Category(name=name.lower(),gender=gender.lower(),description=desc.title(),pic=image)
    db.session.add(category)
    db.session.commit()
    for each in sizes:
        db.session.add(Categorysize(category_id=category.id,size=each))
        db.session.commit()

    return redirect(url_for('admin_panel'))


@login_required(role='ADMIN')
@app.route('/addproduct',methods=['GET','POST'])
def addproduct():



    data = dict(request.form)

    name = data['product-name']
    pop = data['product-popular']
    if pop.lower()=='true':
        pop = True
    else:
        pop = False

    desc = data['product-description']
    price = data['product-price']
    categories = request.form.getlist("product-category")
    pics = request.files.getlist("product-images")
    pictures = []
    for img in pics:
        pictures.append(save_picture(img, app.root_path + '/static/html_pics'))
    image = request.files.get('product-main-image', '')
    image = save_picture(image,app.root_path + '/static/html_pics')




    product = Product(name=name.title(),popular=pop,description=desc.title(),price=price,main_image=image)
    db.session.add(product)
    db.session.commit()
    for each in categories:
        prodcat = ProductCategory(category_id=int(each),product_id=product.id)
        db.session.add(prodcat)
        db.session.commit()
    for each in pictures:
        prodpic = ProductPics(product_id=product.id,pic=each.split('\\')[-1])
        db.session.add(prodpic)
        db.session.commit()


    return redirect(url_for('admin_panel'))

@login_required(role='ADMIN')
@app.route('/editproduct',methods=['GET','POST'])
def editproduct():
    data = request.form.getlist("data[]")

    prod_id = int(data[0])
    prod_name = data[1]
    prod_description = data[2]
    prod_price = data[3].split()[1]
    prod_popular = data[4]
    if prod_popular=='False':
        prod_popular=False
    else:
        prod_popular=True

    product = Product.query.get(prod_id)
    product.price=prod_price
    product.name = prod_name
    product.description = prod_description
    product.popular = prod_popular
    db.session.add(product)
    db.session.commit()
    return jsonify({'val':True})

@login_required(role='ADMIN')
@app.route('/deleteproduct',methods=['GET','POST'])
def deleteproduct():
    data = dict(request.form)
    id = int(data['data'])
    print(id)
    ProductPics.query.filter_by(product_id=id).delete()
    ProductCategory.query.filter_by(product_id=id).delete()
    OrderItem.query.filter_by(product_id=id).delete()
    Product.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'val':True})



@login_required(role='ADMIN')
@app.route('/editcategory',methods=['GET','POST'])
def editcategory():
    data = request.form.getlist("data[]")
    id = int(data[0])
    name = data[1]
    gender = data[2]
    description = data[3]

    category = Category.query.get(id)
    category.name = name
    category.gender = gender.lower()
    category.description=description
    db.session.add(category)
    db.session.commit()
    return jsonify({'val':True})


@login_required(role='ADMIN')
@app.route('/deletecategory',methods=['GET','POST'])
def deletecategory():
    data = dict(request.form)
    id = int(data['data'])
    print(id)
    Categorysize.query.filter_by(category_id=id).delete()
    ProductCategory.query.filter_by(category_id=id).delete()
    Category.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'val':True})


@login_required(role='ADMIN')
@app.route('/editorder',methods=['GET','POST'])
def editorder():
    data = request.form.getlist("data[]")
    id = int(data[0])
    status = data[1]
    order = Order.query.get(id)
    order.status = status
    db.session.add(order)
    db.session.commit()
    return jsonify({'val':True})