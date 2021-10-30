from fastapi import FastAPI
from typing import Optional
import uvicorn

from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: int = 30, published: bool = False, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blogs from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title {blog.title}"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)


