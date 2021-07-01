import pandas as pd

model = pd.read_csv(
    '/home/gefen/Documents/repos/argus-quick-draw/data/predictions'
    '/iter_size_se_resnext50_testsplit__hflip50_shake3_001/model-025-0.967125/submission.csv')
original = pd.read_csv('/home/gefen/Documents/repos/argus-quick-draw/data/my_test_simplified_compare.csv')
labels_model=model['word']
labels_original=original['word']
count=0
for i in range(len(labels_model)):
    if labels_model[i] == labels_original[i]:
        print(i)
        count = count+1
test_acc = count/len(labels_model)
c=1