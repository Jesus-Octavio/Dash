#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:42:00 2023

@author: jesus
"""
from threading import Timer
import dash
from dash import dcc
from dash import html
import pandas as pd
import webbrowser


app = dash.Dash(__name__)
app.layout = html.P("Hi")

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")
    

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(#debug=True,
               host = "127.0.0.1",
               port = "8050")