from fastapi import FastAPI, UploadFile, File
import pandas

app = FastAPI()

@app.post("/")
async def creat_upload_file(file: UploadFile = File(...)):
    df = pandas.read_csv(file.file)
    data_list = df.to_dict(orient='records')

    result = {"data": data_list}

    return result
