from dataclasses import dataclass


@dataclass
class Book:
    id_: int
    title: str
    author: str
    year: str
    status: str = 'In stock'

    def __str__(self):
        return f"id: {self.id_} | Title: {self.title} | Author: {self.author} | Year: {self.year} | Status: {self.status}"

