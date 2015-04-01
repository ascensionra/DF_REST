"""Define a group of functions to facilitate using the Dream Factory
RESTful API"""
import requests,json,sys

def getToken(url,header,data):
	""" Creates a new session, updates the header with the session 
token, and returns the request response """
	try:
		r=requests.post(url,headers=header,data=json.dumps(data))
		header['X-DreamFactory-Session-Token']=r.json()['session_id']
	except requests.exceptions.RequestException,e:
		print 'Token request failed: %s' % (e)
		return
	except ValueError,e:
		print 'Decoding JSON has failed: %s' % (e)
		return
	except BaseException,e:
		print e
		return
	return r

def delToken(url,header):
	""" Sends DELETE request to remove the session token from DF, 
removes token from header, and returns request response """
	try:
		r=requests.delete(url,headers=header)
		del header['X-DreamFactory-Session-Token']
	except requests.exceptions.RequestException,e:
		print e
		return
	except KeyError,e:
		print 'There is no token %s in the provided headers' % (e)
		return
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
		return
	return r

def newGetRequest(url,header):
	""" Submits GET request and returns response  """
	try:
		r=requests.get(url,headers=header)
	except requests.exceptions.RequestException,e:
		print 'Your request failed: %s' % (e)
		return
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
	return r

def newPutRequest(url,header):
	""" Submits PUT request and returns response """
	try:
		r=requests.put(url,headers=header)
	except requests.exceptions.RequestException,e:
		print 'Your request failed: %s' % (e)
		return
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
	return r

def newPostRequest(url,header):
	""" Submits POST request and returns response """
	try:
		r=requests.post(url,headers=header)
	except requests.exceptions.RequestException,e:
		print 'Your request failed: %s' % (e)
		return
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
	return r

def newPostRequestParams(url,header,parameters):
	""" Submits POST request with paramters and returns response """
	try:
		r=requests.post(url,headers=header,data=json.dumps(parameters))
	except requests.exceptions.RequestException,e:
		print 'Your request failed: %s' % (e)
		return
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
	return r

def printJson(response):
	""" Prints JSON dictionary of a successful 
response in a nice format """
	try:
		print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
	except ValueError,e:
		print 'Decoding JSON has failed: %s' % (e)
	return

def writeJson(response,filename):
	""" Writes JSON dictionary of a successful
response in a nice format to a file """
	try:
		with open(filename,'w') as f:
			f.write(json.dumps(response.json(),sort_keys=True, indent=4, separators=(',', ': ')))
	except IOError,e:
		print "I/O error ((0)): (1)".format(e.errno, e.strerror)
	except BaseException,e:
		print 'Undexpected error: %s' % (e)
	return

def tallyRecords(response,field):
	""" Puts unique field into dictionary and increments count on subsequent
occurrences to produce a tally of hits for that field. This does not work with lists yet,
so printing store procedures responses in array or list form will not work. """
	try:
		newDict = {}
		for i in response.json()['record']:
			if not i[field] in newDict:
				newDict[i[field]] = 1
			else:
				newDict[i[field]] += 1
	except KeyError,e:
		print 'There is a problem with the dictionary key: %s' % (e)
		return
	except ValueError,e:
		print 'There is a prolem with the dictionary value: %s' % (e)
		return
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
		return
	return newDict

def printDict(dictionary,sortVal):
	""" Prints out the contents of a dictionary in a nice format
using OrderedDict from collections to sort the dict.""" 
	from collections import OrderedDict as OD
	try:
		if (sortVal.upper() == 'K' or sortVal.upper() == 'KEY'):
			ordered = OD(sorted(dictionary.items(), key = lambda t: t[0]))
		else:
			ordered = OD(sorted(dictionary.items(), key = lambda t: t[1], reverse=True))
		for key in ordered:
			print '%s: %s' % (key,ordered[key])
	except BaseException,e:
		print 'Unexpected error: %s' % (e)

def writeDict(dictionary,filename):
	""" Uses pretty print to write a dictionary's contents to
specified file, sorted."""
	from pprint import pprint
	try:
		with open(filename,'w') as f:
			pprint(dictionary,f)
	except IOError,e:
		print "I/O error((0)): (1)".format(e.errno, e.strerror)
	except BaseException,e:
		print 'Unexpected error: %s' % (e)
	finally:
		f.close()

if __name__ == '__main__':
	# Do some stuff
	print "This is dfmod.py"
