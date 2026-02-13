import pandas as pd
from rules.validation_rules import validate_age, validate_weight
from logger import write_log

# Soglia qualità minima accettabile
MIN_COMPLETENESS_RATIO = 80.0   # percentuale

def run_pipeline():

    df = pd.read_csv("../data/patients.csv")

    write_log("INFO", "Dataset loaded")

    # Conversione tipi
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
    df["dosage_mg"] = pd.to_numeric(df["dosage_mg"], errors="coerce")

    # Validazioni
    df = validate_age(df)
    df = validate_weight(df)

    # Flags integrità
    df["weight_missing_flag"] = df["weight"].isna()
    df["record_quality"] = df["weight_missing_flag"].map(
        {True: "incomplete_but_usable", False: "complete"}
    )

    # Metriche qualità
    total_records = len(df)
    incomplete_records = df["weight_missing_flag"].sum()
    completeness_ratio = (1 - incomplete_records / total_records) * 100

    write_log("INFO", f"Total records: {total_records}")
    write_log("INFO", f"Incomplete records: {incomplete_records}")
    write_log("INFO", f"Completeness ratio: {completeness_ratio:.2f}%")

    # Alert logic 
    if completeness_ratio < MIN_COMPLETENESS_RATIO:
        write_log(
            "WARNING",
            "Data quality degraded – completeness below acceptable threshold"
        )

    print(df)

if __name__ == "__main__":
    run_pipeline()

