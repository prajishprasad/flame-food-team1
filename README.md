# FLAME Food App

A deliberately small Flask app used in **CSIT306 — Software Architecture and Engineering**
for the version-control session (S3).

Three cafes, a menu each, a session-backed cart, and a checkout that clears it.
That is the whole application, and it is meant to stay small enough to hold in your head.

## Run it

You need Python 3 and Git (Step 0 of the course setup guide).

```bash
git clone <your-team's-repo-url>
cd FLAME-food-app

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in a browser.

**Before you change anything, click through all three cafes, add items to the cart,
and check out.** You need to know what "working" looks like, because you will be
asked later whether it still does.

## For the in-class activity

Your tasks are in [`TASKS.md`](TASKS.md). Read that file next.

## Licence

MIT — see [LICENSE](LICENSE). You may copy, modify and build on this freely.
