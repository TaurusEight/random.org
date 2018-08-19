#!/usr/bin/python3
# Time-stamp: <2018-08-19 11:52:30 daniel>

#
# Generate a WAV file of random white noise from random.org
#
# by Daniel Mendyke [daniel@mendyke.com] Aug 19, 2018

#
# Required Modules
import wave



#
# Create the wav file
class Wav( object ) :

  #
  # Constructor
  def __init__( self ) :
    print( 'Wav constructor' )


if __name__ == "__main__" :
  wav = Wav()
