import pandas as pd
import argparse
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Sets up the argument parser for the script.
    """
    parser = argparse.ArgumentParser(description="Analyze network traffic patterns.")
    parser.add_argument("input_file", help="Path to the CSV file containing network traffic data.")
    parser.add_argument("--output_file", help="Path to save the analysis report (optional).", default=None)
    return parser

def analyze_traffic(input_file, output_file=None):
    """
    Analyzes network traffic patterns from a CSV file.

    Args:
        input_file (str): Path to the CSV file containing network traffic data.
        output_file (str): Optional path to save the analysis report.
    """
    try:
        # Load the CSV file into a DataFrame
        logging.info(f"Loading data from {input_file}")
        data = pd.read_csv(input_file)

        # Perform basic analysis (example: count unique IPs and calculate total data transferred)
        logging.info("Performing analysis...")
        unique_ips = data['source_ip'].nunique()
        total_data_transferred = data['data_transferred'].sum()

        # Prepare the analysis report
        report = {
            "Unique IPs": unique_ips,
            "Total Data Transferred": total_data_transferred
        }

        # Print the analysis report
        logging.info("Analysis completed. Results:")
        for key, value in report.items():
            logging.info(f"{key}: {value}")

        # Save the report to a file if output_file is specified
        if output_file:
            logging.info(f"Saving report to {output_file}")
            pd.DataFrame([report]).to_csv(output_file, index=False)

    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        logging.error("The input file is empty.")
        sys.exit(1)
    except KeyError as e:
        logging.error(f"Missing expected column in the data: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the script.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    analyze_traffic(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

# Usage Examples:
# python main.py traffic_data.csv
# python main.py traffic_data.csv --output_file analysis_report.csv