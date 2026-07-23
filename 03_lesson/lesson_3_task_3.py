from address import Address
from mailing import Mailing

address1 = Address("468512", "Морио", "Луччи", "33", "5")
address2 = Address("695443", "Трансильвания", "Дракула-стрит",
                   "13", "98")

mail = Mailing(to_address=address1, from_address=address2,
               cost=1500.0, track="WB547893152248")

print(f"Отправление {mail.track} из  {address1.format()} в "
      f"{address2.format()}. Стоимость {mail.cost} йен.")
