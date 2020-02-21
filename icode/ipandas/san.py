# import pandas as pd
# import numpy as np
#
# data = {
#     'apples': [3, 2, 0, 1],
#     'oranges': [0, 3, 7, 2]
# }
# purchases = pd.DataFrame(data,index=['June', 'Robert', 'Lily', 'David'])
#
# print(purchases)
# print(purchases.loc['June'])
from pathlib import Path, PurePath

# base_path = PurePath("F:")
base_path = Path("G:\SynologyDrive\文档\裁床\历史文档\\2019年定做登记")
print(base_path.absolute())
print(base_path.cwd())
for time_dir in base_path.iterdir():
    if time_dir.is_dir():
        # for file in time_dir.iterdir() :
        for file in time_dir.glob('*.xlsx'):
            print(file)

# print([x for x in base_path.iterdir()])
#