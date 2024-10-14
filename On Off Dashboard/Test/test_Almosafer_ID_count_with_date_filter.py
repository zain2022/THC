# tests/alomosafer_id_date_count.py

from config import Config
from utils import DataUtils

class AlomosaferIDDateCountTest:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        booking_date_df = DataUtils.filter_booking_date(steps_count_df, Config.DATE_FROM, Config.DATE_TO)
        alomosafer_count = DataUtils.count_unique_alomosafer_ids(booking_date_df)
        total_cost, formatted_total = DataUtils.calculate_total_cost(booking_date_df)
        print(f"Total Distinct Alomosafer IDs with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {alomosafer_count}")
        print(f"Total Cost with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {total_cost} ({formatted_total})")
