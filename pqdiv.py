#encoding:cp932
def qs(s,x,y,z,wa=True): s='%%2d%s%%2d＝' % s; return (('%s%%2d' % s) % (x,y,z)) if wa else (s % (x,y))
def qa(x,y,wa=True): return qs('＋',x,y,x+y,wa)
def qe(x,y,wa=True): return qs('－',x+y,y,x,wa)
def qm(x,y,wa=True): return qs('*',x,y,x*y,wa)
def qd(x,y,wa=True): return qs('÷',x*y,y,x,wa)
def ra(x,y): return range(x,y+1)
import random
def sf(s): random.shuffle(s); return s
def xaf(s,t,f): return [[f(i,j) for j in t] for i in s]
def laf(s,t,f): return [f(i,j) for i in s for j in t]
def xa(s,t): return [[(i,j) for j in t] for i in s]
def la(s,t): return [(i,j) for i in s for j in t]
CR="\n";S="   ";R19=ra(1,9);R29=ra(2,9)
def jx(s): return CR.join([S.join(r) for r in s])
def sp(s,n): return [] if not s else [s[:n]]+sp(s[n:],n)
HN=u' 0123456789'; ZN=u'　０１２３４５６７８９'; DIC=dict([(ord(h),z) for h in HN for z in ZN])
def nz(s): return s.translate(DIC)
print jx(sp([qd(x,y,False) for x,y in sf(la(R29,R19))],5)
