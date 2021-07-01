import pandas as pd
import tqdm
import json
import random
import numpy as np
from os.path import join
from sklearn.model_selection import train_test_split

from src import config

SAVE_NAME_VAL = 'val_key_ids_002'
SAVE_NAME_TEST= 'test_key_ids_002'
SAVE_NAME_TRAIN='train_key_ids_002'
VAL_SPLIT = 0.002
SAVE_PATH_VAL = join(config.DATA_DIR, SAVE_NAME_VAL+'.json')
SAVE_PATH_TEST = join(config.DATA_DIR, SAVE_NAME_TEST+'.json')
SAVE_PATH_TRAIN = join(config.DATA_DIR, SAVE_NAME_TRAIN+'.json')

if __name__ == '__main__':
    random.seed(42)
    np.random.seed(42)

    val_key_ids = []
    test_key_ids = []
    train_key_ids=[]
    for cls in tqdm.tqdm(config.CLASSES):
        class_df = pd.read_csv(config.CLASS_TO_CSV_PATH[cls])
        class_key_ids = class_df.key_id
        train_id, val_test_id = train_test_split(class_key_ids, test_size=2*VAL_SPLIT)
        val_key_ids += val_id.tolist()
        test_key_ids += test_id.tolist()
        train_key_ids += train_id.tolist()
        if len(val_key_ids) > 15:
            break


    with open(SAVE_PATH_VAL, 'w') as file:
        file.write(json.dumps(val_key_ids))
    with open(SAVE_PATH_TEST, 'w') as file:
        file.write(json.dumps(test_key_ids))
    with open(SAVE_PATH_TRAIN, 'w') as file:
        file.write(json.dumps(train_key_ids))

    print("Validation key ids saved to", SAVE_PATH_VAL)
    print("Train key ids saved to", SAVE_PATH_TRAIN)
    print("Test key ids saved to", SAVE_PATH_TEST)
