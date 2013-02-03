#encoding:cp932
def z(s)s.tr(' 0-9','　０-９')end
def w(a,b,c=nil)z("%2d÷%d＝%s"%[a*b,a,c ? b : ''])end
def m(a,b)(a..b).to_a.shuffle.map{|i|i}end
def by(a,b,&c);a.map{|i|b.map{|j|c.call(i,j)}}end
A=by(m(2,9),m(1,9)){|i,j|[w(i,j),w(i,j,1)]}; CR="\n"; Z='　'
def sz(a,i=0,s=0)a.slice((i*4)..(i*4+3)).map{|e|e.map{|f|f[s]}}end
def jp(a)puts a.transpose.map{|o|o.join(Z)}.join(CR);puts CR;end
SW=[0,1];SW.each{|t|SW.each{|s|jp sz(A,s,t)}}
