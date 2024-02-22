class Book:

    # Didn't use *args because it's usually a positional argument
    def __init__(self, **kwargs):
        self.book_id = kwargs.get('book_id') # Primary
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

class Sale:

    def __init__(self, **kwargs):
        self.order_id = kwargs.get('order_id') # Primary
        self.product_name = kwargs.get('book_name') # Foreign
        self.product_price = kwargs.get('product_price')
        self.product_amount = kwargs.get('product_amount')
        self.order_date = kwargs.get('order_date')
        self.employee_id = kwargs.get('employee_id') # Foreign
        

class Report:

    # Monthly report
    def __init__(self, **kwargs):
        self.report_id = kwargs.get('report_id') # Primary
        self.report_date = kwargs.get('report_date')
        self.sales = kwargs.get('sales') # Foreign
        self.total_sale = kwargs.get('total_sale')
        

class Employee:

    # This part is purely abstraction

    def __init__(self, employee_name, employee_pass, employee_id, employee_prev):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_pass = employee_pass
        self.employee_prev = employee_prev
