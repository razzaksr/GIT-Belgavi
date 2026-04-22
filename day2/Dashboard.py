from API import gHealth

health1 = gHealth.getHealth()
print(health1.filter("bmr",1400,"ge"))
health1.initialize("Sabarinathan",34,"male",172)
health1.makeWeighIn(id="4",weight=82.9)