import duckdb

con = duckdb.connect("lendlens.duckdb", read_only=True)

tables = ["mart_vintage_defaults", "fct_monthly_portfolio"]
for table in tables:
    print("Exporting " + table + "...")
    con.execute(
        "COPY main_marts." + table +
        " TO 'exports/" + table + ".csv' (HEADER)"
    )

con.close()
print("Done!")

