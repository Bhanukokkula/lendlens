import duckdb

print("Connecting to DuckDB...")
con = duckdb.connect("lendlens.duckdb")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

print("Loading Fed funds rate...")
con.execute("""
    CREATE OR REPLACE TABLE raw.fedfunds AS
    SELECT * FROM read_csv_auto('data/raw/fedfunds.csv')
""")

print("Loading unemployment rate...")
con.execute("""
    CREATE OR REPLACE TABLE raw.unrate AS
    SELECT * FROM read_csv_auto('data/raw/unrate.csv')
""")

print("Loading Lending Club loans (this takes a minute)...")
con.execute("""
    CREATE OR REPLACE TABLE raw.loans AS
    SELECT * FROM read_csv(
        'data/raw/accepted_2007_to_2018Q4.csv.gz',
        header = true,
        all_varchar = true,
        ignore_errors = true
    )
""")

print("Row counts:")
tables = ["fedfunds", "unrate", "loans"]
for table in tables:
    count = con.execute("SELECT COUNT(*) FROM raw." + table).fetchone()[0]
    print(table, count)

con.close()
print("Done!")