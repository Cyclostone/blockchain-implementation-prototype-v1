**Activate the Virtual Environment**
```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual env (optional in my case)

```
python -m pytest backend/tests
```

**Run the Flask Application/API**

```
python -m backend.app
```