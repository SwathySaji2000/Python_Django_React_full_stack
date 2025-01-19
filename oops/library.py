# create a class library

# add_book: parameters title,author,year

# {title:{author:"author",year:"year"}}

#remove bookname

# year > 2000 in a list 

class Library:

    def __init__(self):

        self.data = {}
        self.deatils = {}
       


    def add_book(self,title,author,year):

        self.title = title
        self.author = author
        self.year = year

        self.data[self.title] = {author : 'author',year : 'year'}   
        return(self.data) 
    

    def remove_book(self,name):
        if name in self.data:

            del self.data[name]

            print(self.data)
        else:

            print("not found")

    def filter_2000(self):

        # new = []

        # for i in self.data:

        #     if self.data[i]['year'] >= 2000:

        #         return new

        result = [i for i in self.data if self.data[i]['year'] >= 2000]
        return result

obj=Library()
obj.add_book(title="window",author="j.k",year=2017)
obj.add_book(title="dark shades",author="taylor",year=2000)
obj.add_book(title="hope",author="roy",year=1999)
# obj.add_book()
obj.remove_book(name="window")
obj.filter_2000()
print(obj.filter_2000())
# print(obj.add_book(title="balarama",author="j.k",year=2017))

