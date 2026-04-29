from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Pricelevel:
    price: Decimal
    quantity: Decimal


p = Pricelevel(price=Decimal("42000.50"), quantity=Decimal("1.5"))

print(p)
print(p.price)
# p.price = Decimal("99.00")
my_set = {p}
