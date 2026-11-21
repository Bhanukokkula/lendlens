import duckdb

print("Connecting to DuckDB...")
con = duckdb.connect("lendlens.duckdb")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

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

count = con.execute("SELECT COUNT(*) FROM raw.loans").fetchone()[0]
print("loans", count)

con.close()
print("Done!")