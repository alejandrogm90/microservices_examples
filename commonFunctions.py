#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


def myError(mensaje, numero):
    print(mensaje)
    exit(numero)


def isDate(cadena):
    if len(cadena) != 10:
        print("10")
        return False
        
    if cadena[4] != "-" or cadena[7] != "-":
        print("-")
        return False

    try:
        anno = int(cadena[0:4])
        mes = int(cadena[5:7])
        dia = int(cadena[8:10])
    except:
        return False

    if dia > 31 or dia <= 0:
        return False

    if mes > 12 or mes <= 0:
        return False

    if anno < mes or anno < dia:
        return False

    return True

