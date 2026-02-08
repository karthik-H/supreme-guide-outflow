# How to Run: Periodic User Data Retrieval System

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Edit the `.env` file to adjust API URL, output directory, or interval if needed.

4. **Run the application**
   ```bash
   python src/main.py
   ```

5. **CSV Output**
   - CSV files will be generated in the directory specified by `CSV_OUTPUT_DIR` in `.env` (default: `csv_snapshots`).
   - Each file is named `user_data_{timestamp}.csv`.

6. **Stopping the Process**
   - Press `Ctrl+C` in the terminal to terminate the process manually.

## Notes
- All user fields, including nested address and company objects, are included in the CSV output.
- The process runs indefinitely until stopped.
- Network errors and file write errors are logged to the console.
