# Python Data Processing Pipeline

## Project Overview
This project reads raw data from a CSV file, cleans and transforms the data, and saves the processed results into an output CSV file.

## Features
- Reads data from CSV files.
- Handles missing values.
- Converts data types where required.
- Cleans and transforms raw data.
- Generates structured output.
- Maintains logs of pipeline execution.
- Uses a JSON configuration file.

## Technologies Used
- Python
- Pandas
- CSV
- JSON
- Logging

## Project Structure
```text
PythonDataPipeline/
├── data/
│   ├── raw_data.csv
│   └── output.csv
├── src/
│   └── pipeline.py
├── logs/
│   └── pipeline.log
├── config.json
├── requirements.txt
└── README.md
```

## How to Run
1. Install the required packages:
   `pip install -r requirements.txt`
2. Run the pipeline:
   `py src/pipeline.py`
3. Check `data/output.csv` for the processed data.
4. Check `logs/pipeline.log` for execution logs.

## Expected Output
The pipeline processes the input CSV file, handles missing values according to the configured rules, and generates a cleaned output file.

## Author
Rithika