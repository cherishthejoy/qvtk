class Books:

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