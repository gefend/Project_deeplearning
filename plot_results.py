import numpy as np
import matplotlib.pyplot as plt
val_line = []
train_line = []
line_number = 0
with open(r"C:\Users\97252\OneDrive - Technion\תואר שני- חשמל\למידה עמוקה\project\log.txt", "r") as f:
    for line in f:
        line_number += 1
        if 'INFO Validation' in line:
            val_line.append(line)
        if 'INFO Train' in line:
            train_line.append(line)
epoch = np.zeros(len(val_line))
val_loss = np.zeros(len(val_line))
val_acc = np.zeros(len(val_line))
val_map_at_k = np.zeros(len(val_line))
LR = np.zeros(len(train_line))
train_loss = np.zeros(len(train_line))

for i in range(len(train_line)):
    split_train_line = train_line[i].split()
    epoch_tmp = split_train_line[6]
    epoch[i] = float(epoch_tmp[:-1])
    LR_tmp = split_train_line[8]
    LR[i] = float(LR_tmp[:-1])
    train_loss_tmp = split_train_line[10]
    train_loss[i] = float(train_loss_tmp[:-1])

for i in range(len(val_line)):
    split_val_line = val_line[i].split()
    epoch_tmp = split_val_line[6]
    epoch[i] = float(epoch_tmp[:-1])
    val_map_at_k[i] = float(split_val_line[12])
    val_loss_tmp = split_val_line[8]
    val_loss[i] = float(val_loss_tmp[:-1])
    val_acc_tmp = split_val_line[10]
    val_acc[i] = float(val_acc_tmp[:-1])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(epoch[0:3], val_map_at_k[0:3])
plt.xticks(epoch[0:3])
plt.xlabel('Epoch')
plt.ylabel('Val MAP@3')
plt.title('Val MAP@3')
plt.show()

fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(epoch[0:3], val_acc[0:3])
plt.xticks(epoch[0:3])
plt.xlabel('Epoch')
plt.ylabel('Val accuracy')
plt.title('Val accuracy')
plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.plot(epoch[0:3], val_loss[0:3])
plt.xticks(epoch[0:3])
plt.xlabel('Epoch')
plt.ylabel('Val loss')
plt.title('Val loss')
plt.show()

fig3 = plt.figure()
ax = fig3.add_subplot(111)
ax.plot(epoch[0:3], train_loss[0:3])
plt.xticks(epoch[0:3])
plt.xlabel('Epoch')
plt.ylabel('Train loss')
plt.title('Train loss')
plt.show()

fig4 = plt.figure()
ax = fig4.add_subplot(111)
ax.plot(epoch[0:3], LR[0:3])
plt.xticks(epoch[0:3])
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title('Learning Rate')
plt.show()

