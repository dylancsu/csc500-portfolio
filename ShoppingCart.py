from List import ItemToPurchase

class ShoppingCart:
    def __init__(self, **kwargs):
        self.customer_name=kwargs.get('customer_name','none')
        self.current_date=kwargs.get('current_date','none')
        self.cart_items=[]
    def add_items(ItemToPurchase item):
        self.cart_items.append(item)
        