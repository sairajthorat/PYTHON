from fastapi import FastAPI,Depends
from database import database_models
from database.db import session,engine
from sqlalchemy.orm import Session
from models.models import Product


app=FastAPI()


products=[
    Product(id=1,name="Dell",description="Dell Laptop",price=50000,quantity=55),
    Product(id=2,name="HP",description="Professional",price=65000,quantity=55),
    Product(id=3,name="Asus",description="gaming",price=100000,quantity=55),
    Product(id=4,name="Mac",description="Brand New",price=150000,quantity=55),
    Product(id=5,name="MI",description="Phone",price=15000,quantity=55)
]

"""products=[
    {"id":1,"name":"MOto","description":"Dell Laptop","price":50000,"quantity":55},
    {"id":2,"name":"Samsung","description":"Professional","price":65000,"quantity":55},
    {"id":3,"name":"Vivo","description":"gaming","price":100000,"quantity":55},
    {"id":4,"name":"Oppo","description":"Brand New","price":50000,"quantity":55},
    {"id":5,"name":"CSK","description":"Phone","price":15000,"quantity":55}
]
"""
database_models.Base.metadata.create_all(engine)
print("Created")

def init_db():
    db=session()
    count=db.query(database_models.Product).count()
    if count==0:
        print("Creating......")
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        print("Created")    
    else:
        print("Exist")
    db.commit()


init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/product")
def get_all(db : Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products


@app.post("/product")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product/{id}")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.id=product.id
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.price
        db.commit()
        return "Product updated"
    else:
        return "Product not Found"