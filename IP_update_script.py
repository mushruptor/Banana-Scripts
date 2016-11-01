import urllib.request, json

class main():
	def __init__(self):
		sfile = 'secret'
		
		data = json.loads(urllib.request.urlopen('http://ip.jsontest.com/').read().decode('utf-8'))
		ext_ip = data['ip']

		url = 'https://nico-westerbeck.de/forwarder/'
		f = open(sfile)        
		postjson = {'secret' : f.read(), 'ip' : ext_ip}
		f.close()
		urllib.request.Request(url, postjson)

main()
