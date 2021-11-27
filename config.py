from transitions import State


TOKEN = 'Your token here'


states = ['ready', 
          State(name='pizza', on_enter=['ask_pizza_size']), 
          State(name='pending_for_size', on_enter=['check_pizza_size']), 
          State(name='payment', on_enter=['ask_payment_type']), 
          State(name='pending_for_payment', on_enter=['check_payment_type']), 
          State(name='confirm', on_enter=['ask_order_confirm']), 
          State(name='pending_confirm', on_enter=['check_order_confirm']), 
          'complete']

transitions = [
    {'trigger': 'greeting', 'source': '*', 'dest': 'ready'},
    {'trigger': 'pizza_size', 'source': ['ready', 'pending_for_size'], 'dest': 'pizza'},
    {'trigger': 'payment_type', 'source': ['pending_for_payment'], 'dest': 'payment'}
]


WORDS_ENG = {}


WORDS_RUS = {
    'ask_pizza_size': 'Какую вы хотите пиццу? Большую или маленькую?',  
    'check_pizza_size': ['Большую', 'маленькую'],
    'ask_payment_type': 'Как вы будете платить?',
    'check_payment_type': ['Наличкой', 'за спасибо :)'], 
    'check_order_confirm': ['Да', 'OK', 'Done'],
    'order_thanks': 'Спасибо за заказ',
    'cancel_order': 'Cancel order'
}


