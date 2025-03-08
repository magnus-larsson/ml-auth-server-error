About venv: https://medium.com/@sukul.teradata/understanding-python-virtual-environments-using-venv-and-virtualenv-283f37d24b13

About testing dynamic web pages: https://www.zenrows.com/blog/dynamic-web-pages-scraping-python#scraping-dynamic-web-pages-in-python-using-selenium

About "Chrome for Testing": https://wikomtech.com/blog/chrome-for-testing-browser-use-case-with-selenium-in-python/

Create venv

    python3 -m venv env

Activate venv

    source ./env/bin/activate

Deactivate venv

    deactivate

Install requirements:

    pip install --upgrade pip
    pip3 install -r requirements.txt

Run:

    python3 test-openapi-ui.py
