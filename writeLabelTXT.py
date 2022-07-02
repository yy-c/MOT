
import os

data_path = "dataset"
set_list = os.listdir(data_path)
set_list

for idx in set_list:
    try:
        int(idx)
    except:
        continue
    det_path = os.path.join(data_path,idx,'det','det.txt')
    label_list = []
    with open(det_path) as fp:
        for line in fp.readlines():
            if len(line.strip('\n')) == 0:
                continue
            label_list.append([*map(lambda x:int(x), line.strip().split(','))])
    
    label_path = os.path.join(data_path,idx,'label')
    isExists = os.path.exists(label_path)
    if not isExists:
        os.makedirs(label_path)
        print(label_path + ' 创建成功')
    else:
        print(label_path + ' 目录已存在')

    flg = label_list[0][0]
    row_num = len(label_list)
    row_idx = 0
    label_single = []
    while row_idx < row_num:
        if label_list[row_idx][0] == flg:
            label_single.append(label_list[row_idx])
            row_idx += 1
        
        else:
            file_name_id = None
            if flg < 10:
                file_name_id = "000"+str(flg)
            elif flg < 100:
                file_name_id = "00"+str(flg)
            elif flg < 1000:
                file_name_id = "0"+str(flg)
            else:
                file_name_id = str(flg)

            write_path = os.path.join(label_path,'out'+idx+'_'+file_name_id+'.txt')
            label_file = open(write_path, 'w+')
            for line_single in label_single:
                temp_s = str(line_single).replace('[', '').replace(']', '') + '\n'
                label_file.write(temp_s)
            label_file.close()

            flg = label_list[row_idx][0]
            label_single = []
    
    file_name_id = None
    if flg < 10:
        file_name_id = "000"+str(flg)
    elif flg < 100:
        file_name_id = "00"+str(flg)
    elif flg < 1000:
        file_name_id = "0"+str(flg)
    else:
        file_name_id = str(flg)

    write_path = os.path.join(data_path,idx,'label','out'+idx+'_'+file_name_id+'.txt')
    label_file = open(write_path, 'w+')
    for line_single in label_single:
        temp_s = str(line_single).replace('[', '').replace(']', '') + '\n'
        label_file.write(temp_s)
    label_file.close()
    print(label_path + '写入完成')



