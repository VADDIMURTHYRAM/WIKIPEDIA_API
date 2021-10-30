import streamlit as st
import pandas as pd
import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route('/')
def run_script():
    file = open(r'/streamlitt_app.py', 'r').read()
    return exec(file)

if __name__ == "__main__":
    app.run(debug=True)
