from API import gHealth

health1 = gHealth.getHealth()
print(health1.filter("bmr",1400,"ge"))