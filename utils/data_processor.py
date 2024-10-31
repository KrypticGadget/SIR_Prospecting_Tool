# utils/data_processor.py
import pandas as pd
from datetime import datetime
from utils.address_standardizer import AddressStandardizer

class DataProcessor:
    def __init__(self, valid_property_classes):
        self.valid_property_classes = valid_property_classes
        self.address_standardizer = AddressStandardizer()

    def load_data(self, file_path):
        """Load the raw data from an Excel file."""
        return pd.read_excel(file_path)

    def filter_data(self, df):
        """Filter data based on specific property classes."""
        filtered_df = df[df["Property class"].isin(self.valid_property_classes)]
        return filtered_df.drop(columns=["Block & Lot"], errors="ignore")

    def standardize_addresses(self, df):
        """Concatenate address fields and standardize address."""
        df["Address"] = df["Address"].apply(self.address_standardizer.standardize)
        df["Full Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + " " + df["Zipcode"].astype(str)
        return df

    def remove_duplicates(self, df):
        """Remove duplicate entries based on Full Address while keeping the first occurrence."""
        # Sort by date to keep the most recent entry (if date column exists)
        if 'Sale date' in df.columns:
            df['Sale date'] = pd.to_datetime(df['Sale date'], errors='coerce')
            df = df.sort_values('Sale date', ascending=False)

        # Drop duplicates based on Full Address
        deduped_df = df.drop_duplicates(subset=['Full Address'], keep='first')
        
        # Reset index after deduplication
        deduped_df = deduped_df.reset_index(drop=True)
        
        return deduped_df

    def process_file(self, file_path):
        """Process and validate the data."""
        try:
            # Load and process the data
            df = self.load_data(file_path)
            filtered_df = self.filter_data(df)
            standardized_df = self.standardize_addresses(filtered_df)
            deduped_df = self.remove_duplicates(standardized_df)
            
            # Add processing timestamp in readable format
            deduped_df["Processed Date"] = datetime.now().strftime("%B %d, %Y at %I:%M %p")
            
            return deduped_df
        except Exception as e:
            print(f"Error processing file: {str(e)}")
            return None