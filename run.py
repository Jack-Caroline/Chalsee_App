import pytest

# allure_report_path = "--alluredir=test_result/reports"

# 1、生成 allure 测试报告数据
pytest.main(["--alluredir=test_result/reports"])
