from tailorweb import db,login_manager,app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)


    def return_dict(self):
        user_dict = {
            'id' : self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            }


        return user_dict

    @classmethod
    def return_all_obj(cls):
        users_dict = {}
        for user in User.query.all():
            users_dict[user.id] = user.return_dict()
        return users_dict


class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(500),nullable=False)
    phone = db.Column(db.String(20),nullable=False)
    credit_card_num = db.Column(db.String(20), nullable=True)
    credit_card_exp = db.Column(db.String(10), nullable=True)
    credit_card_name = db.Column(db.String(20), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)

    def return_dict(self):
        customer_dict = {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email,
            'password':self.password,
            'address':self.address,
            'phone':self.phone,
            'credit_card_num': 'None' if self.credit_card_num == None else self.credit_card_num,
            'credit_card_exp': 'None' if self.credit_card_exp == None else self.credit_card_exp,
            'credit_card_name': 'None' if self.credit_card_name == None else self.credit_card_name,
            'zip_code': 'None' if self.zip_code == None else self.zip_code
        }
        return customer_dict

    @classmethod
    def return_all_obj(cls):
        customers_dict = {}
        for cust in Customer.query.all():
            customers_dict[cust.id]=cust.return_dict()
        return customers_dict

    def __repr__(self):
        return "({},{})".format(str(self.id), self.first_name+" "+self.last_name)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(1000),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    main_image = db.Column(db.String(100), nullable=False, default='default.jpg')
    popular = db.Column(db.Boolean,default=False)
    pics = db.relationship('ProductPics', backref='product', lazy=True)
    categories = db.relationship('ProductCategory', backref='product', lazy=True)
    orders = db.relationship('OrderItem', backref='product', lazy=True)

    def return_dict(self):
        product_dict = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'main_image': self.main_image,
            'popular': 'false' if self.popular==False else 'true',
            'pics':[pic.return_dict() for pic in self.pics],
            'categories':[category.return_dict() for category in self.categories],
            'orders':[order.return_dict() for order in self.orders]
        }

        return product_dict

    def return_gender(self):
        gender = ''
        for each in self.categories:
            if Category.query.get(each.category_id).gender.lower()=='male' or Category.query.get(each.category_id).gender.lower()=='female':
                gender=Category.query.get(each.category_id).gender
                break
        return gender

    @classmethod
    def return_filtered(cls, gender):
        product_list = []
        for each in Product.query.all():
            categories = each.categories
            for each2 in categories:
                cat = Category.query.filter_by(id=each2.category_id).all()[0]
                if cat.gender == gender.lower():
                    product_list.append(each)
                    break
        return product_list

    @classmethod
    def return_filtered_js(cls,gender):
        product_list = []
        for each in Product.query.all():
            categories = each.categories
            for each2 in categories:
                cat = Category.query.filter_by(id=each2.category_id).all()[0]

                if cat.gender==gender.lower():
                    product_list.append(each)
        products_dict = {}
        for prod in product_list:
            products_dict[prod.id] = prod.return_dict()
        return products_dict

    @classmethod
    def return_filtered_name(cls, name):
        product_list = []
        for each in Product.query.all():
            categories = each.categories
            for each2 in categories:
                cat = Category.query.filter_by(id=each2.category_id).all()[0]
                if cat.name == name.lower():
                    product_list.append(each)
                    break
        return product_list

    @classmethod
    def return_filtered_name_js(cls, name):
        product_list = []
        for each in Product.query.all():
            categories = each.categories
            for each2 in categories:
                cat = Category.query.filter_by(id=each2.category_id).all()[0]

                if cat.name == name.lower():
                    product_list.append(each)
        products_dict = {}
        for prod in product_list:
            products_dict[prod.id] = prod.return_dict()
        return products_dict

    @classmethod
    def return_filtered_popular(cls):
        product_list = []
        for each in Product.query.all():
            if each.popular:
                product_list.append(each)
        return product_list

    @classmethod
    def return_filtered_popular_js(cls):
        product_list = []
        for each in Product.query.all():
            if each.popular:
                product_list.append(each)
        products_dict = {}
        for prod in product_list:
            products_dict[prod.id] = prod.return_dict()
        return products_dict

    @classmethod
    def return_all_obj(cls):
        products_dict = {}
        for prod in Product.query.all():
            products_dict[prod.id] = prod.return_dict()
        return products_dict

class ProductPics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    pic = db.Column(db.String(100), nullable=False, default='default.jpg')

    def return_dict(self):
        productpic_dict = {
            'id': self.id,
            'product_id': self.product_id,
            'pic': self.pic
        }

        return productpic_dict

    @classmethod
    def return_all_obj(cls):
        productspics_dict = {}
        for pic in Product.query.all():
            productspics_dict[pic.id] = pic.return_dict()
        return productspics_dict


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    pic = db.Column(db.String(100),nullable=False)
    sizes = db.relationship('Categorysize',backref='category',lazy=True)
    products = db.relationship('ProductCategory',backref='category',lazy=True)

    def return_dict(self):
        category_dict = {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'description': self.description,
            'pic':self.pic,
            'sizes':[size.return_dict() for size in self.sizes],
            'products':[product.return_dict() for product in self.products]
        }

        return category_dict

    @classmethod
    def return_filtered(cls, gender):
        return cls.query.filter_by(gender=gender).all()

    @classmethod
    def return_filtered_js(cls, gender):
        categories_dict = {}
        for cat in cls.query.filter_by(gender=gender):
            categories_dict[cat.id] = cat.return_dict()
        return categories_dict

    @classmethod
    def return_filtered_name(cls, name):
        return cls.query.filter_by(name=name).all()

    @classmethod
    def return_filtered_name_js(cls, name):
        categories_dict = {}
        for cat in cls.query.filter_by(name=name):
            categories_dict[cat.id] = cat.return_dict()
        return categories_dict

    @classmethod
    def return_all_obj(cls):
        categories_dict = {}
        for cat in Category.query.all():
            categories_dict[cat.id] = cat.return_dict()
        return categories_dict




class Categorysize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    size = db.Column(db.String(5),nullable=False)
    orders = db.relationship('OrderItem',backref='size',lazy=True)
    def return_dict(self):
        category_size = {
            'id': self.id,
            'category_id': self.category_id,
            'size': self.size,
            'orders':[order.return_dict() for order in self.orders]
        }

        return category_size


    @classmethod
    def return_all_obj(cls):
        categorysizes_dict = {}
        for catsize in Categorysize.query.all():
            categorysizes_dict[catsize.id] = catsize.return_dict()
        return categorysizes_dict

class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def return_dict(self):
        productcategory_dict = {
            'id': self.id,
            'product_id': self.product_id,
            'category_id': self.category_id
        }

        return productcategory_dict

    @classmethod
    def return_all_obj(cls):
        productcategories_dict = {}
        for prodcat in ProductCategory.query.all():
            productcategories_dict[prodcat.id] = prodcat.return_dict()
        return productcategories_dict


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20),nullable=False)
    total_price = db.Column(db.Integer, nullable=True)
    address_first = db.Column(db.String(500),nullable=True)
    address_second = db.Column(db.String(500),nullable=True)
    phone_first = db.Column(db.String(20),nullable=True)
    phone_second = db.Column(db.String(20),nullable=True)
    credit_card_num = db.Column(db.String(20),nullable=True)
    credit_card_exp = db.Column(db.String(10),nullable=True)
    credit_card_name = db.Column(db.String(20), nullable=True)
    zip_code = db.Column(db.String(10),nullable=True)
    items = db.relationship('OrderItem',backref='order',lazy=True)

    def return_dict(self):
        order_dict = {
            'id':self.id,
            'customer_id':self.customer_id,
            'date':self.date,
            'status':self.status,
            'total_price':'None' if self.total_price==None else self.total_price,
            'address_first':'None' if self.address_first==None else self.address_first,
            'address_second':'None' if self.address_second==None else self.address_second,
            'phone_first':'None' if self.phone_first==None else self.phone_first,
            'phone_second':'None' if self.phone_second==None else self.phone_second,
            'credit_card_num':'None' if self.credit_card_num==None else self.credit_card_num,
            'credit_card_exp':'None' if self.credit_card_exp==None else self.credit_card_exp,
            'credit_card_name':'None' if self.credit_card_name==None else self.credit_card_name,
            'zip_code':'None' if self.zip_code==None else self.zip_code,
            'items':[item.return_dict() for item in self.items]
        }
        return order_dict

    @classmethod
    def return_all_obj(cls):
        orders_dict = {}
        for order in Order.query.all():
            orders_dict[order.id] = order.return_dict()
        return orders_dict


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    quantity = db.Column(db.Integer,default=1)
    size_id = db.Column(db.Integer,db.ForeignKey('categorysize.id'),nullable=True)

    def return_dict(self):
        orderitem_dict = {
            'id': self.id,
            'product_id': self.product_id,
            'order_id': self.order_id,
            'quantity': self.quantity,
            'size_id': self.size_id
        }

        return orderitem_dict

    @classmethod
    def return_all_obj(cls):
        orderitems_dict = {}
        for orderitem in OrderItem.query.all():
            orderitems_dict[orderitem.id] = orderitem.return_dict()
        return orderitems_dict


class Design(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    code = db.Column(db.String(),nullable=False)
    name = db.Column(db.String(500),nullable=False)
    type = db.Column(db.String(20),nullable=False)
    image = db.Column(db.String(100),nullable=False)

    def return_dict(self):
        design_dict = {
            'id': self.id,
            'code':self.code,
            'name': self.name,
            'type': self.type,
            'image': self.image
        }

        return design_dict

    @classmethod
    def return_all_obj(cls):
        designs_dict = {}
        for design in Design.query.all():
            designs_dict[design.id] = design.return_dict()
        return designs_dict


class DesignImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def return_dict(self):
        designimage_dict = {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'image': self.image
        }

        return designimage_dict

    @classmethod
    def return_all_obj(cls):
        designimage_dict = {}
        for design in DesignImage.query.all():
            designimage_dict[design.code] = design.return_dict()
        return designimage_dict

