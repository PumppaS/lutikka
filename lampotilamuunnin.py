#!/usr/bin/python
#-*- coding: utf-8 -*-
#import os, sys
#Ryhmä Lutikka
######################################################################
##kirjasto
######################################################################
#muuntokaavat
#Yhteensopiva Python3.0+ kanssa (print kusee muuten osittain, sa korjata)
def c2f(celsius):
      fahrenheit= (celsius*1.8) +32
      return fahrenheit 
def c2k(celsius):
      kelvin= celsius +273.15
      return kelvin
def f2k(fahrenheit):
      kelvin = (fahrenheit +459.67)/1.8
      return kelvin
def f2c(fahrenheit):
      celsius = (fahrenheit -32)/1.8            #toteuttanut ryhmä Valuuttamuunnin
      return celsius
def k2c(kelvin):
      celsius = kelvin - 273.15			#toteuttanut ryhmä sananmuunnin
      return celsius
def k2f(kelvin):      
      fahrenheit = (kelvin*1.8)-459.67
      return fahrenheit      

##valikko
def valikko():
      print("Mistä mihin haluat muuntaa?")
      print("1) Celsius->Fahrenheit")
      print("2) Celsius->Kelvin")
      print("3) Fahrenheit->Kelvin")
      print("4) Fahrenheit->Celsius")
      print("5) Kelvin->Celsius")
      print("6) Kelvin->Fahrenheit")
      print("0) Lopeta")
##pääohjelma
def main():
      while(True):
            valikko()
            valinta= int(input("Valintasi: "))
            if (valinta==0):
                break
            elif (valinta==1):             
                  aste=float(input("Anna lähtölämpötila: "))
                  muunnos=c2f(aste)
                  print("Lämpötila fahrenheit asteina:", round(muunnos, 2))
            elif (valinta==2): 
                  aste=float(input("Anna lähtölämpötila: "))
                  muunnos=c2k(aste)
                  print("Lämpötila kelvin asteina:", round(muunnos, 2))
            elif (valinta==3): 
                  aste=float(input("Anna lähtölämpötila: "))
                  muunnos=f2k(aste)
                  print("Lämpötila kelvin asteina:", round(muunnos, 2))
            elif (valinta==4):#valinta toimii mutta toiminallisuus puuttuu
                  aste=float(input("Anna lähtölämpötila: "))
                  muunnos=f2c(aste)
                  print("Lämpötila celsius asteina:", round(muunnos, 2))
            elif (valinta==5):
                  aste=float(input("Anna lähtölämpötila: "))
                  muunnos=k2c(aste)
                  print("Lämpötila celsius asteina:", round(muunnos, 2))
            elif (valinta==6):              
                  aste=float(input("Anna lähtölämpötila: "))
                  muunnos=k2f(aste)
                  print("Lämpötila fahrenheit asteina:", round(muunnos, 2))
main()
 

######################################################################
# eof 
