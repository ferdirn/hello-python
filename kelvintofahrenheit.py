#!/usr/bin/env python

def KelvinToFahrenheit(temperature):
    assert (temperature >= 0), "Colder than absolute zero!"
    return ((temperature-273)*1.8)+32

print KelvinToFahrenheit(273)
print KelvinToFahrenheit(-5)


