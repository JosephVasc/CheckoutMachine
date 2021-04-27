import pytest
import main
def case_sensitive():
    assert (main.mainfunction('ma', [("suit", 200.00, "CLOTHING")]) == main.mainfunction('MA', [
        ("suit", 200.00, "clothing")]))
def floater():
    assert (main.mainfunction('ma',[("suit", 200.00, "CLOTHING")]), float)
def notaxoutofstate():
    assert (main.mainfunction('TM', [("suit", 200.00, "CLOTHING")]) == 200.00)
def noReturns():
    assert(main.mainfunction('MA', [("suit", -200.00, "CLOTHING")]) == 0)


