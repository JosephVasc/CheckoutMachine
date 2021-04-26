import pytest
import main
def capital_case():
    listofitems = ['shirt', 'shoes', 'DOG', 'PaNts', 'horse', 'car']
    state = 'ma'
    assert main.mainfunction(state, listofitems) == 91.88
