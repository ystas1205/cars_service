

import uvicorn
from fastapi import FastAPI, Depends


from cars_api.router import router as router_cars

app = FastAPI(title="API cars")

app.include_router(router_cars)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
