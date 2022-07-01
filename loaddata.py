import os
import numpy as np
import torch
import cv2.cv2 as cv2
from torch.utils.data import Dataset
from utils.axes_transform import transform

class ReadYOLO(Dataset):
    
    def __init__(self, phase="1", preproc=None, imagefiletype='jpg', labelfiletype='txt'):
        """_summary_

        Args:
            phase (str, optional): dataset ID. Defaults to "1".
            preproc (_type_, optional): tranforming methods. Defaults to None.
            imagefiletype (str, optional): type of image. Defaults to 'jpg'.
            labelfiletype (str, optional): type of label. Defaults to 'txt'.
        """
        super(ReadYOLO, self).__init__()
        self.preproc = preproc
        self.phase = phase
        self.imagefiletype = imagefiletype
        self.labelfiletype = labelfiletype
        
        self.labels = os.listdir(os.path.join('dataset',phase,'label')) # content of labels, one txt file to one image
        
    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self, item):
        # load label files
        label_list = []
        with open(os.path.join('dataset',phase,'label',self.labels[item]),'r') as fp:
            for line in fp.readlines():
                if len(line.strip('\n')) == 0:
                    continue
                label_list.append([*map(lambda x: float(x), line.strip().split(' '))])
        targer = torch.tensor(label_list)
        
        # load graph data
        pic_name = self.labels[item].split('.'+self.labelfiletype)[0]
        picture = None
        try:
            picture = torch.from_numpy(cv.imread(
                os.path.join('dataset', self.phase, self.phase, pic_name+'.'+self.imagefiletype)
            ).astype(np.float32)).permute(2,0,1)
        except AttributeError:
            print('opencv read picture error. The picture name is {}'.format(pic_name))
            quit()
            
        # target[:, 1:] = center_size(target[:,1:])
        if self.preproc:
            picture, target = self.preproc(picture, target, self.phase)
            
        return picture, target
    
if __name__ == '__main__':
    from Augmentation.data_augment import DataAugment
    from utils.config import cfg
    import torchvision
    import matplotlib.pyplot as plt
    
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    
    # Examples of preproc
    dataset = ReadYOLO(phase="1", preproc=data_augment, imagefiletype='jpg')
    
    picture, target = dataset[0]
    pic = torchvision.transforms.ToPILImage()(picture)
    plt.figure()
    pic = plt.imshow(pic)
    rect = plt.Rectangle(xy=(target[0,1]*320-0.5*target[0,4]*320, target[0,2]*320-0.5*target[0,3]*
                             320),
                         width=target[0,4]*320,
                         height=target[0,3]*320,
                         fill=False)
    pic.axes.add_patch(rect)