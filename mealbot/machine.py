from transitions import Machine, State
from transitions.extensions.states import add_state_features, Tags, Timeout

import config


class InstanceStorage(type):
    """Metaclass designed to implement storage for various number
    of instances, provide access to instance by unique id""" 

    _instances = dict()
    
    def __call__(cls, *args, **kwargs):
        inst_id = kwargs['bot_id'] 
        if inst_id in cls._instances:
            return cls._instances[inst_id]
        cls._instances[inst_id] = super(InstanceStorage, cls).__call__(*args, **kwargs)
        return cls._instances[inst_id]


class PizzaBot(metaclass=InstanceStorage):
  
    def __init__(self, *args, **kwargs):
        self.message = ''
        self.response = ''
        self.pizza_size = ''
        self.payment_type = ''
        self.machine = Machine(model=self, states=config.states, transitions=config.transitions, initial='ready')
        self.machine.add_ordered_transitions()
        self.words = config.WORDS_RUS

    def on_message(self, msg=''):
       self.message = msg
       self.response = ''
       self.next_state()	
       return self.response
    

    def words_for(self, key, default=''):
        return self.words[key] if key in self.words else default	

    def check_word(self, key, word):
        if key not in self.words:
            return False

        data = self.words[key]    
        
        if word in data:  # List or tuple of values
        	return True

        if word == data:  # Single string
            return True 

        return False


    def ask_pizza_size(self):  
        #self.response = 'Choose pizza size, big or small ?'
        self.response = self.words_for('ask_pizza_size')


    def check_pizza_size(self, message=''):
        if self.check_word('check_pizza_size', self.message):
        	self.pizza_size = self.message
        	self.next_state()
        else:
            self.trigger('pizza_size')	   # Trigger is hardcoded, bad !!!
        

    def ask_payment_type(self):  
        self.response = self.words_for('ask_payment_type')

    def check_payment_type(self, message=''):
        if self.check_word('check_payment_type', self.message):
        	self.payment_type = self.message
        	self.next_state()
        else:
            self.trigger('payment_type')	# Trigger is hardcoded, bad !!!
        

    def ask_order_confirm(self):  
        #self.response = 'Complete order, pizza "{}" payment "{}" ?'.format(self.pizza_size, self.payment_type)
        self.response = 'Вы хотите {0} пиццу, оплата - {1}?'.format(self.pizza_size.lower(), self.payment_type.lower())

    def check_order_confirm(self, message=''):
        if self.check_word('check_order_confirm', self.message):
            self.response = self.words_for('order_thanks')
        else:
            self.response = self.words_for('cancel_order')
        self.next_state()
        
    