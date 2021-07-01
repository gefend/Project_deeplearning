import pandas as pd
import numpy as np

from src.datasets import DrawDataset, get_train_val_samples
from src import config

VAL_KEY_ID_PATH = './data/val_key_ids_002.json'
TRAIN_KEY_ID_PATH = './data/train_key_ids_002.json'
TEST_KEY_ID_PATH = './data/test_key_ids_002.json'
train_samples, val_samples, test_samples = get_train_val_samples(VAL_KEY_ID_PATH, TRAIN_KEY_ID_PATH, TEST_KEY_ID_PATH)
test_df = pd.read_csv(config.TEST_SIMPLIFIED_PATH)

data=[]
data_compare=[]
n_samples=len(test_samples[0])
key_id=np.arange(n_samples)
for i in range(n_samples):
    point={"key_id":key_id[i],"countrycode":test_samples[2][i],"drawing":test_samples[0][i]}
    point_compare={"key_id":key_id[i],"countrycode":test_samples[2][i],"drawing":test_samples[0][i],"word":test_samples[1][i]}
    data.append(point)
    data_compare.append(point_compare)
df = pd.DataFrame(data)
df_compare=pd.DataFrame(data_compare)
df.to_csv('./data/my_test_simplified.csv', index=False)
df_compare.to_csv('./data/my_test_simplified_compare.csv', index=False)
