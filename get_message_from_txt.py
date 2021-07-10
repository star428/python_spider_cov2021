import os
import re
import csv

def return_data(mouth, day):
    addr = 'C:\\Users\\LEGION\\Documents\\GitHub\\Python3WebSpider\\Cov_2021\\NHC_Data\\' + str(mouth) + '.' + \
                str(day) + '.txt'
    with open(addr, "r", encoding='utf-8') as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
        return data

def output_dict(data):
    dict = {
    '时间':0,
    '新增确诊人数':0,
    '新增死亡人数':0,
    '新增疑似人数':0,
    '新增治愈人数':0,

    '现有确诊人数':0,
    '累计治愈人数':0, # 累计治愈人数
    '累计死亡人数':0, # 累计死亡人数
    '累计确诊人数':0, # 现有确诊人数
    '现有疑似人数':0, # 现有疑似人数
    '累计密切接触者':0 # 累计密切接触者
    }

    time = re.search('.*?(\d*)\u6708(\d*)\u65e5', data)

    dict['时间'] = str(time.group(1)) + '.' + str(time.group(2))

    # dayConfirmedCount = re.search('\u65b0\u589e\u786e\u8bca\u75c5\u4f8b(\d*)\u4f8b', data) # 新增确诊病例
    newConfirmed = re.search('\u65b0\u589e\u786e\u8bca.*?\u4f8b(\d*)\u4f8b', data, re.S)
    newSuspected = re.search('\u65b0\u589e\u7591\u4f3c.*?\u4f8b(\d*)\u4f8b', data, re.S)
    newDead = re.search('\u65b0\u589e\u6b7b\u4ea1.*?\u4f8b(\d*)\u4f8b', data, re.S)
    newCured = re.search('\u65b0\u589e\u6cbb\u6108.*?\u4f8b(\d*)\u4f8b', data, re.S)

    try:
        dict['新增确诊人数'] = newConfirmed.group(1)
    except AttributeError:
        dict['新增确诊人数'] = 0

    try:
        dict['新增疑似人数'] = newSuspected.group(1)
    except AttributeError:
        dict['新增疑似人数'] = 0

    try:
        dict['新增死亡人数'] = newDead.group(1)
    except AttributeError:
        dict['新增死亡人数'] = 0

    try:
        dict['新增治愈人数'] = newCured.group(1)
    except AttributeError:
        dict['新增治愈人数'] = 0

    isnewConfirmed = re.search('\u65e0\u65b0\u589e\u786e\u8bca\u75c5\u4f8b.*?\u622a\u81f3', data, re.S)
    isnewSuspected = re.search('\u65e0\u65b0\u589e\u7591\u4f3c\u75c5\u4f8b.*?\u622a\u81f3', data, re.S)
    isnewDead = re.search('\u65e0\u65b0\u589e\u6b7b\u4ea1\u75c5\u4f8b.*?\u622a\u81f3', data, re.S)
    isnewCured = re.search('\u65e0\u65b0\u589e\u6cbb\u6108\u75c5\u4f8b.*?\u622a\u81f3', data, re.S)

    if not (isnewConfirmed is None):
        dict['新增确诊人数'] = 0

    if not (isnewSuspected is None):
        dict['新增疑似人数'] = 0

    if not (isnewDead is None):
        dict['新增死亡人数'] = 0

    if not (isnewCured is None):
        dict['新增治愈人数'] = 0

    nowConfirmed = re.search('\u622a\u81f3.*?\u73b0\u6709.*?\u786e\u8bca.*?\u4f8b(\d*)\u4f8b', data, re.S)
    confirmed = re.search('\u622a\u81f3.*?\u7d2f\u8ba1.*?\u786e\u8bca.*?\u4f8b(\d*)\u4f8b', data, re.S)
    suspected = re.search('\u622a\u81f3.*?\u7591\u4f3c.*?\u4f8b(\d*)\u4f8b', data, re.S)
    dead = re.search('\u622a\u81f3.*?\u7d2f\u8ba1.*?\u6b7b\u4ea1.*?\u4f8b(\d*)\u4f8b', data, re.S)
    cure = re.search('\u622a\u81f3.*?\u7d2f\u8ba1.*?\u6cbb\u6108.*?\u4f8b(\d*)\u4f8b', data, re.S)
    contentPeople = re.search('\u622a\u81f3.*?\u5bc6\u5207\u63a5\u89e6.*?\u8005(\d*)\u4eba', data, re.S)


    try:
        dict['现有确诊人数'] = nowConfirmed.group(1)
    except AttributeError:
        dict['现有确诊人数'] = 0

    try:
        dict['累计确诊人数'] = confirmed.group(1)
    except AttributeError:
        dict['累计确诊人数'] = 0

    try:
        dict['现有疑似人数'] = suspected.group(1)
    except AttributeError:
        dict['现有疑似人数'] = 0

    issuspected = re.search('\u622a\u81f3.*?\u65e0\u73b0\u6709\u7591\u4f3c\u75c5\u4f8b', data, re.S)

    if not (issuspected is None):
        dict['现有疑似人数'] = 0

    try:
        dict['累计死亡人数'] = dead.group(1)
    except AttributeError:
        dict['累计死亡人数'] = 0

    try:
        dict['累计治愈人数'] = cure.group(1)
    except AttributeError:
        dict['累计治愈人数'] = 0

    try:
        dict['累计密切接触者'] = contentPeople.group(1)
    except AttributeError:
        dict['累计密切接触者'] = 0


    return dict

if __name__ == '__main__':

    for mouth in range(1, 13):
        for day in range(1, 32):
            try:
                data = return_data(mouth, day)
                dict = output_dict(data)
                print(dict)

            except:
                continue

            if mouth == 1 and day == 24:
                with open('data.csv', 'a', encoding='utf-8-sig',newline='') as csvfile:
                    fieldnames = [
                                '时间',
                                '新增确诊人数',
                                '新增死亡人数',
                                '新增疑似人数',
                                '新增治愈人数',
                                '现有确诊人数',
                                '累计治愈人数', # 累计治愈人数
                                '累计死亡人数', # 累计死亡人数
                                '累计确诊人数', # 现有确诊人数
                                '现有疑似人数', # 现有疑似人数
                                '累计密切接触者' # 累计密切接触者
                            ]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()


            with open('data.csv', 'a', encoding='utf-8',newline='') as csvfile:
                fieldnames = [
                            '时间',
                            '新增确诊人数',
                            '新增死亡人数',
                            '新增疑似人数',
                            '新增治愈人数',
                            '现有确诊人数',
                            '累计治愈人数', # 累计治愈人数
                            '累计死亡人数', # 累计死亡人数
                            '累计确诊人数', # 现有确诊人数
                            '现有疑似人数', # 现有疑似人数
                            '累计密切接触者' # 累计密切接触者
                        ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                # writer.writeheader()
                writer.writerow(dict)
