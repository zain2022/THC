# main.py

from Test.test_Almosafer_ID_count_with_date_filter import AlomosaferIDDateCountTest
from Test.test_Almosafer_ID_count import AlomosaferIDCountTest
from Test.test_total_cost import TotalCostTest
from Test.test_average_lead_time import AverageLeadTimeTest

def main():
    # print("Running Alomosafer ID Count Test...")
    # AlomosaferIDCountTest().run()
    #
    # print("\nRunning Total Cost Test...")
    # TotalCostTest().run()

    print("\nRunning Alomosafer ID Count with Date Filter Test...")
    AlomosaferIDDateCountTest().run()

    print("\nRunning Average Lead Time Test...")
    AverageLeadTimeTest().run()

if __name__ == "__main__":
    main()