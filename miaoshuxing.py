import os
import configparser
data_path = "杰瑞杯初赛测试集test-1"
set_list = os.listdir(data_path)
set_list.sort()
i = 0
while i < len(set_list):
    try:
        int(set_list[i])
        i += 1
    except:
        set_list.pop(i)
set_list

name = []
imDir = []
frameRate = []
seqLength = []
imWidth = []
imHeight = []
imExt = []
isharbor = []
isdeparture = []
isentering = []
issea = []
isfog = []
isstrongbacklit = []
for idx in set_list:
    try:
        int(idx)
    except:
        continue
    info_path = os.path.join(data_path,idx,'seqinfo.ini')
    config = configparser.ConfigParser() # 类实例化
    config.read(info_path)
    name.append(config.get('Sequence','name'))
    imDir.append(config.getint('Sequence','imDir'))
    frameRate.append(config.getint('Sequence','frameRate'))
    seqLength.append(config.getint('Sequence','seqLength'))
    imWidth.append(config.getint('Sequence','imWidth'))
    imHeight.append(config.getint('Sequence','imHeight'))
    imExt.append(config.get('Sequence','imExt'))
    isharbor.append(config.getint('Sequence','isharbor'))
    isdeparture.append(config.getint('Sequence','isdeparture'))
    isentering.append(config.getint('Sequence','isentering'))
    issea.append(config.getint('Sequence','issea'))
    isfog.append(config.getint('Sequence','isfog'))
    isstrongbacklit.append(config.getint('Sequence','isstrongbacklit'))
    
siz = []
for i in range(len(imWidth)):
    siz.append([imWidth[i],imHeight[i]])
