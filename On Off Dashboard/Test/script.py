import pandas as pd
import json


def load_excel(file_path, sheet_name):
    """Loads an Excel file and returns a DataFrame for a specified sheet."""
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Remove leading/trailing spaces and ensure consistent case
    df['Department'] = df['Department'].str.strip().str.lower()
    df['account_name'] = df['account_name'].str.strip().str.lower()
    df['record_flag'] = df['record_flag'].str.strip().str.lower()

    print("All Records: ", len(df))
    return df


def filter_department(df, departments):
    """Filters the DataFrame for specified department values."""
    departments = [d.lower() for d in departments]
    filtered_df = df[df['Department'].isin(departments)]
    print("Total Records after Department Filters: ", len(filtered_df))
    return filtered_df


def filter_account_name(df, account_names):
    """Filters the DataFrame for specified account name values."""
    account_names = [d.lower() for d in account_names]
    filtered_df = df[df['account_name'].isin(account_names)]
    print("Total Records after Account Names Filters: ", len(filtered_df))
    return filtered_df


def filter_record_flag(df, record_flag_value="latest"):
    """Filters the DataFrame for the 'record_flag' column with a specified value."""
    filtered_df = df[df['record_flag'] == record_flag_value.lower()]
    print("Total Records after Record Flag Filter: ", len(filtered_df))
    return filtered_df


def filter_steps_count(df, steps_count_value=1):
    """Filters the DataFrame for the 'steps_count' column with a specified value."""
    filtered_df = df[df['steps_count'] == steps_count_value]
    print("Total Records after Steps Count Filter: ", len(filtered_df))
    return filtered_df


def combine_filters(department_filtered_df, account_filtered_df):
    """Combines department and account name filters."""
    combined_df = department_filtered_df.merge(account_filtered_df, how='inner')
    print("Combined Records after Department, Account Name, Record Flag and Steps Count Filters: ", len(combined_df))
    return combined_df


def count_unique_alomosafer_ids(filtered_data):
    """Counts distinct Alomosafer IDs in the filtered data."""
    unique_count = filtered_data['almosafer_order_ID'].nunique()
    print(f"Total Distinct Alomosafer IDs: {unique_count}")
    return unique_count


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
    print("NAT Records: ", df['booking_date'].isna().sum())  # Shows count of NaT values

    # Filter for 'from' and 'to' dates
    combined_date_filtered = df[(df['booking_date'] >= from_date) & (df['booking_date'] <= to_date)]

    print("Total Records after Date Filters: ", len(combined_date_filtered))
    return combined_date_filtered

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

    # print(f"df['travel_date']: {df['travel_date']}")
    # print(f"df['booking_date']: {df['booking_date']}")
    # print(f"lead_time: {lead_time}")
    # print(f"valid_lead_times: {valid_lead_times}")
    print(f"Average Lead Time in Days: {average_lead_time}")
    return average_lead_time

def main():
    # Define file path and sheet name
    file_path = 'C:/Users/zain.abideen_venture/PycharmProjects/pythonProject/.venv/On Off Dashboard/Data Source/Travel Model.xlsx'
    sheet_name = 'Sheet1'

    # Define filters
    departments = [
        'Operation P121_AW139', 'Operation (P121)', 'Operation P121_ACH160', 'Operation P121_H145',
        'Operation (P135)', 'Operation (P133)', 'Operation P135_H125',
        'Maintenance (P121)', 'Maintenance (P145)', 'Maintenance P145_AW139', 'Maintenance (P135)',
        'Maintenance P145_H145', 'Maintenance P145_ ACH160', 'Maintenance P145_H125', 'Maintenance (P133)'
    ]
    account_names = [
        'Operations Control Center', 'Maintenance', 'SRA', 'Maintenance_Off-On Rotation',
        'Maintenance_SRA_Off-On Rotation', 'Flight Ops Management_Off-On Rotation'
    ]

    record_flag = "latest"

    steps_count = 1

    # Date filter range
    from_date = '2024-01-01'
    to_date = '2024-06-30'

    # Load data
    df = load_excel(file_path, sheet_name)

    # Apply filters
    department_filtered_df = filter_department(df, departments)
    account_filtered_df = filter_account_name(department_filtered_df, account_names)
    record_flag_filtered_df = filter_record_flag(account_filtered_df, "latest")
    steps_count_filtered_df = filter_steps_count(record_flag_filtered_df, 1)

    # Combine filters and print combined record count
    combined_data = combine_filters(department_filtered_df, account_filtered_df)

    # Count distinct Alomosafer IDs without date filter
    alomosafer_id_count = count_unique_alomosafer_ids(steps_count_filtered_df)
    print(f"Total distinct Alomosafer IDs for On/Off dashboard: {alomosafer_id_count}")

    # Apply date filters and count distinct Alomosafer IDs with date filter
    date_filtered_df = filter_booking_date(steps_count_filtered_df, from_date, to_date)
    alomosafer_id_count_with_date = count_unique_alomosafer_ids(date_filtered_df)
    print(f"Total distinct Alomosafer IDs with Date Filters from {from_date} to {to_date} for On/Off dashboard: {alomosafer_id_count_with_date}")

    # Total Cost without Date Filter
    total_cost, formatted_total = calculate_total_cost(steps_count_filtered_df)
    print(f"Total Cost On/Off dashboard: {total_cost}")
    print(f"Total Cost On/Off dashboard: {formatted_total}")

    # Total Cost with Date Filter
    total_cost, formatted_total = calculate_total_cost(date_filtered_df)
    print(f"Total Cost with Date Filter On/Off dashboard: {total_cost}")
    print(f"Total Cost with Date Filter On/Off dashboard: {formatted_total}")

    # Average Lead Time (Days)
    average_lead_time = calculate_average_lead_time(account_filtered_df)
    print(f"Average Lead Time (Days) On/Off dashboard: {average_lead_time}")

# Execute the main function
if __name__ == "__main__":
    main()