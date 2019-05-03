"""
>>> Hawkeye = Avenger('Clint Barton', 'Bow')
>>> Hawkeye
Avenger(real_name='Clint Barton', weapon='Bow')
>>> Avenger._fields
('real_name', 'weapon')
"""

from collections import namedtuple

Avenger = namedtuple('Avenger', ['real_name', 'weapon'])