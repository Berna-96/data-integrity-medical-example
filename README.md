# Data Integrity – Medical Dataset Example

This project demonstrates a realistic data engineering scenario involving incomplete medical records.

## Scenario

In clinical datasets, some variables (e.g. patient weight) may be missing while dependent variables
(e.g. dosage) are present. Naive imputations can introduce dangerous biases or clinically invalid data.

## Key Concepts Demonstrated

- Safe numeric conversion
- Domain validation rules
- Missing data handling without unsafe imputations
- Metadata / integrity flags
- Record quality classification

## Why This Matters

In safety-critical domains such as healthcare, preserving data integrity is more important than
forcing dataset completeness. Missing values are often preferable to incorrect synthetic data.

## Structure

- `data/` → Example dataset
- `rules/` → Domain validation logic
- `pipeline/` → Processing pipeline

## Educational Purpose

This repository is intended as a learning example for data validation and integrity patterns.
