from List import ItemToPurchase

class ShoppingCart:
    def __init__(self, **kwargs):
        self.customer_name=kwargs.get('customer_name','none')
        self.current_date=kwargs.get('current_date','none')
        self.cart_items=[]
    def add_items(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name==item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, new_item):
        for item in self.cart_items:
            if item.item_name==new_item.item_name:
                if new_item.item_quantity!=0:
                    item.item_quantity=new_item.item_quantity
                if new_item.item_price!=0.0:
                    item.item_price=new_item.item_price
                if new_item.item_description!='none':
                    item.item_description=new_item.item_description
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total+=item.item_quantity
        return total
    def get_cost_of_cart(self):
        total = 0.0
        for item in self.cart_items:
            total+=item.item_quantity*item.item_price
        return total
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of items: {self.get_num_items_in_cart}")
        total_cost = 0.0
        for item in self.cart_items:
            total_cost+=(item.item_price * item.item_quantity)
            item.print_item_cost()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    while True:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output item descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Enter your selection: ")
        match choice:
            case 'q':
                break
            case 'a':
                name = input("Enter the item name: ")
                price = float(input("Enter the item price: "))
                quantity = int(input("Enter the item quantity: "))
                new_item=ItemToPurchase(item_price=price,item_name=name,item_quantity=quantity)
                cart.add_items(new_item)
            case 'r':
                name = input ("Enter the item name: ")
                cart.remove_item(name)
            case 'c':
                name = input("Enter the item name: ")
                price = float(input("Enter the item price: "))
                quantity = int(input("Enter the item quantity: "))
                new_item=ItemToPurchase(item_price=price,item_name=name,item_quantity=quantity)
                cart.modify_item(new_item)
            case 'i':
                cart.print_descriptions()
            case 'o':
                cart.print_total()
            

def main():
    name = input("Enter your name: ")
    date = input("Enter the currrent date")
    cart = ShoppingCart(customer_name=name,current_date=date)
    print_menu(cart)

if __name__ == "__main__":
    main()