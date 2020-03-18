https://docs.python.org/zh-cn/3/library/pathlib.html

https://openpyxl.readthedocs.io/en/stable/tutorial.html


1. 合并单元格不可信
2. 下面一行可能为备注，可能不是备注
3. 【】 可能是备注
4. 并不是每5列为一组


规则：
1. 四项一起判断
2. 如果有一列出现 拉链/ 等字眼，判断为分类 *
3，如果出现[] 则为尺寸
4. 按照编号 宽度 高度 三项来进行大项判断5
5. 提取关键子  关键字判断  白色 米色 素色 绣花 凤尾 。。。。