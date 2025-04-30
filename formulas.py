import math
import yfinance as yf
import pandas as pd


lista_acoes =["BBAS3", "TAEE4", "KLBN4", "VALE3", "BBDC4", "TASA4", "ISAE4"]
for acao in lista_acoes:
    ticker = yf.Ticker(f"{acao}.SA")

    preco_atual = ticker.history(period="1d")["Close"].iloc[-1]
    info = ticker.info
    lpa = info.get("trailingEps")
    vpa = info.get("bookValue")
    dividendos_history = ticker.dividends
    dividendos_history.index = dividendos_history.index.tz_localize(None)

    limite = pd.Timestamp.now() - pd.DateOffset(years=10)
    dividendos_filtrados = dividendos_history[dividendos_history.index >= limite]

    dividendos_anuais = dividendos_filtrados.groupby(dividendos_filtrados.index.year).sum()
    dpa_medio_anual = dividendos_anuais.mean().item()

    def bazin(DPA):
        return DPA / 0.06

    def graham(LPA, VPA):
        return math.sqrt(22.5 * LPA * VPA)


    result_bazin = bazin(dpa_medio_anual)
    result_graham = graham(lpa, vpa)

    print(acao)
    print(f"Preço Atual: {preco_atual}\nFórmula Bazin: {result_bazin}\nFórmula Graham: {result_graham}")