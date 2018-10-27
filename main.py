from view import View
from control import Control
from model import Model
from arquivo import Arquivo
m = Model()
v = View()
c = Control(v, m)
a = Arquivo()

v.set_control(c)

c.exibir_menu()
