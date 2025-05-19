from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Metreyar API"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "size": len(content)}

@app.get("/upload-form", response_class=HTMLResponse)
async def upload_form():
    return """
    <html>
        <body>
            <h2>آپلود فایل متره</h2>
            <form action="/upload/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """
