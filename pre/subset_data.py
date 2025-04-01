import pandas as pd

housing = pd.read_csv("housing.csv")

housing = housing.sample(n=10000, replace=False)
housing["median_income"] = housing["median_income"] * 10000

housing.to_csv("housing-subset.csv", index=False)