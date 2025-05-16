"""
<Assignment 2>


Copyright (c) 2021
Licensed
Written by <Xinhang Li>
"""

def image(image_name):
    from IPython.display import display, Image
    a = display(Image(filename=image_name))
    return a

def csv(csv_name):
    import pandas as pd
    df = pd.read_csv(csv_name)
    return df
    
def excel(excel_name):
    import pandas as pd
    df_excel = pd.read_excel(excel_name)
    return df_excel

def html(html_name):
    from bs4 import BeautifulSoup
    page = open(html_name).read()
    soup = BeautifulSoup(page, 'html.parser')
    return soup 
    
def json(json_name):
    import json 
    f = open(json_name,) 
    data = json.load(f) 
    return data
    
def SQLite(SQLite_name):
    from sqlalchemy import create_engine
    db = create_engine(SQLite_name)
    return db

if __name__ == "__main__":
    image(image_name = 'hw2_data\\atlas.png')