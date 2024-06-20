from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    email:EmailStr
    acc_id:int

    @validator("acc_id")
    def validate_acc_id(cls, value):
        if value <= 0:
            raise ValueError(f"acc_id sould be positive: {value}")
        return value

user = User(name='Roba', email ='linkmash030@gmail.com', acc_id = 22222)

#print(user.acc_id)
#print(user.email)

#print(user)

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]

my_books = [
		Book(
		    author="J. K. Rowling",
		    title="Harry Potter and the Philosopher's stone",
		    pages=[
		        Page(
		            number=1,
		            text="There once was a boy...",
		        ),
		        Page(
		            number=2,
		            text="He went to magic school...",
		        )
		    ]
		),
		Book(
		    author="Roger Zelazny",
		    title="Lord of Light",
		    pages=[
		        Page(
		            number=1,
		            text="It is said that fifty-three years ago...",
		        )
		    ]
		),
		Book(
            author = "Jeff Kinney",
            title = "Diary of  a Wimpy Kid",
            pages=[
                Page(
                    number=5,
                    text = "There once was a young boy"
                )
            ]
        ),
]

#print(my_books[0].author)
# print(my_books[0].pages[0].text)

#for book in my_books:
#    print(book.title)

import yaml

print(yaml.dump(my_books[0].dict()))

from pydantic_core import to_jsonable_python

print(yaml.dumps(to_jsonable_python(my_books)))