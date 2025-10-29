from fastapi import FastAPI
from route import router as api_router
import uvicorn
from middleware.auth import verify_token

app = FastAPI(
    title="Dayta Backend",
    description="""This backedn contains all the logic to buy and sell your
    mobile data provded you have a provider. An open source project feel free
    to use! """,
)

app.middleware("http")(verify_token)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "working dayta"}


def main():
    print("Hello from dayta-backend!")
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()
