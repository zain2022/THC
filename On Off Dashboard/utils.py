# utils.py

import pandas as pd

class DataUtils:
    @staticmethod
    def load_excel(file_path, sheet_name):
        """Loads an Excel file and returns a DataFrame for a specified sheet."""
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Remove leading/trailing spaces and ensure consistent case
        df['Department'] = df['Department'].str.strip().str.lower()
        df['account_name'] = df['account_name'].str.strip().str.lower()
        df['record_flag'] = df['record_flag'].str.strip().str.lower()

        # print("All Records: ", len(df))
        return df

    @staticmethod
    def filter_department(df, departments):
        """Filters the DataFrame for specified department values."""
        departments = [d.lower() for d in departments]
        filtered_df = df[df['Department'].isin(departments)]
        # print("Total Records after Department Filters: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def filter_account_name(df, account_names):
        """Filters the DataFrame for specified account name values."""
        account_names = [d.lower() for d in account_names]
        filtered_df = df[df['account_name'].isin(account_names)]
        # print("Total Records after Account Names Filters: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def filter_record_flag(df, record_flag):
        """Filters the DataFrame for the 'record_flag' column with a specified value."""
        filtered_df = df[df['record_flag'] == record_flag.lower()]
        # print("Total Records after Record Flag Filter: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def filter_steps_count(df, steps_count):
        """Filters the DataFrame for the 'steps_count' column with a specified value."""
        filtered_df = df[df['steps_count'] == steps_count]
        # print("Total Records after Steps Count Filter: ", len(filtered_df))
        return filtered_df

    @staticmethod
    def combine_filters(department_filtered_df, account_filtered_df):
        """Combines department and account name filters."""
        combined_df = department_filtered_df.merge(account_filtered_df, how='inner')
        # print("Combined Records after Department, Account Name, Record Flag and Steps Count Filters: ",len(combined_df))
        return combined_df

    @staticmethod
    def filter_booking_date(df, from_date, to_date):
        """Applies both 'from' and 'to' date filters on 'booking_date' column.
            This line converts the booking_date column to datetime format. The errors='coerce' argument ensures that any invalid or non-parsable date entries will be converted to
            NaT (Not a Time), avoiding potential errors. The use of .loc[:, 'booking_date'] ensures that we modify the DataFrame directly rather than a copy, which helps avoid the
            SettingWithCopyWarning.
            Ensure the booking_date column is in datetime format using .loc
            """
        df.loc[:, 'booking_date'] = pd.to_datetime(df['booking_date'].dt.date, errors='coerce')
        # df.loc[:, 'booking_date'] = pd.to_datetime(df['booking_date'], errors='coerce')
        # print("Records with Date Filters: ", df.to_dict(orient="records"))  # Updated to be JSON-serializable
        # print("Records with Date Filters: ", df['booking_date'].to_dict())
        # print(json.dumps(df, indent=4))
        # print("NAT Records: ", df['booking_date'].isna().sum())  # Shows count of NaT values

        # Filter for 'from' and 'to' dates
        combined_date_filtered = df[(df['booking_date'] >= from_date) & (df['booking_date'] <= to_date)]

        # print("Total Records after Date Filters: ", len(combined_date_filtered))
        return combined_date_filtered

    @staticmethod
    def count_unique_alomosafer_ids(df):
        """Counts distinct Alomosafer IDs in the filtered data."""
        unique_count = df['almosafer_order_ID'].nunique()
        # print(f"Total Distinct Alomosafer IDs: {unique_count}")
        return unique_count

    @staticmethod
    def calculate_total_cost(df):
        """
            Rounds off each value in the 'total' column, sums all values, and rounds the final sum.
            Args:
            df (DataFrame): DataFrame containing the 'total' column.
            Returns:
            float: The rounded final sum of the 'total' column values.
            """
        # Round each value in the 'total' column
        df.loc[:, 'total'] = df['total'].round()

        # Sum the rounded values and then round the final sum
        total_cost = round(df['total'].sum())

        # print(f"Rounded Total Cost: {total_cost}")

        # total_cost = round(df['total'].round().sum())

        # Determine the suffix based on the magnitude of total_cost
        if total_cost >= 1_000_000_000:
            formatted_total = f"{round(total_cost / 1_000_000_000)}B"
        elif total_cost >= 1_000_000:
            formatted_total = f"{round(total_cost / 1_000_000)}M"
        elif total_cost >= 1_000:
            formatted_total = f"{round(total_cost / 1_000)}K"
        else:
            formatted_total = str(total_cost)  # No suffix for values less than 1,000

        return total_cost, formatted_total

    def calculate_average_lead_time(df):
        """
        Calculates the average lead time in days based on 'travel_date' and 'booking_date' columns.
        Lead time is calculated as (travel_date - booking_date) with both date and time components.

        Args:
        df (DataFrame): DataFrame containing 'travel_date' and 'booking_date' columns.

        Returns:
        float: The average lead time in days, rounded to the nearest whole number.
        """
        # Create a copy of the DataFrame to avoid SettingWithCopyWarning
        df = df.copy()

        # Convert 'travel_date' and 'booking_date' to datetime format without removing time component
        df['travel_date'] = pd.to_datetime(df['travel_date'].dt.date, errors='coerce')
        df['booking_date'] = pd.to_datetime(df['booking_date'].dt.date, errors='coerce')

        # Calculate lead time in days
        lead_time = df['lead_time_days'] = (df['travel_date'] - df['booking_date']).dt.total_seconds() / (24 * 60 * 60)

        # Filter out any rows with NaN values in lead_time_days
        valid_lead_times = df['lead_time_days'].dropna()

        # Calculate the average lead time and round it
        average_lead_time = round(valid_lead_times.mean())
        average_lead_time_without_round = valid_lead_times.mean()

        # print(f"df['travel_date']: {df['travel_date']}")
        # print(f"df['booking_date']: {df['booking_date']}")
        # print(f"lead_time: {lead_time}")
        # print(f"valid_lead_times: {valid_lead_times}")
        print(f"Average Lead Time in Days: {average_lead_time}")
        print(f"Average Lead Time in Days without Round: {average_lead_time_without_round}")
        return average_lead_time
