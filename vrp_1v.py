#!/usr/bin/env python
# *-* coding: utf8 *-*
from operator import itemgetter 

from operator import index
import random
from random import randint
import numpy as np
import input_1v as inp
import copy
from math import *
global n_v01
global n_v02
global n_c01
global n_c02
global nnc
nnc=inp.nc
global nvav
global tab2opt
tab2opt=[]
global fotab2opt
fotab2opt=[]
global n2opt
n2opt=inp.nv -1
# n2opt=18
#  nombre des valeurs apres vergule (choix)
nvav=3
ttt=0.1
# pour incrementer les index
def add1(sol):
    global n_v01
    global n_v02
    global n_c01
    global n_c02
    len_c1 = len(sol[n_c01])
    len_c2 = len(sol[n_c02])
    len_sol = len(sol)

    if n_v01+1 >= len_c1:
        n_v01 = 0
        n_c01 +=1 
    else:
        n_v01 +=1 
    if n_v02+1 >= len_c2:
        n_v02 = 0
        n_c02 +=1
    else:
        n_v02 +=1 
    if n_c01 >= len_sol:
        n_c01=0
    if n_c02 >= len_sol:
        n_c02=0
    
class individu:
# pour initialiser les fonctions
    def __init__(self):
        self.sol=self.get_new_indi()
        self.fo=0
    # cette fonction, pour generer la premiere solution selement
    def get_sec(self,m, n):
        s=0
        lis = [0] * m;
        while s<n:
            a=random.sample(lis,1)
            lis[lis.index(a[0])] +=1
            s=sum(lis)
        return lis
# contrainte de la capacité du camion qu'il faut respecter
    def contrent_c(self,sol):
        i=0
        for rec in sol:
            s=0
            for rec2 in rec:
                s+=inp.dv[rec2]
            if s > inp.cc[i]:
                return  True
            #   print('s= ',s)
            i+=1
        return False
# trouver la nouveau chemin
    def get_new_indi(self):
        sec_v=list(range(inp.nv))
        fin=True
        sol = []
        while fin:
            sec_c = self.get_sec(inp.nc, inp.nv)
            random.shuffle(sec_v)
            sol = []
            k = 0
            for i in range(inp.nc):
                lis = []
                for j in range(sec_c[i]):
                    lis.append(sec_v[k])
                    k += 1
                sol.append(lis)
            fin=self.contrent_c(sol)
        return sol
# calculer la fonction objectif d'un chemin courante trouver
    def calc_fo(self):
        sol=self.sol
        ds=inp.distance
        d=0
        l=0
        for i in sol:
            if len(i)!=0:
                k = i[0] + 1
                d += ds[0][k]
                for j in range(len(i) - 1):
                    k = i[j] + 1
                    l = i[j + 1] + 1
                    d += ds[k][l]
                d += ds[l][0]
        self.fo =d
# la solution voisin trouver en swapon des point de ville de la solution courante
    def get_voisin(self):
        indv=copy.deepcopy(self)
        sol=copy.deepcopy(self.sol)
        def get_new_indi(self):
            sec_v = list(range(inp.nv))
        nnc = inp.nc
        fin = True
        while fin:
            # debut 2-opt
            finnn = True
            add1(self.sol)
            ssss='('+str(n_c01)+ " , "+str(n_v01)+ ") - ("+str(n_c02)+" , "+str(n_v02)+ ")"
            print(ssss)
            sol = copy.deepcopy(self.sol)
            v1 = sol[n_c01][n_v01]
            sol[n_c01][n_v01] = sol[n_c02][n_v02]
            sol[n_c02][n_v02] = v1
            fin = self.contrent_c(sol)
            # fin 2-opt
            # fin =True
        indv.sol = sol
        indv.calc_fo()
        return indv
# appliquer l'algorithme recuit simulé
def recuit_simule(ind):
    N = 10
    t = 0
    T0 = 10
    T = T0
    Tmin = 1
    tau= 100
    k = 0
    ind_courante = copy.deepcopy(ind)
    ind_courante.calc_fo()
    d_courante = ind_courante.fo
    global n_v01
    global n_v02
    global n_c01
    global n_c02
    n_c01 = 0
    n_c02 = 0
    n_v01 = 0
    n_v02 = 1
    inv=1
    # initialisation meilleur solution
    best_sol= ind_courante.fo
    best_ind = ind_courante
    while Tmin < T:
        if inv==1:
            # print('_________________________________')
            # print("cout du chemin de distance du chemin courante = ", d_courante, "chemin hamilto courante = ",
            #       ind_courante.sol)
            inv=0
        # 2 opt
        tab2opt=[]
        for iii in range(n2opt):
            ssss='('+str(n_c01)+ " , "+str(n_v01)+ ") - ("+str(n_c02)+" , "+str(n_v02)+ ")"

            beta = round(random.uniform(0,1),nvav)
            ind_voisine = ind_courante.get_voisin()
            d_voisine= ind_voisine.fo

            lll=[]
            lll.append(d_voisine)
            lll.append(ssss)
            lll.append(ind_voisine)
            lll.append(beta)
            tab2opt.append(lll)
            pass
        # afficher ind_courante
        print(ind_courante.sol)
        print(' k :',k)
        # afficher avant le classement
        # for rec in tab2opt:
        #     print(rec[2].sol,' ,beta: ',rec[3],' ,fo: ',rec[0])
        res = sorted(tab2opt, key = itemgetter(0))
        # afficher apres le classement
        print('***')
        iii=0
        for rec in res:
            iii+=1
            if iii<len(tab2opt):
                print(rec[2].sol, ' ,beta: ', rec[3], ' ,fo: ', rec[0],"(x,y)-(x,y) :",tab2opt[iii][1])
        print('***')
        # min fo in tab2opt
        d_voisine=copy.deepcopy(res[0][0])

        ind_voisine=copy.deepcopy(res[0][2])
        # mise a jour (meilleur solution)
        T = round(T0 * np.exp(-t / tau), nvav)
        if d_voisine < best_sol:
            best_sol = copy.deepcopy(ind_voisine.fo)
            best_ind = copy.deepcopy(ind_voisine)
            print('best_sol:',best_sol)
        
        if d_voisine < d_courante:
             d_courante =copy.deepcopy( d_voisine)
             ind_courante = copy.deepcopy(ind_voisine)
             inv = 1
             k += 1
        else:
            #T = round(T0 * np.exp(-t / tau), nvav)
            for i_res in res:
                d_voisine=i_res[0]
                dE =   d_voisine-d_courante
                p = round(np.exp(-dE / T),nvav)
                beta=i_res[3]

                pass
                if beta > p or dE==0:
                    # if beta > p or dE == 0:
                    pass
                    #  nouveau solution est rejeter
                else:

                    print("p :",p)
                    print("beta :", beta)
                    print("temperature :",T)

                    d_courante = i_res[0]
                    ind_courante = copy.deepcopy(i_res[2])
                    inv = 1
                    k += 1
                    break
                # abaisser la temperature =======> refroidissment
                t += 1
                print("T=", T)
        # affichage des resultat finaux
        # print("cout du chemin de distance du chemin voisin = ", ind_courante.fo, "chemin hamilto voisin = ", ind_courante.sol)
        pass
    return best_ind
    # return ind_courante
if __name__ == "__main__":
    ind=individu()
    ind=recuit_simule(ind)
    ind.calc_fo()
    print('___________________________')
    print(ind.fo)
    print(ind.sol)




