# Cosie.me

## Local dev

```python
# sample hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/{who}")
def say_hi(who: str):
    if not who:
        return {"message": "Hello, World!"}
    return {"message": f"Hello, {who}!"}
```

In the python file, you can add:

```python
if __name__ == "__main__":
    uvicorn.run("hello:app", port=8000, reload=True)
```

Then run the file:

```bash
python hello.py
```

or you can use `uvicorn` to run the file:

```bash
uvicorn hello:app --reload
```

Then you can test the api:

```bash
http localhost:8000/hi
```

```python
>>> import requests
>>> requests.get("http://localhost:8000/hi").json()
{'message': 'Hello, World!'}
```

## Deploy fastapi app to vercel

You need to also add a `vercel.json` file to the root of the project:

```json
{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

To deploy the app to vercel, you need to run the following commands:

```bash
# make sure you have vercel installed
npm install -g vercel
vercel login
# deploy to dev to preview
vercel .
# deploy to prod if everything is good
vercel --prod
```
