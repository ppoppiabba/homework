from abc import ABC, abstractmethod

class Item(ABC):
    count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1

    @abstractmethod
    def getprice(self):
        pass

class Book(Item):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author
        print("제목:",self.title,",가격:",self.price,",페이지 수:",self.pages,"저자:",self.author)
    def getprice(self):
        return f"{self.title}의 가격은 {self.price}원 입니다."

class Magazine(Item):
    def __init__(self, title, price, issue_month):
        super().__init__(title, price)
        self.issue_month = issue_month
        print("제목:",self.title,",가격",self.price,",출간 월:",self.issue_month)
    def getprice(self):
        return f"{self.title}의 가격은 {self.price}원 입니다."

if __name__ == '__main__':
    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, 9)
    magazine2 = Magazine('싱글즈', 13000, 8)

 
    print(book1)
    print(book2)
    print(book3)
    print(magazine1)
    print(magazine2)

 
    print('총', Item.count, '권')

 
    print("*", book2.title, "의 가격은 ", book2.price, "원 입니다.")
    print("*", magazine1.title, "의 가격은 ", magazine1.price, "원 입니다.")
    print("*", book1.title, "의 가격은 ", book1.price, "원 입니다.")
