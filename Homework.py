# class My_printer:
#     my_input = "" 
    
#     def __init__(self):
#         print('my printer has been created')
        
#     def get_string(self):    
#         self.my_input = input('give me a random word: ')
    
#     def print_string(self):
#         print(self.my_input.upper())
        
    
# user1 = My_printer()
# user1.get_string()
# user1.print_string()


# user = input('what would you like to add to your cart?: ')

class Shopping_Cart:
    cart = {}

    def greeting(self):
        print('welcome to my shop')
        
    def driver(self):
        for item, value in self.cart.items():
            print(f'you currently have {value} {item}\'s in your shopping list \n' )
        item = input('please enter an item to add to your shopping list or type "quit" to stop: \n')
        if item.lower() == 'quit':
            return quit
        value = input('how many of that item would you like?: \n')
        self.cart[item] = value
    
        del_item = input('did you make a mistake? say the name of the last item you entered to delete: or press enter to continue. \n')
        if del_item == self.cart[item]:
            del self.cart[item] 
        else:
            self.driver()
        
        

        
u = Shopping_Cart()
u.driver()