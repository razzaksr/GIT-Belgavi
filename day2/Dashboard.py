from API import gHealth

health1 = gHealth.getHealth()
health1.initialize("Sabarinathan",34,"male",172)
health1.makeWeighIn(id="1",weight=82.9)
health1.initialize("Razak Mohamed",34,"male",158)
health1.makeWeighIn(id="2",weight=71.02)
health1.initialize("Nithya",24,"female",142)
health1.makeWeighIn(id="3",weight=52.9)
health1.initialize("Rakshana",33,"female",160)
health1.makeWeighIn(id="4",weight=62.9)
print(health1.filter("bmr",1400,"ge"))
# health1.updateWeighIn(id="4",weight=78)