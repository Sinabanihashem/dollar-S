import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_dollar_price():
    url = "https://dollar.api-sina-free.workers.dev/dollar"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        price_toman = data.get("price_toman")
        price_rial = data.get("price_rial")
        updated_at = data.get("updated_at")
        creator = data.get("creator")
        source = data.get("source", "tgju.org")

        if not price_toman:
            console.print("[red] داده‌ای دریافت نشد. لطفاً دوباره تلاش کنید.[/red]")
            return

        
        updated_time = datetime.fromisoformat(updated_at.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S")

        
        table = Table(title="💸 قیمت لحظه‌ای دلار آزاد", show_lines=True)
        table.add_column("فیلد", justify="right", style="cyan", no_wrap=True)
        table.add_column("مقدار", justify="left", style="bold green")

        table.add_row("💰 قیمت به تومان", f"{price_toman:,} تومان 🇮🇷")
        table.add_row("💵 قیمت به ریال", f"{int(price_rial):,} ریال")
        table.add_row("⏰ آخرین بروزرسانی", updated_time)
        table.add_row("🌐 منبع", source)
        table.add_row("👤 توسعه‌دهنده", creator)

        console.print(Panel.fit(table, border_style="green", title="SinaDollar API"))

    except requests.exceptions.Timeout:
        console.print("[red] زمان پاسخ‌گویی سرور تمام شد (Timeout).[/red]")
    except requests.exceptions.RequestException as e:
        console.print(f"[red] خطا در اتصال به سرور:\n{e}[/red]")
    except Exception as e:
        console.print(f"[red] خطای ناشناخته:\n{e}[/red]")

if __name__ == "__main__":
    get_dollar_price()
