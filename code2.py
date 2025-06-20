import urllib.request
import json

def fetch_price(symbol):
    """
    Fetch current price for a given ticker symbol using Yahoo Finance unofficial API.
    """
    url = ("https://query1.finance.yahoo.com/v7/finance/quote?symbols=",symbol)
    with urllib.request.urlopen(url) as resp:
        data = json.loads(resp.read().decode())
        quote = data["quoteResponse"]["result"]
        if quote:
            return float(quote[0].get("regularMarketPrice", 0))
    return None
class Portfolio:
    def __init__(self):
        self.holdings = {}  # symbol -> shares held

    def buy(self, symbol, shares):
        self.holdings[symbol] = self.holdings.get(symbol, 0) + shares

    def sell(self, symbol, shares):
        if symbol not in self.holdings or self.holdings[symbol] < shares:
            print("Error: Not enough shares to sell",shares,symbol)
            return
        self.holdings[symbol] -= shares
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]

    def total_value(self):
        total = 0.0
        details = []
        for sym, qty in self.holdings.items():
            price = fetch_price(sym)
            if price is None:
                print("Warning: Couldn't fetch price for", sym)
                continue
            value = price * qty
            total += value
            details.append((sym, qty, price, value))
        return total, details
def main():
    pf = Portfolio()
    while True:
        cmd = input("Enter command (BUY/SELL/SHOW/QUIT): ").strip().upper()
        if cmd == "QUIT":
            break
        elif cmd in ("BUY", "SELL"):
            sym = input("Ticker symbol: ").strip().upper()
            qty = int(input("Shares: "))
            if cmd == "BUY":
                pf.buy(sym, qty)
            else:
                pf.sell(sym, qty)
        elif cmd == "SHOW":
            total, details = pf.total_value()
            print("\nYour Portfolio:")
            print("%-8s%6s%12s%14s" % ("Ticker", "Qty", "Price", "Value"))
            print("-" * 42)
            for sym, qty, price, val in details:
                sym_str   = str(sym).ljust(8)
                qty_str   = str(qty).rjust(6)
                price_str = ("{:.2f}".format(price)).rjust(12)
                val_str   = ("{:.2f}".format(val)).rjust(14)

                print(sym_str + qty_str + price_str + val_str)

                
            print("-" * 42)
            label   = "TOTAL".ljust(26)
            total_str = "{:.2f}".format(total)
            total_str = total_str.rjust(14)
            print(label + total_str + "\n")
        else:
            print("Unknown command.")
