class ItemToPurchase:
    def __init__(self, **kwargs):
        self.item_name=kwargs.get('item_name','none')
        self.item_description=kwargs.get('item_description','none')
        self.item_price=kwargs.get('item_price',0.0)
        self.item_quantity=kwargs.get('item_quantity',0)
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${(self.item_price * self.item_quantity):.2f}')