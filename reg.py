import re

reg = r"h\w+"
result = re.match(reg,'world')
print(f'匹配结果：{result}')