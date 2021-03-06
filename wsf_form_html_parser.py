from HTMLParser import HTMLParser
from sys import *
import os.path

def PrintHelp():
    print "This tool help for extract all Input informations in HTML Form!\n"
    print "Example: %s file.html\n" %argv[0]

def WriteOutput(write_output):
    if(os.path.isfile('exploit') == False):
        output = file('exploit', 'w')
        output.write('[Base]\n')
        output.write('title=\n')
        output.write('description:\n')
        output.write('version=\n')
        output.write('author=\n')
        output.write('date=\n')
        output.write('type=\n\n')
        output.write('[Identifiers]\n')
        output.write('EDB=\n')
        output.write('CVE=\n\n')
        output.write('[Exploitation]\n')
        output.write('method=\n')
        output.write('url=\n\n')
        output.write('[Parameters]\n')
        output.close()
    output = file('exploit', 'a')
    output.write(write_output + '\n')
    output.close()

class WSFHTMLParser(HTMLParser):
    def handle_starttag(self, type_html, params_html):
        if type_html == 'input':
            for i in range(0,len(params_html)):
                if(params_html[i][0] == 'value'):
                    WriteOutput(params_html[i-1][1] + '=' + params_html[i][1])

print "WordPress Sploit Framework - Exploit Creator - V1.0\n"
if(len(argv) < 2):
    PrintHelp()
else:
    if(os.path.isfile(argv[1]) == False):
        print 'Error: No file exist!'
        exit()
    file_html = file(argv[1], 'r')
    html = WSFHTMLParser()
    html.feed(file_html.read())
    file_html.close()
    print "Success: File %s parsed!" % argv[1]