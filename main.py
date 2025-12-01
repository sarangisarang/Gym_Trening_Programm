from fastapi import FastAPI

app= FastAPI(titele="Now Api for Gym")


list={"name":"biceps","repetition":3}

@app.get("/catalog")
def catalog():
    return list

