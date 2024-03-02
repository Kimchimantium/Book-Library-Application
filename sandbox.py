# class Planet:
#     def __init__(self, name_of_planet):
#         self.name_of_planet = name_of_planet
#     def __repr__(self):
#         return f'<Planet Name: {self.name_of_planet}>'
#
# planet_picker = Planet('Uranus')
# picked_planet = repr(planet_picker)
# print(picked_planet)
#
class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'MyClass({self.value})'

# Creating an instance of MyClass
obj = MyClass(42)
representation = repr(obj)
print(representation)
