import pandas as pd
def clean_data():
    # Read Data
    df = pd.read_csv("Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States (1).csv")

    "Original data:",df.head()

    # Removing irrelevant data from the columns.
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "").str.replace("%", "Percent").str.replace("/", "").str.replace("-", "").str.replace("", "")

    print("Cleaned Columns:", df.columns.tolist())

    # Identifyng the null valuea nd dropping them.
    df = df.dropna(subset=["year", "age", "estimate", "stub_name"])


    # Converting the datatype if there are any incorrect type.
    df["year"] = df["year"].astype(int)
    df["year_num"] = pd.to_numeric(df["year_num"], errors = "coerce")
    df["age_num"] = pd.to_numeric(df["age_num"], errors = "coerce")
    df["estimate"] = pd.to_numeric(df["estimate"], errors = "coerce")

    # Renaming the data for better interpretability.
    df = df.rename(columns={
        "stub_name": "demographic_group",
        "year": "year",
        "age": "age_group",
        "estimate": "death_rate_estimate"
    })


    # Saving the cleaned data.
    df.to_csv("cleaned_suicide.csv", index = False)
    print("ETL Operation is succesfully completed and saved in the root directory.")


if __name__ == "__main__":
    clean_data()