#!/usr/bin/env python
'Conjugate-gradient method'

##   Copyright (C) 2008 University of Texas at Austin
##  
##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2 of the License, or
##   (at your option) any later version.
##  
##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.
##  
##   You should have received a copy of the GNU General Public License
##   along with this program; if not, write to the Free Software
##   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import m8r

def conjgrad(oper,dat,x0,ref,niter):
    'Conjugate-gradients for minimizing |oper x - dat|^2'
    dat2 = dat.dot2()
    l2dat0 = dat2**0.5
    print "Data L2res m=0: %g" %(l2dat0)
    x = x0
    R = oper(adj=0)[x]-dat      
    for iter in range(niter):
        R2 = R.dot2()
        l2R = R2**0.5
        print "Data L2res iter %d: %g" % (iter+1,l2R)
        g = oper(adj=1)[R]
        G = oper(adj=0)[g]
        gn = g.dot2()
        print "Gradient iter %d: %g" % (iter+1,gn)
        if 0==iter:
            s = g
            S = G
        else:
            beta = gn/gnp
            s = g+s*beta
            S = G+S*beta
        gnp = gn
        alpha = -gn/S.dot2()
        x = x+s*alpha
        R = R+S*alpha
        dist = x-ref
        dist2 = dist.dot2()
        l2dist = dist2**0.5
        print "Model L2res iter %d: %g " %(iter+1, l2dist)



    return x

if __name__ == "__main__":

    # Using function above
    wavl = m8r.File('wavelet.rsf')
    vel = m8r.File('vel-mig.rsf')

    data = m8r.File('bshots45.rsf')
    # using model0 all zeros
    mod0 = m8r.File('model0.rsf')
    refl = m8r.File('refl.rsf')

    oper = m8r.fdlsrtm(velocity=vel, wavelet=wavl, \
        nr=1150, dr=0.008, r0=0, ns=45, ds=0.2, s0=0.0, verb='y')

    x = conjgrad(oper,data,mod0,refl,20)

    print(x)

    