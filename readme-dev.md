# Cosie.me

## Local dev

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
