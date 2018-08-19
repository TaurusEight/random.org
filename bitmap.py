#!/usr/bin/python3
# Time-stamp: <2018-08-19 11:25:58 daniel>

#
# Generate a random RGB bitmap that is 128x128 pixels using
# random number generated at 'random.org'
#
# by Daniel Mendyke [daniel@mendyke.com], Aug 19, 2018
#

#
# Required modules
from randorg import Integers
from PIL import Image
import os
from stat import ST_SIZE

#
# Create and store the bitmap
class Bitmap( object ) :

  KEY = "1b1ab23b-c138-40f2-99d7-d09e3319d332"

  #
  # Constructor
  # Code to create a BMP file modified from code found on stackoverflow
  # https://stackoverflow.com/questions/38697787/create-bmp-file-of-given-size-in-python-3
  def __init__( self ) :
    print( 'Bitmap.__init__' )

    pixel = self.generate_pixels()
    print( pixel )
    self.img = Image.new( 'RGB', ( 128, 128 ), "white" )
    image_pixels = self.img.load()

    count = 0
    for i in range( self.img.size[ 0 ] ) :
      for j in range( self.img.size[ 1 ] ):
        image_pixels[ i, j ] = ( i, j, pixel[ count ] )
        count = count + 1
    self.img.save( "some.bmp" )

  #
  # Use random.org to generate all the values for the RGP bitmap
  # There is a limit to the number of values that can be generated per request
  # to random.org so the requests have to be split into two
  def generate_pixels( self ) :
    first = Integers( key = Bitmap.KEY, id = 15, min = 0, max = 255, num = 9984 )
    second = Integers( key = Bitmap.KEY, id = 16, min = 0, max = 255, num = 6400 )
    return first.value + second.value

if __name__ == "__main__" :
  bmp = Bitmap()
