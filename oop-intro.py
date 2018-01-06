# Introduction to OOP

# item - we will have lots of items
class Item():
  def __init__(self, name, desc, value):
    self.name = name
    self.desc = desc
    self.value = value

  def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, 
                                                   self.desc,
                                                   self.value)
#==================================================================
class Weapon(Item):
	def __init__(self,name,desc,value,dura):
	    self.dura = dura
	    super().__init__(name, desc, value)

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDurability: {}\n".format(self.name, 
                                                   self.desc,
                                                   self.value,
                                                   self.dura)
		

# define a charecter

# main
#goldBar = Item('Gold bar', 'A ingot of pure gold', 100)
#silverBar = Item('Silver bar', 'A ingot of pure silver', 80)

# How do we create a sword - durability, material
sword = Weapon("iron sword", "sword of iron", 25, 100)
print(sword)
#print(goldBar)
#print(silverBar)