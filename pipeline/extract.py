import pandas as pd


def read_csv_file(file_name):
  df = pd.read_csv("data/input/" + file_name, encoding="utf-8-sig", dtype=str).fillna("")
  df.columns = df.columns.str.strip().str.lower()
  return df


def extract_data():
  customers = read_csv_file("customers.csv")
  accounts = read_csv_file("accounts.csv")
  branches = read_csv_file("branches.csv")
  transactions = read_csv_file("transactions.csv")
  loans = read_csv_file("loans.csv")
  return customers, accounts, branches, transactions, loans