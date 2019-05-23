class Parent:
   def __init__(self, name="Parent class"):
       self.name = name


class Child1(Parent):
   def __init__(self, name):
       Parent.name = name


class Child2(Parent):
   def __init__(self, name):
       Child2.name = name


def vypis_potomkov():
   print(
       f"Parent name: {Parent.name}\n"
       f"Potomok1 name: {potomok1.name}\n"
       f"Potomok2 name: {potomok2.name}\n"
   )


if __name__ == "__main__":
   potomok1 = Child1("Child 1")
   potomok2 = Child2("Child 2")
   vypis_potomkov()
   potomok2.name = "Potomok 2"
   potomok1.name = "Potomok 1"
   print("====")
   vypis_potomkov()