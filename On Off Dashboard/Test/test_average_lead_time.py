# tests/alomosafer_id_date_count.py

from config import Config
from utils import DataUtils

class AverageLeadTimeTest:
    def run(self):
        df = DataUtils.load_excel(Config.FILE_PATH, Config.SHEET_NAME)
        department_df = DataUtils.filter_department(df, Config.DEPARTMENTS)
        account_name_df = DataUtils.filter_account_name(department_df, Config.ACCOUNT_NAMES)
        record_flag_df = DataUtils.filter_record_flag(account_name_df, Config.RECORD_FLAG)
        steps_count_df = DataUtils.filter_steps_count(record_flag_df, Config.STEPS_COUNT)
        booking_date_df = DataUtils.filter_booking_date(steps_count_df, Config.DATE_FROM, Config.DATE_TO)
        combine_df = DataUtils.combine_filters(department_df, account_name_df)
        average_lead_time1 = DataUtils.calculate_average_lead_time(df)
        average_lead_time2 = DataUtils.calculate_average_lead_time(department_df)
        average_lead_time3 = DataUtils.calculate_average_lead_time(account_name_df)
        average_lead_time4 = DataUtils.calculate_average_lead_time(record_flag_df)
        average_lead_time5 = DataUtils.calculate_average_lead_time(steps_count_df)
        average_lead_time6 = DataUtils.calculate_average_lead_time(booking_date_df)
        average_lead_time7 = DataUtils.calculate_average_lead_time(combine_df)
        print(f"All Records: {average_lead_time1}")
        print(f"Departments: {average_lead_time2}")
        print(f"Account Names: {average_lead_time3}")
        print(f"Record Flag: {average_lead_time4}")
        print(f"Steps Count: {average_lead_time5}")
        print(f"Average Lead Time (Days) with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {average_lead_time6}")
        print(f"Combined Data with Departments and Account Names: {average_lead_time7}")
        # print(f"Average Lead Time (Days) with Date Filter from {Config.DATE_FROM} to {Config.DATE_TO}: {average_lead_time4}")
