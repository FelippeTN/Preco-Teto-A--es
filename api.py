from fastapi import FastAPI, HTTPException
import uvicorn
from formulas import stock_info, bazin, graham
from schema import StockName

app = FastAPI(title="FastAPI Endpoint")

@app.post("/formula", response_model=dict)
async def formula_apply(stock: StockName):
    try:
        preco_atual, lpa, vpa, dpa_medio_anual = stock_info(stock.ticker_name)
        
        result_bazin = bazin(dpa_medio_anual)
        result_graham = graham(lpa, vpa)
        
        return {
            "ticker": stock.ticker_name,
            "current_price": preco_atual,
            "result_bazin": result_bazin,
            "result_graham": result_graham
        }
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)