"""Define a group of functions to facilitate using the Dream Factory
RESTful API"""
import requests,json,sys

def getToken(url,header,data):
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
		print 'Undefined error: %s' % (e)
		return
	return r

if __name__ == '__main__':
	# Do some stuff
	print "This is dfmod.py"
