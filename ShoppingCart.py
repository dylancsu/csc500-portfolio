from List import ItemToPurchase

class ShoppingCart:
    def __init__(self, **kwargs):
        self.customer_name=kwargs.get('customer_name','none')
        self.current_date=kwargs.get('current_date','none')
        self.cart_items=[]
    def add_items(item):
        self.cart_items.append(item)
    def remove_item(item_name):
        for item in self.cart_items:
            if item.item_name==item_name:
                self.cart_items.remove(item)
                break
        print("Item not found in cart. Nothing removed.")
    def modify_item(new_item):
        for item in self.cart_items:
            if item.item_name==new_item.item_name:
                if new_item.item_quantity!=0:
                    item.item_quantity=new_item.item_quantity
                if new_item.item_price!=0.0:
                    item.item_price=new_item.item_price
                if new_item.item_description!='none':
                    item.item_description=new_item.item_description
                break
            print("Item not found in cart. Nothing modified.")
            