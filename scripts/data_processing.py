#! /usr/bin/python3
#created by: aime nishimwe
#created at: Avery Hall, UNL
#created on: March 17, 2022

#library imports
import pandas as pd
import numpy as np
from data_load import data_extract

def preprocess():
    df = data_extract()
    df['filename'] = df.apply(lambda x: x['new_path'] if x['new_path'] else x['old_path'], axis =1)
    df['module']   = df.filename.apply(lambda x: "/".join(x.split("/")[:-1]))
    df['churn']    = df.added_lines + df.removed_lines
    df = df[df.module != '']
    return df[['module','commit_hash','churn']]

def active_modules(df):
    df = df.groupby('module', as_index = False).count()
    df = df.sort_values('commit_hash',ascending = False).head(12)
    return df[['module','commit_hash']]

def churn_rate(df):
    df = df.groupby('module', as_index = False).sum()
    df = df.sort_values('churn', ascending = False)
    return df

def clean_data():
    df = preprocess()
    return (active_modules(df), churn_rate(df))

if __name__ == "__main__":
    active_mod, churn_rate = clean_data()
