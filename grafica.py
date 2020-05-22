from numpy import *
from matplotlib.pyplot import *

X=arange(-4,4,0.01)
Y=arange(0.1,4,0.01)
Z=arange(0.1,4,0.1)

f1=figure()
plot(sin(X),label='sen(x)')
plot(cos(X),label='cos(x)')
title('Sen y Cos')
legend()
savefig('senocoseno.pdf')
#show()

f2=figure()
plot(exp(Y),label='epx(x)')
plot(log(Y),label='ln(x)')
title('Exp y Log')
legend()
savefig('expolog1.pdf')
#show()


f3=figure()
plot(exp(Z),label='epx(x)',color='blue',marker='o')
plot(log(Z),label='ln(x)',color='blue',marker='*')
title('Exp y Log')
legend()
savefig('expolog2.pdf')
#show()
