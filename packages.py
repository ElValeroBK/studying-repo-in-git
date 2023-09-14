# import ecommerce.shipping       # way 1 to call a module
# ecommerce.shipping.calculate()

'''from ecommerce.shipping import calculate,cal_tax  # way 2 to call a module  and multiplex methods
calculate()
cal_tax()'''


from ecommerce import shipping  # way 3 to call a module
shipping.cal_tax()
shipping.calculate()


import random    # system modules (ramdom)

for i in range(3):
   print(random.randint(50,70))

team = ["Juan","Pacheco","Manuel","alverto"]
print(random.choice(team))
 

