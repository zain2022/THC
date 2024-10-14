# tests/total_cost.py

from config import Config
from utils import DataUtils

class TotalCostTest:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        total_cost, formatted_total = DataUtils.calculate_total_cost(steps_count_df)
        print(f"Total Cost: {total_cost} ({formatted_total})")


# import pandas as pd
# import json
#
#
# def load_excel(file_path, sheet_name):
#     """Loads an Excel file and returns a DataFrame for a specified sheet."""
#     df = pd.read_excel(file_path, sheet_name=sheet_name)
#
#     # Remove leading/trailing spaces and ensure consistent case
#     df['Department'] = df['Department'].str.strip().str.lower()
#     df['account_name'] = df['account_name'].str.strip().str.lower()
#     df['record_flag'] = df['record_flag'].str.strip().str.lower()
#
#     print("All Records: ", len(df))
#     return df
#
#
# def filter_department(df, departments):
#     """Filters the DataFrame for specified department values."""
#     departments = [d.lower() for d in departments]
#     filtered_df = df[df['Department'].isin(departments)]
#     print("Total Records after Department Filters: ", len(filtered_df))
#     return filtered_df
#
#
# def filter_account_name(df, account_names):
#     """Filters the DataFrame for specified account name values."""
#     account_names = [d.lower() for d in account_names]
#     filtered_df = df[df['account_name'].isin(account_names)]
#     print("Total Records after Account Names Filters: ", len(filtered_df))
#     return filtered_df
#
#
# def filter_record_flag(df, record_flag_value="latest"):
#     """Filters the DataFrame for the 'record_flag' column with a specified value."""
#     filtered_df = df[df['record_flag'] == record_flag_value.lower()]
#     print("Total Records after Record Flag Filter: ", len(filtered_df))
#     return filtered_df
#
#
# def filter_steps_count(df, steps_count_value=1):
#     """Filters the DataFrame for the 'steps_count' column with a specified value."""
#     filtered_df = df[df['steps_count'] == steps_count_value]
#     print("Total Records after Steps Count Filter: ", len(filtered_df))
#     return filtered_df
#
#
# def combine_filters(department_filtered_df, account_filtered_df):
#     """Combines department and account name filters."""
#     combined_df = department_filtered_df.merge(account_filtered_df, how='inner')
#     print("Combined Records after Department, Account Name, Record Flag and Steps Count Filters: ", len(combined_df))
#     return combined_df
#
#
# def calculate_total_cost(df):
#     """
#     Rounds off each value in the 'total' column, sums all values, and rounds the final sum.
#     Args:
#     df (DataFrame): DataFrame containing the 'total' column.
#     Returns:
#     float: The rounded final sum of the 'total' column values.
#     """
#     # Round each value in the 'total' column
#     df.loc[:, 'total'] = df['total'].round()
#
#     # Sum the rounded values and then round the final sum
#     total_cost = round(df['total'].sum())
#
#     # print(f"Rounded Total Cost: {total_cost}")
#
#     # total_cost = round(df['total'].round().sum())
#
#     # Determine the suffix based on the magnitude of total_cost
#     if total_cost >= 1_000_000_000:
#         formatted_total = f"{round(total_cost / 1_000_000_000)}B"
#     elif total_cost >= 1_000_000:
#         formatted_total = f"{round(total_cost / 1_000_000)}M"
#     elif total_cost >= 1_000:
#         formatted_total = f"{round(total_cost / 1_000)}K"
#     else:
#         formatted_total = str(total_cost)  # No suffix for values less than 1,000
#
#     return total_cost, formatted_total
#
# def main():
#     # Define file path and sheet name
#     file_path = 'C:/Users/zain.abideen_venture/PycharmProjects/pythonProject/.venv/On Off Dashboard/Data Source/Travel Model.xlsx'
#     sheet_name = 'Sheet1'
#
#     # Define filters
#     departments = [
#         'Operation P121_AW139', 'Operation (P121)', 'Operation P121_ACH160', 'Operation P121_H145',
#         'Operation (P135)', 'Operation (P133)', 'Operation P135_H125',
#         'Maintenance (P121)', 'Maintenance (P145)', 'Maintenance P145_AW139', 'Maintenance (P135)',
#         'Maintenance P145_H145', 'Maintenance P145_ ACH160', 'Maintenance P145_H125', 'Maintenance (P133)'
#     ]
#     account_names = [
#         'Operations Control Center', 'Maintenance', 'SRA', 'Maintenance_Off-On Rotation',
#         'Maintenance_SRA_Off-On Rotation', 'Flight Ops Management_Off-On Rotation'
#     ]
#
#
#     # Load data
#     df = load_excel(file_path, sheet_name)
#
#     # Apply filters
#     department_filtered_df = filter_department(df, departments)
#     account_filtered_df = filter_account_name(department_filtered_df, account_names)
#     record_flag_filtered_df = filter_record_flag(account_filtered_df, "latest")
#     steps_count_filtered_df = filter_steps_count(record_flag_filtered_df, 1)
#
#     # Combine filters and print combined record count
#     combined_data = combine_filters(department_filtered_df, account_filtered_df)
#
#     # Total Cost
#     total_cost, formatted_total = calculate_total_cost(steps_count_filtered_df)
#     print(f"Total Cost On/Off dashboard: {total_cost}")
#     print(f"Total Cost On/Off dashboard: {formatted_total}")
#
# # Execute the main function
# if __name__ == "__main__":
#     main()