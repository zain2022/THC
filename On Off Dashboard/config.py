# config.py

class Config:
    FILE_PATH = 'C:/Users/zain.abideen_venture/PycharmProjects/pythonProject/.venv/On Off Dashboard/Data Source/Travel Model.xlsx'
    SHEET_NAME = 'Sheet1'

    DEPARTMENTS = [
        'Operation P121_AW139', 'Operation (P121)', 'Operation P121_ACH160', 'Operation P121_H145',
        'Operation (P135)', 'Operation (P133)', 'Operation P135_H125',
        'Maintenance (P121)', 'Maintenance (P145)', 'Maintenance P145_AW139', 'Maintenance (P135)',
        'Maintenance P145_H145', 'Maintenance P145_ ACH160', 'Maintenance P145_H125', 'Maintenance (P133)'
    ]
    ACCOUNT_NAMES = [
        'Operations Control Center', 'Maintenance', 'SRA', 'Maintenance_Off-On Rotation',
        'Maintenance_SRA_Off-On Rotation', 'Flight Ops Management_Off-On Rotation'
    ]
    RECORD_FLAG = 'latest'
    STEPS_COUNT = 1
    DATE_FROM = '2024-01-01'
    DATE_TO = '2024-06-30'