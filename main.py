
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from vpic import VpicApiClient
import sqlite3
import uvicorn
import pandas as pd
from fastparquet import write

def get_columns():
    columns = ["VIN", "Make", "Model", "Model_Year", "Body_Class", "Cached_Result"]
    return columns

app = FastAPI()

# Initialize VPIC API client
vpic_client = VpicApiClient()

# Initialize SQLite connection and cursor
conn = sqlite3.connect("cache.db")
cursor = conn.cursor()

# Create cache table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS cache (
        vin TEXT PRIMARY KEY,
        make TEXT,
        model TEXT,
        model_year TEXT,
        body_class TEXT,
        cached_result BOOLEAN
    )
    """
)


@app.get("/lookup/{vin}")
async def lookup_vin(vin: str):
    '''
    The lookup endpoint checks to see if an entry is already in the cache, and if it isn't we reach out to the vPIC API
    to pull details about the vehicle. 
    Input: 17 character string VIN
    Output: Vehicle details
    '''
    # FIRST - sanity check - is the string 17 chars exactly?
    if len(vin) != 17:
        raise HTTPException(400)
    elif " " in vin:
        raise HTTPException(400)
    elif not vin.isalnum():
        raise HTTPException(400)
    
    # Check if VIN exists in cache
    cursor.execute("SELECT VIN,Make,Model,Model_Year,Body_Class,Cached_Result FROM cache WHERE vin=?", (vin,))
    result = cursor.fetchone()

    if result:
        # VIN found in cache, return cached data
        result_with_columns = dict(zip(get_columns(), result))

        return JSONResponse(content=result_with_columns)

    # VIN not found in cache, fetch data from VPIC API
    try:
        data = vpic_client.lookup(vin)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve data from VPIC API")

    # Cache the data
    vin = data['VIN']
    make = data['Make']
    model = data['Model']
    model_year = data['ModelYear']
    body_class = data['BodyClass']
    cached_result = True
    cursor.execute("INSERT INTO cache (vin, make, model, model_year, body_class, cached_result) VALUES (?, ?, ?, ?, ?, ?)", (vin, make, model, model_year, body_class, cached_result))
    conn.commit()

    vehicle = dict(zip(get_columns(),[vin,make,model,model_year,body_class,cached_result]))

    return JSONResponse(content=vehicle)


@app.get("/export")
async def export_cache():
    '''
    The export endpoint will fetch all data from the cache and export it to a parquet format file
    which will be written to disk as export_file.parquet
    Input: n/a
    Output: File in parquet format
    '''
    # Retrieve all records from cache
    cursor.execute("SELECT * FROM cache")
    results = cursor.fetchall()

    cache_contents = {result[0]: result[1] for result in results}
    print(cache_contents)

    json_response = JSONResponse(content=cache_contents)

    columns = get_columns()

    store = pd.DataFrame(cache_contents, columns=columns)

  
    write('export_file.parquet', store)
   
@app.get("/delete/{vin}")
async def delete_record(vin: str):
    '''
    The delete endpoint deletes a VIN from the cache if it is found there.
    Input: 17 character VIN
    Output: A response indicating success or failure if the record wasn't there at all
    '''
    # Delete record from cache
    cursor.execute("DELETE FROM cache WHERE vin=?", (vin,))
    conn.commit()

    # Check if any records were deleted
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Record not found")

    return JSONResponse(content={"message": "Record deleted successfully"})


# Close SQLite connection when the app stops
@app.on_event("shutdown")
def shutdown():
    conn.close()



# Entry
if __name__ == "__main__":

    # Run app 
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)

