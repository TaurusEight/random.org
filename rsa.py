#!/usr/bin/python3
# Time-stamp: <2018-08-19 11:49:00 daniel>

#
# Generate an RSA key pair using random.org
#
# by Daniel Mendyke [daniel@mendyke.com], Aug 19, 2018
#

#
# Requied Modules
from randorg import Integers
from Crypto.PublicKey import RSA

#
# Generate RSA keys from random.org
class RSA( object ) :

  KEY = "1b1ab23b-c138-40f2-99d7-d09e3319d332"

  #
  # Constructor
  def __init__( self ) :

    value = Integers( RSA.KEY, id = 1, num = 3, min = 0 )
    private_key = RSA.construct( ( value[ 0 ], value[ 1 ], value[ 2 ] ) )
    public_key = private_key.publickey()

    print( private_key )
    print( public_key )

if __name__ == "__main__" :
  rsa = RSA()
