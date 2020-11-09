from jinja2 import Template
from postprocess_fom import obj
import os

with open('truss.jinja') as fh:
    templ = Template(fh.read())
def calculate_objective(v, i=None):
    if i:
        name = 'truss' + str(i)
    else:
        name = 'truss'
    print(name)
    with open(name, 'w') as fh:
        fh.write(templ.render(v0=v[0],
            v1=v[1],
            v2=v[2],
            v3=v[3],
            v4=v[4],
            v5=v[5]))
    os.system('./a.out ' + name)
    return obj(name + '_result')

# print(calculate_objective([0,0,0,-2,-2,-2]))
