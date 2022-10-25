import re

# 读取文件
# data = "C:\\Users\\17993\Desktop\\filterIP\\ip.txt"
data = "ip.txt"
with open(data, "r+", encoding="utf-8") as f:
    ip_raw = f.readlines()

    # print(ip_raw)
# 过滤IP
    ip_list = []
    for i in ip_raw:
        result = re.search("((?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]))", i)
        if result:
            ip_list.append(result.group(1))
            # ip_list.append(result.group(1))
            # print(result.group(1))
    # print(ip_list)

# 清空原文件
with open(data, "w", encoding="utf-8") as clean_file:
    clean_file.write("")
# 把读取的IP写入原文件
with open(data, "a+", encoding="utf-8") as into_file:
    for i in ip_list:
        into_file.write(f"{i}\n")