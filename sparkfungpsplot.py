#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# geo_coords_ex1.py
#
# Simple Example for SparkFun ublox GPS products 
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, July 2020
# 
# Do you like this library? Help support SparkFun. Buy a board!
# https://sparkfun.com
#==================================================================================
# GNU GPL License 3.0
# Copyright (c) 2020 SparkFun Electronics
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#==================================================================================
# Example 1
# This example sets up the serial port and then passes it to the UbloxGPs
# library. From here we call geo_coords() and to get longitude and latitude. I've
# also included heading of motion here as well. 

import serial
import matplotlib.pyplot as plt
from ublox_gps import UbloxGps
#grabs and sets up the image to work with matplotlib (need a screenshot of google maps and to know the extent of it in lat and lon degrees)
img = plt.imread("Graph3.png")
fig, ax = plt.subplots()
ax.imshow(img, extent = [-77.08943, -77.08872, 38.93247, 38.93189])
#sets up the gps serial communications
port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)
#this function plots the lat and lon points on our graph, the pause is needed to show the points
def run():
    

    try:
        print("Listening for UBX Messages")
        while True:
            try:
                geo = gps.geo_coords()
                x = geo.lon
                print("Longitude: ", geo.lon) 
                y = geo.lat
                print("Latitude: ", geo.lat)
                print("Heading of Motion: ", geo.headMot)
                plt.scatter(x, y)
                plt.pause(.5)  
            except (ValueError, IOError) as err:
                print(err)
        

    finally:
        port.close()


if __name__ == '__main__':
    run()
plt.show()