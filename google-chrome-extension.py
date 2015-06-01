import sys
import urllib2

for arg in sys.argv: #(1)
    arguments=arg.split('/')
element = len(arguments)
idExtension = (arguments[element-1].split('?'))[0]
url = "http://clients2.google.com/service/update2/crx?response=redirect&x=id%3D"+idExtension+"%26uc%26lang%3Den-US&prod=chrome"
print url
extension = urllib2.urlopen(url)
output = open('extension.crx','wb')
output.write(extension.read())
output.close()