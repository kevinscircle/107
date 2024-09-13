from flask import Flask , request    # request needed for post api 
import json
from config import db   # import db from file 
# __name__  --> there is two on each side   
app = Flask(__name__)    # app is the name of the project folder 107 using the __name__ 


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
  
    return json.dumps(products)

# post
@app.post("/api/products")
def save_products():
    item = request.get_json() # json into python

    #products.append(item)
    db["products"].insert_one(item)
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






app.run(debug=True)  # has to be at the end of page !!!!!