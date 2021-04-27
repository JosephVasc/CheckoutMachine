from dataclasses import dataclass
import time
import winsound


@dataclass
class itemTax:
    item_name: str
    unit_price: float
    state: str
    item_type: str
    tax_rate = 0.0
    clothing_tax_limit = 0.00

    def state_tax(self):
        if self.state == 'MA' and self.item_type == 'other':
            self.tax_rate = 0.0625
        elif self.state == 'MA' and self.item_type == 'clothing' and self.unit_price > 175.00:
            clothing_cost = self.unit_price - 175.00
            clothing_cost = clothing_cost * 1.0625
            self.unit_price = clothing_cost + 175.00
            self.tax_rate = 0.0

        if self.state == 'ME' and self.item_type == 'clothing':
            self.tax_rate = 0.055
        elif self.state == 'ME' and self.item_type == 'other':
            self.tax_rate = 0.055
        elif self.state == 'ME':
            self.tax_rate = 0.00


    def total(self):
        tax = self.unit_price * self.tax_rate
        totalprice = tax + self.unit_price
        return totalprice

def mainfunction(state, listofitems):
    total = 0.0

    for i in range(len(listofitems)):
        item,price,type = listofitems[i]
        print("Scanning Item: ", item)
        print("price: ", price)
        print("type: ", type)
        my_item = itemTax(item.lower(), price, state.upper(), type.lower())
        my_item.state_tax()
        item_total = my_item.total()
        print("item after tax: ", item_total)
        time.sleep(1)
        total += item_total
    print("your checkout price including tax:", round(total, 2))
    return total


state = 'MA'
listofitems= [("suit", 200.00, "CLOTHING"), ("suit", 100.00, "clothing"), ("dog", 200.00, "other"), ("burger", 10.00, "food")]
mainfunction(state, listofitems)

















