# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:43:24 2022

@author: lab
"""
acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("El dato ingresado es un ACL Estandar")
elif acl>=1300 and acl <=1999:
    print("El dato ingresado es un ACL Expandida")
else:
    print("El # Ingresado no es de un ACL")
    
acl=int(input("Ingrese el # de ACL: "))
if acl>=100 and acl<=199:
    print("El dato ingresado es un ACL Extendida")
elif acl>=2000 and acl <=2699:
    print("El dato ingresado es un ACL Expandida")
else:
    print("El # Ingresado no es de un ACL")    

    
