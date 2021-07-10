import os
import re

path = "C:/Users/LEGION/Documents/GitHub/Python3WebSpider/Cov_2021/NHC_Data/"

fileList = os.listdir(path)

n = 0

for i in fileList:

    oldname = fileList[n]

    result = re.match('[\u4e00-\u9fa5]*(\d+)[\u4e00-\u9fa5](\d+)', oldname)

    newname = result.group(1) + '.' + result.group(2)+'.txt'

    oldname = path + os.sep + oldname
    newname = path + os.sep + newname

    os.rename(oldname, newname)
    n += 1

    print(oldname,result.group(1),result.group(2))
