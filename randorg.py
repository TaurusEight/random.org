# Time-stamp: <2018-08-19 11:20:56 daniel>

#
# Using the 'random.org' to generate random numbers
#
# By Daniel Mendyke - [daniel@mendyke.com]
# Aug 19, 2018
#

import json
import urllib.request

#
#
class Bounds :

  Min = -100000000
  Max = 100000000

#
# Using the API found at random.org to generate a list of random integers
class Integers( object ) :

  URL = "https://api.random.org/json-rpc/1/invoke"
  Max = 1000000000
  Min = -Max

  #
  # Constructor for this class, which using 'random.org' to generate integers
  def __init__( self, key, id, num = 1, min = Bounds.Min, max = Bounds.Max ) :

    self.key = key
    self.id = id
    self.num = num
    self.min = min
    self.max = max
    self.value = []

    try :
      request = self.create_request()
      response = urllib.request.urlopen( request )
      self.parse_response( response.read().decode( 'utf-8' ) )
    except Exception as E :
      print( E )  # end exception has been called, something went wrong


  #
  # Encode the params as a string for inclusion in the https request
  def encode_params( self ) :
    required = { "apiKey": self.key, "n": self.num,
                 "min": self.min, "max": self.max }
    params = { "jsonrpc": "2.0", "method": "generateIntegers",
               "params": required, "id": self.id }
    params_string = json.dumps( params ).encode( 'utf-8' )
    print( params_string )
    return params_string

  #
  # Create the HTTP request for 'random.org' to return a list of random integers
  def create_request( self ) :
    request = urllib.request.Request(
      Integers.URL,
      data = self.encode_params(),
      headers = { 'content-type': 'application/json-rpc' }
    )  # end request
    return request

  #
  # Parse the JSON response from random.org and store the random numbers
  def parse_response( self, response ) :
    parsed_response = json.loads( response )
    self.value = parsed_response[ 'result' ][ 'random' ][ 'data' ]
