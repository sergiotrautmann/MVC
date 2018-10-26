from view import View
from control import Control
from model import Model

m = Model()
v = View()
c = Control(v, m)

v.set_control(c)

c.exibir_menu()
