class Book:

    # Didn't use *args because it's usually a positional argument
    def __init__(self, **kwargs):
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
        self.order_number = kwargs.get('order_number')
        self.product_name = kwargs.get('book_name')
        self.product_price = kwargs.get('product_price')
        self.product_amount = kwargs.get('product_amount')
        self.product_total_price = kwargs.get('product_total_price')
        pass
        

class Report:

    def __init__(self, **kwargs):
        self.report_date = kwargs.get('report_date')
        self.sale = kwargs.get('sale')

        self.total_sale = kwargs.get('total_sale')
        pass
        