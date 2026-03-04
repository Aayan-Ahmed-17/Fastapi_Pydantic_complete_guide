from fastapi import FastAPI

app = FastAPI()

#root get request
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

#hello get request
@app.get("/hello")
def say_hello():
    return {"message": "Hello, FastAPI!"}

#path parameter get request
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

#multiple path parameters get request
@app.get("/users/{user_id}/posts/{post_id}")
def read_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}

# query param get route dn
@app.get("/search/")
def search(keyword: str, page: int = 1, page_size: int = 10):
    """
    - keyword: required string to search for
    - page: optional page number, defaults to 1
    - page_size: optional results per page, defaults to 10
    """    
    return{
        "keyword": keyword,
        "page": page,
        "page_size": page_size
    }
    
# Real World Prodict Listing Analogy
@app.get("/products/")
def list_products(
    category: str,
    sort: str = "name",
    min_price: float = 0.0,
    max_price: float = 1000.0,
    in_stock: bool = True
):
    return {
        "category": category,
        "sort": sort,
        "min_price": min_price,
        "max_price": max_price,
        "in_stock": in_stock,
    }
    
# Combining Multiple Filters
@app.get("/filters/")
def advance_search(
    q: str,
    page: int = 1,
    page_size: int = 5,
    sort_by: str = "relevance",
    include_images: bool = True  
):
    """
    - q: required search term
    - page, page_size: pagination controls
    - sort_by: sort field ("relevance", "date", etc.)
    - include_images: whether to include image URLs in results
    """
    return{
        "q": q,
        "page": page,
        "page_size": page_size,
        "sort_by": sort_by,
        "include_images": include_images,
    }
