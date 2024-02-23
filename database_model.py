class Book:

    def __init__(self, **kwargs):
        self.book_id = kwargs.get('book_id')
        self.book_name = kwargs.get('book_name')
        self.book_author = kwargs.get('book_author')
        self.book_published_date = kwargs.get('book_published_date')
        self.book_publisher = kwargs.get('book_publisher')
        self.book_category = kwargs.get('book_category')
        self.book_language = kwargs.get('book_language')
        self.book_dimension = kwargs.get('book_dimension')
        self.book_ISBN = kwargs.get('book_ISBN')
        self.book_page_count = kwargs.get('book_page_count')
        self.book_synopsis = kwargs.get('book_synopsis')
        self.book_cover_type = kwargs.get('book_cover_type')
        self.book_price = kwargs.get('book_price')
        self.book_model = kwargs.get('book_model')
        self.book_stock = kwargs.get('book_stock')
        self.book_weight = kwargs.get('book_weight')

    def addBookRecord(self):
        pass

    def deleteBookRecord(self):
        pass

    def editBookRecord(self):
        pass

    def searchBookByName(self):
        pass
    
    def searchBookByAuthor(self):
        pass


class Sale:

    def __init__(self, **kwargs):
        self.order_id = kwargs.get('order_id') 
        self.product_name = kwargs.get('book_name') 
        self.product_price = kwargs.get('product_price')
        self.product_amount = kwargs.get('product_amount')
        self.order_date = kwargs.get('order_date')
        self.employee_id = kwargs.get('employee_id')

    def createSale(self):
        pass

    def editSale(self):
        pass

    def deleteSale(self):
        pass

        

class Report:

    def __init__(self, **kwargs):
        self.report_id = kwargs.get('report_id')
        self.report_date = kwargs.get('report_date')
        self.sales = kwargs.get('sales') 
    
    def createReport(self):
        pass


class Employee:

    def __init__(self, **kwargs):
        self.employee_id = kwargs.get('employee_id')
        self.employee_firstname = kwargs.get('employee_firstname')
        self.employee_lastname = kwargs.get('employee_lastname')
        self.employee_pass = kwargs.get('employee_pass')
        self.employee_prev = kwargs.get('employee_prev')

    def addEmployee(self):
        pass

    def removeEmployee(self):
        pass

    def changeUser(self):
        pass




