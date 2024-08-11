class ItemToPurchase:
    def __init__(self, **kwargs):
        self.item_name=kwargs.get('item_name','none')
        self.item_price=kwargs.get('item_price',0.0)
        self.item_quantity=kwargs.get('item_quantity',0)
    def print_item_cost():
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_cost} = ${self.item_cost * self.item_quantity}')

items=[]
for i in range(2):
    print(f"Item {i}")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    new_item=ItemToPurchase(item_price=price,item_name=name,item_quantity=quantity)
    items.append(new_item)

total_cost = 0.0
for item in items:
    total_cost+=(item.item_price * item.item_quantity)
    item.print_item_cost()
print(f"Total: ${total_cost}")