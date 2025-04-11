import pandas as pd
from fastapi import FastAPI, HTTPException
import os


file_path = "cleaned_suicide.csv"


if not os.path.exists(file_path):
    raise FileNotFoundError(f"The specified file does not exist, Please check.")


df = pd.read_csv(file_path)

df = df.fillna("NA")


app = FastAPI(
    title="Suicide Death Rates API",
    description="API providing suicide death rates by Year, Age, Demographics.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": (
            "Welcome: Available endpoints: /all, /year/{year}, /age/{age_group}, "
            "/demographic/{group}, /years, /age-groups, /demographics"
        )
    }


@app.get("/all")
def get_all_data():
    return df.to_dict(orient = "records")


@app.get("/year/{year}")
def get_data_by_year(year: int):
    filtered = df[df['year'] == year]
    if filtered.empty:
        raise HTTPException(status_code=404, detail=f"No data found for year {year}")
    return filtered.fillna('NA').to_dict(orient="records")


@app.get("/age/{age_group}")
def get_data_by_age(age_group: str):
    filtered = df[df['age_group'].str.lower() == age_group.lower()]
    if filtered.empty:
        raise HTTPException(status_code=404, detail=f"No data found for age_group {age_group}")
    return filtered.fillna('NA').to_dict(orient="records")


@app.get("/demographic/{demographic_group}")
def get_data_by_demographic_group(demographic_group: str):
    filtered = df[df['demographic_group'].str.lower() == demographic_group.lower()]
    if filtered.empty:
        raise HTTPException(status_code=404, detail=f"No data found for demographic_group {demographic_group}")
    return filtered.fillna('NA').to_dict(orient="records")


@app.get("/years")
def get_unique_years():
    return {"years": sorted(df['year'].unique().tolist())}

@app.get("/age_groups")
def get_unique_years():
    return {"age_groups": sorted(df['age_group'].unique().tolist())}

@app.get("/demographics")
def get_unique_years():
    return {"demographic_groups": sorted(df['demographic_group'].unique().tolist())}