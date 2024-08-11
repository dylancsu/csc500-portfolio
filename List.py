class ItemToPurchase:
    def __init__(self, **kwargs):
        self.item_name=kwargs.get('item_name','none')
        self.item_price=kwargs.get('item_price',0.0)
        self.item_quantity=kwargs.get('item_quantity',0)
    def print_item_cost():
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_cost} = ${self.item_cost * self.item_quantity}')
        
