import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader

from src.datasets import DrawDataset, get_train_val_samples
from src.transforms import ImageTransform, DrawTransform
import src.config as config

image_size = 256
scale_size = 128
image_pad = 3
shake = [0, 3, 5, 7]
image_line_width = 3
train_epoch_size = 10_000
num = 4

if __name__ == "__main__":
    _, samples = get_train_val_samples('./data/val_key_ids_003.json', None)
    n = len(samples[0])
    trns = ImageTransform(True, scale_size)
    fig = plt.figure()
    for j in range(len(shake)):
        draw_transform = DrawTransform(image_size, image_pad, image_line_width, False, shake[j])
        dataset = DrawDataset(samples, draw_transform, size=train_epoch_size, image_transform=trns)
        loader = DataLoader(dataset, batch_size=n, num_workers=0, shuffle=False)
        for img, trg in loader:
            c = np.zeros(num)
            for i in range(n):
                label = trg[i].item()
                if (c[label] > 0):
                    continue
                c[label] = 1
                ax = fig.add_subplot(len(shake), num, j*num+label+1)
                img_i = 1 - img[0][i, :, :, :].numpy().transpose((1,2,0))
                if (shake[j]==0):
                    s = ' no shake'
                else:
                    s = ' shake=' + str(shake[j])
                ax.set_title(config.IDX_TO_CLASS[label] + s)
                ax.imshow(img_i)
                ax.set_axis_off()
            if np.prod(c) > 0:
                break
    plt.show()
