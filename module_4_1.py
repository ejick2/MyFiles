from Divide.fake_math import divide as fake_divide
from Divide.true_math import divide as true_divide
print("Фейковое деление:")
print(fake_divide(69, 3))
print(fake_divide(3, 0))
print("Истинное деление:")
print(true_divide(49, 7))
print(true_divide(15, 0))

