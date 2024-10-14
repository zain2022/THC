# tests/alomosafer_id_count.py

from config import Config
from utils import DataUtils

class AlomosaferIDCountTest:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        alomosafer_count = DataUtils.count_unique_alomosafer_ids(steps_count_df)
        print(f"Total Distinct Alomosafer IDs: {alomosafer_count}")