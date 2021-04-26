from dataclasses import dataclass
import time
import winsound


@dataclass
class itemTax:
    item_name: str
    unit_price = 0.0
    state: str
    item_type = ''
    tax_rate = 0.0

    def state_tax(self):
        if self.state == 'MA' and self.item_type == 'taxable':
            self.tax_rate = 0.0625
        elif self.state == 'ME' and self.item_type == 'taxable':
            self.tax_rate = 0.055
        else:
            self.tax_rate = 0.0

    def total(self):
        tax = self.unit_price * self.tax_rate
        totalprice = tax + self.unit_price
        return totalprice

    def items(self):
        if self.item_name == 'shirt':
            self.unit_price = 10.00
            self.item_type = ''
        elif self.item_name == 'pants':
            self.unit_price = 20.00
            self.item_type = ''
        elif self.item_name == 'shoes':
            self.unit_price = 30.00
            self.item_type = ''
        elif self.item_name == 'eggs':
            self.unit_price = 4.00
            self.item_type = ''
        elif self.item_name == 'milk':
            self.unit_price = 2.00
            self.item_type = ''
        elif self.item_name == 'bread':
            self.unit_price = 2.00
            self.item_type = ''
        else:
            self.unit_price = 10.00
            self.item_type = 'taxable'


def mainfunction(state, listofitems):
    total = 0

    for i in range(len(listofitems)):

        item = listofitems[i]
        winsound.Beep(1000, 250)
        print("Scanning Item: ", item)
        my_item = itemTax(item, state)
        my_item.items()
        my_item.state_tax()
        item_total = my_item.total()
        print(item_total)
        time.sleep(1)
        total += item_total
    print("your checkout price including tax:", round(total, 2))


state = 'MA'
listofitems = ['shirt', 'shoes', 'dog', 'pants', 'horse', 'car']
mainfunction(state, listofitems)
















