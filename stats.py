import csv
from pathlib import Path

with Path("data.csv").open(encoding="utf-8") as f:
    values = [float(row["value"]) for row in csv.DictReader(f)]

print("数据条数:", len(values))
print("平均值:", round(sum(values) / len(values), 3))
print("最大值:", max(values))
print("最小值:", min(values))
