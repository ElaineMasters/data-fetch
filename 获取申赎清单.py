import requests
import csv

output_file = '/home/hejiayan/shannon_py_public/510300ETF/申购清单.csv'

# 准备CSV文件的表头
csv_header = ['Date', 'Content']

# 打开CSV文件准备写入数据
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_header)

    # 迭代请求不同日期的数据
    for year in range(2024, 2025):  # 年份范围，从2024年到2024年
        for month in range(1, 7):  # 月份范围，从1月到12月
            for day in range(1, 32):  # 日范围，从1号到31号（实际上不会超过当月的天数）
                # 构建日期字符串
                date_str = f"{year}{month:02}{day:02}"
                # 构建完整的URL
                url = f"https://www.huatai-pb.com/etf-web/etf/download?filePath=/510300{date_str}.TXT"

                # 发起请求
                response = requests.get(url)
                if response.status_code == 200:
                    # 获取文本内容
                    text_content = response.text
                    # 将日期和内容写入CSV文件
                    writer.writerow([date_str, text_content])
                    print(f"Successfully fetched data for {date_str}")
                else:
                    print(f"Failed to fetch data for {date_str}")

print(f"CSV output saved to {output_file}")
