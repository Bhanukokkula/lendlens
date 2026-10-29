import dlt
import requests


def get_series(series_id):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": dlt.secrets["fred_api_key"],
        "file_type": "json",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    rows = []
    for obs in response.json()["observations"]:
        row = {
            "observation_date": obs["date"],
            series_id.lower(): obs["value"],
        }
        rows.append(row)
    return rows


pipeline = dlt.pipeline(
    pipeline_name="fred",
    destination=dlt.destinations.duckdb("lendlens.duckdb"),
    dataset_name="raw_fred",
)

series_list = ["FEDFUNDS", "UNRATE"]
for series_id in series_list:
    print("Loading " + series_id + "...")
    data = get_series(series_id)
    info = pipeline.run(data, table_name=series_id.lower(), write_disposition="replace")
    print(info)