x1 = float(input("Digite o ponto x1:  "))
x2 = float(input("Digite o ponto x2:  "))
y1 = float(input("Digite o ponto y1:  "))
y2 = float(input("Digite o ponto y2:  "))

import func_dist
res=func_dist.calc_dist(x1,x2,y1,y2)

print(res)