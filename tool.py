import os
import re
import argparse
from  concurrent.futures import ThreadPoolExecutor
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.markdown import Markdown
from rich.console import Console
from rich import print
from Mods.urlencode import *
from Mods.header import *
from Mods.potocol import *
from Mods.ports import *
from Mods.modsqli import *

console = Console()

parser = argparse.ArgumentParser(description="Universal Bypasser tool Help Menu")
parser.add_argument('-U', '--url', metavar='', required=True, help="Enter the url to scan")
parser.add_argument('-H', '--header', action="store_true", required=False, help="Use this for Http header Bypass")
parser.add_argument('-J', '--protocol', action="store_true", required=False, help="Use this for Http protocol Bypass")
parser.add_argument('-P', '--port', action="store_true", required=False, help="Use this for port Bypass")
parser.add_argument('-K', '--encode', action="store_true", required=False, help="Use this for url encode/403 Bypass")
parser.add_argument('-M', '--mod', action="store_true", required=False, help="Use this for mod security Bypass")
parser.add_argument('-A', '--all', action="store_true", required=False, help="Use this for All Bypass")

args = parser.parse_args()

urls = args.url

term_size = os.get_terminal_size().columns
captions = '''
This tool use for bypassing 401/403, http method, httpprotocol
'''
caption2 = "A Fast 401/403 Bypasser Author [0xAgun]"
pixels1 = (term_size//2)-(len(captions)//2)
pixels2 = (term_size//2)-(len(caption2)//2)


space = "&nbsp;"
title = f'''
 {space*pixels1}{captions}{space*pixels1}\n
 {space*pixels2}{caption2}
'''
note = f'''
# Universal Bypasser
{title}
1. bypass 401 status
2. bypass 403 status
3. bypass http header


'''
sub = "subtitle"

markdown = Markdown(note, style="white")
console.print(Panel(markdown, title="Welcome", subtitle="0xAgun", box=box.HEAVY, style="blue"))

enc = '''

╦ ╦╦═╗╦    ╔═╗┌┐┌┌─┐┌─┐┌┬┐┌─┐  ╔╗ ┬ ┬┌─┐┌─┐┌─┐┌─┐
║ ║╠╦╝║    ║╣ ││││  │ │ ││├┤   ╠╩╗└┬┘├─┘├─┤└─┐└─┐
╚═╝╩╚═╩═╝  ╚═╝┘└┘└─┘└─┘─┴┘└─┘  ╚═╝ ┴ ┴  ┴ ┴└─┘└─┘



'''


hd = '''
    ╦ ╦╔╦╗╔╦╗╔═╗  ╦ ╦┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔╗ ┬ ┬┌─┐┌─┐┌─┐┌─┐
    ╠═╣ ║  ║ ╠═╝  ╠═╣├┤ ├─┤ ││├┤ ├┬┘  ╠╩╗└┬┘├─┘├─┤└─┐└─┐
    ╩ ╩ ╩  ╩ ╩    ╩ ╩└─┘┴ ┴─┴┘└─┘┴└─  ╚═╝ ┴ ┴  ┴ ┴└─┘└─┘`

'''

mt = '''


╦ ╦╔╦╗╔╦╗╔═╗  ╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐  ╔╗ ┬ ┬┌─┐┌─┐┌─┐┌─┐
╠═╣ ║  ║ ╠═╝  ║║║├┤  │ ├─┤│ │ ││  ╠╩╗└┬┘├─┘├─┤└─┐└─┐
╩ ╩ ╩  ╩ ╩    ╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘  ╚═╝ ┴ ┴  ┴ ┴└─┘└─┘



'''

pot = '''



╔═╗┌─┐┬─┐┌┬┐  ╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐  ╔╗ ┬ ┬┌─┐┌─┐┌─┐┌─┐
╠═╝│ │├┬┘ │   ║║║├┤  │ ├─┤│ │ ││  ╠╩╗└┬┘├─┘├─┤└─┐└─┐
╩  └─┘┴└─ ┴   ╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘  ╚═╝ ┴ ┴  ┴ ┴└─┘└─┘


'''

mod = '''


┌┬┐╔═╗╔╦╗  ┌─┐╔═╗╔═╗  ╔╗ ┬ ┬┌─┐┌─┐┌─┐┌─┐
│││║ ║ ║║  └─┐║╣ ║    ╠╩╗└┬┘├─┘├─┤└─┐└─┐
┴ ┴╚═╝═╩╝  └─┘╚═╝╚═╝  ╚═╝ ┴ ┴  ┴ ┴└─┘└─┘



'''

patt = "[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?"

mtc = re.search(patt, urls)

reurl = mtc.group()

if args.encode:
    print(enc)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            argk = ((urls, etx) for etx in payload1.exten)
            pool.map(lambda p: payload1.payloads1(*p), argk)


if args.header:
    print(hd)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            for x in payload2.mans:
                headers = {x:'127.0.0.1, 68.180.194.242'}
                pool.submit(payload2.payloads1,urls,headers)


if args.protocol:
    print(mt)
    payload3.payloads1(urls,reurl)


if args.port:
    print(pot)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            for x in payload4.port:
                headers = {"X-Forwarded-Port": x}
                pool.submit(payload4.payloads1,urls,headers)


if args.mod:
    print(mod)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            for x in payload5.pays:
                pool.submit(payload5.payloads1,urls,x)

#-----------------------------------------------------------------------------------
if args.all:
    print(enc)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            argk = ((urls, etx) for etx in payload1.exten)
            pool.map(lambda p: payload1.payloads1(*p), argk)
    print(hd)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            for x in payload2.mans:
                headers = {x:'127.0.0.1, 68.180.194.242'}
                pool.submit(payload2.payloads1,urls,headers)

    print(mt)
    payload3.payloads1(urls,reurl)

    print(pot)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            for x in payload4.port:
                headers = {"X-Forwarded-Port": x}
                pool.submit(payload4.payloads1,urls,headers)

    print(mod)
    if __name__ == "__main__":
        with ThreadPoolExecutor(40) as pool:
            for x in payload5.pays:
                pool.submit(payload5.payloads1,urls,x)
