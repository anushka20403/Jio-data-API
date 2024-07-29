import pandas as pd
import functions
from fastapi import FastAPI, HTTPException, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
import uvicorn
from typing import Optional, Union

app=FastAPI()
subapi=FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@subapi.get("/stats")
async def Display(value: Union[int, None] = None, pg_name: Union[str, None] = Query(default=None)):
    print(f"Received request with value={value} and pg_name={pg_name}")
    
    try:
        df = pd.read_csv('myjio_tdata.csv')
        print("CSV file loaded successfully")
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error reading CSV file: {str(e)}")
        
    if value == 1:
        try:
            result = functions.PeakTime(df)
            peak = result[1]
            return {'Peak Time': peak}
        except Exception as e:
            print(f"Error processing PeakTime: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing Peak Time")
        
    elif value == 2:
        try:
            result = functions.max5PayMode(df)
            return result.to_dict('records')  # Use 'records' instead of 'r'
        except Exception as e:
            print(f"Error processing max5PayMode: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing Top 5 Payment Modes")
        
    elif value == 3:
        try:
            result = functions.max5PG(df)
            return result.to_dict('records')  # Use 'records' instead of 'r'
        except Exception as e:
            print(f"Error processing max5PG: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing Top 5 Payment Gateways")
        
    elif value == 4:
        try:
            result = functions.PGwise(df)
            return result.to_dict('records')  # Use 'records' instead of 'r'
        except Exception as e:
            print(f"Error processing PGwise: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing PG Wise Recharge Count")
        
    elif value == 5:
        try:
            result = functions.PG(df)
            if pg_name is None:
                return result.to_dict('records')  # Use 'records' instead of 'r'
            elif not result['PG_NAME'].isin([pg_name]).any():
                print(f"PG_NAME {pg_name} not found in result")
                raise HTTPException(status_code=404, detail="PG not found")
            else:
                y = result.loc[result['PG_NAME'] == pg_name]
                return y.to_dict('records')  # Use 'records' instead of 'r'
        except Exception as e:
            print(f"Error processing PG Info: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing PG Info")
        
    elif value == 6:
        try:
            result = functions.timebased(df)
            return result.to_dict('records')  # Use 'records' instead of 'r'
        except Exception as e:
            print(f"Error processing timebased analysis: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing Time Based Analysis")
        
    elif value == 7:
        try:
            result = functions.PayWise(df)
            return result.to_dict('records')  # Use 'records' instead of 'r'
        except Exception as e:
            print(f"Error processing PayWise: {str(e)}")
            raise HTTPException(status_code=500, detail="Error processing PM Wise Recharge Count")
        
    else:
        print(f"Invalid value parameter: {value}")
        raise HTTPException(status_code=400, detail="Invalid value parameter")


app.mount("/jiodata", subapi)

if __name__ == "__main__":
    config = uvicorn.Config(app, host='0.0.0.0', port=9898, log_level="info")
    server = uvicorn.Server(config)
    server.run()
