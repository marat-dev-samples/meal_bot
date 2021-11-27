"""

Run this tests using: 
- python -m unittest -v tests.machine_tests

< Какую вы хотите пиццу? Большую или маленькую?
> Большую
< Как вы будете платить?
> Наличкой
< Вы хотите большую пиццу, оплата - наличкой?
> Да
< Спасибо за заказ

"""

import unittest
import unittest.mock  
from mock import Mock
from mock import patch
from collections import namedtuple

from mealbot.machine import PizzaBot
import config


class PizzaBotTests(unittest.TestCase):
    
    def setUp(self):
        return
    
    #@unittest.skip("Skipped temporary")
    def test_for_machine_states(self):                    
        
        TestCase = namedtuple('TestCase', ['name', 'msg', 'state'])
        test_cases = [                      
            TestCase('Open connection', '', 'pizza'), 
            TestCase('Incorrect pizza size', 'Middle', 'check_pizza_size'), 
            TestCase('Correct pizza size', 'Большую', 'pizza'), 
            TestCase('Choose payment method', 'Наличкой', 'payment'), 
            TestCase('Confirm order', 'Да', 'confirm') 
        ]

        bot = PizzaBot(bot_id='123456') 
    
        for test in test_cases:     
            
            # Prints are more informative here
            print('> {}'.format(test.msg))
            print('< {}'.format(bot.on_message(test.msg)))
            
            #self.assertEqual(state, test.state, '{0} test got incorrect state result'.format(test.name, test.result, result)) 
      
            if bot.state == 'complete':
                break
            