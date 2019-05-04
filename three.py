# Another iteration on namedtuples
from collections import namedtuple

Ranger = namedtuple('Ranger', 'name armor weapon')

def spawn_ranger(name, armor, weapon):
    """
    >>> spawn_ranger('Llewyn', 'leather', 'crossbow')
    Ranger(name='Llewyn', armor='leather', weapon='crossbow')
    """
    return Ranger(name, armor, weapon)