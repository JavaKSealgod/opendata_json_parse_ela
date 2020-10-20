# py3
import json, base64, os

file_dir = 'E:\\dpress\\http\\'

data_list = []


def bs4_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print(len(data))
    for i in data:
        i = json.loads(i)
        temp = base64.b64decode(i['data'])
        temp = temp.decode('utf-8','ignore')
        i['data'] = temp
        # data_list.append(i)
        i = json.dumps(i, ensure_ascii=False)
        name = file_name.split('\\')
        for ii in name:
            if '.txt' in ii:
                na = ii.split('.')[0]

        name = 'E:\\dpress\\http-c\\' + na + '.txt'
        i = json.dumps(i, ensure_ascii=False)
        with open(name, 'a', encoding='utf-8') as f:
            f.write(i)
            f.write('\n')
        #print('1')


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':  # 想要保存的文件格式
                L.append(os.path.join(root, file))

    return L


l = file_name(file_dir)
# print(l)
for i in l:
    #print(i)
    bs4_json(i)
