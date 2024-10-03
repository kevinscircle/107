from flask import Flask , request    # request needed for post api 
import json
from config import db   # import db from file 
from flask_cors import CORS    # python3 -m pip install flask-cors



# __name__  --> there is two on each side   
app = Flask(__name__)    # app is the name of the project folder 107 using the __name__ 
CORS(app)  # warning disables CORS policy 

# get
@app.get("/")

def home():
    return  "Hello, form flask!"


@app.get("/about")
def about():
    me = {
        "name": "This is about page"
    }
    return json.dumps(me)

# get
# create api to footer that contains name of the page (anything i want )

@app.get("/section")
def section():
    page = {
        "name": "section page"
    }
    return json.dumps(page)




products = []

def fix_id(obj):
    obj['_id'] = str(obj["_id"])
    return obj

# get 
@app.get("/api/products")
def read_products():
    cursor = db.catalog.find({})
    catalog = []
    for prod in cursor:
        catalog.append(fix_id(prod))
  
    return json.dumps(catalog)

# post
@app.post("/api/products")
def save_products():
    item = request.get_json() # json into python

    #products.append(item)
    db["catalog"].insert_one(item)
    print(item)
    return json.dumps(fix_id(item))


# put update 
@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0 <= index < len(products):
        products[index] = update_item
        return json.dumps(update_item) # turns variable into json
    else: 
        return "That index does not exist"



######################    coupons  #####################





# get
@app.get("/api/coupons")
def read_coupons():
    cursor = db.coupons.find({})
    coupons = []
    for coup in cursor:
        coupons.append(fix_id(coup))
  
    return json.dumps(coupons)

# post 
@app.post("/api/coupons")
def save_coupons():
    item = request.get_json() # json into python

    #products.append(item)
    db["coupons"].insert_one(item)
    print(item)
    return json.dumps(fix_id(item))


# coupon structure 
# code - string 
# discount - number 

"""

{
"code:" "qwerty",
"discount": 10
}


"""









app.run(debug=True)  # has to be at the end of page !!!!!