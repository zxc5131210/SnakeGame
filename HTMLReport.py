# 导入所需的模块
import datetime

# 创建测试结果数据（这里只是一个示例）
test_results = [
    {"test_name": "Test 1", "status": "Pass", "message": ""},
    {"test_name": "Test 2", "status": "Fail", "message": "Assertion error"},
    {"test_name": "Test 3", "status": "Pass", "message": ""},
]

# 生成当前日期和时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建 HTML 报告
report = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Test Report</title>
</head>
<body>
    <h1>Test Report - {current_time}</h1>
    <table border="1">
        <tr>
            <th>Test Name</th>
            <th>Status</th>
            <th>Message</th>
        </tr>
        {"".join(f"<tr><td>{result['test_name']}</td><td>{result['status']}</td><td>{result['message']}</td></tr>" for result in test_results)}
    </table>
</body>
</html>
"""

# 保存报告为 HTML 文件
with open("test_report.html", "w") as report_file:
    report_file.write(report)
