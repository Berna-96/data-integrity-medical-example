import pandas as pd

def validate_age(df):
    invalid_mask = (df["age"] < 0) | (df["age"] > 120)
    df.loc[invalid_mask, "age"] = pd.NA
    return df

def validate_weight(df):
    invalid_mask = (df["weight"] <= 0) | (df["weight"] > 300)
    df.loc[invalid_mask, "weight"] = pd.NA
    return df
