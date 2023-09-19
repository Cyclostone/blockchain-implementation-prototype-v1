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

**Run a peer instance**

```
export PEER=True && python -m backend.app
```

**Run the frontend**

In the frontend directory:

```
npm run start
```

**Seed the backend with data**

This command is for windows powershell

```
$env:SEED_DATA='True'; python -m backend.app
```
