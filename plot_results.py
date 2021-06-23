import numpy as np
import matplotlib.pyplot as plt


def get_results(log_file_path):
    val_line = []
    train_line = []
    line_number = 0
    with open(log_file_path, "r") as f:
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
    return epoch, val_acc, val_loss, val_map_at_k, LR, train_loss


log_file_path_noshake = r"/home/gefen/Documents/repos/argus-quick-draw/data/experiments" \
                        r"/iter_size_se_resnext50_testsplit_001/log.txt"
epoch, val_acc, val_loss, val_map_at_k, LR, train_loss = get_results(log_file_path_noshake)
log_file_path_shake3 = r"/home/gefen/Documents/repos/argus-quick-draw/data/experiments" \
                        r"/iter_size_se_resnext50_testsplit_shake3_001/log.txt"
epoch3, val_acc3, val_loss3, val_map_at_k3, LR3, train_loss3 = get_results(log_file_path_shake3)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(epoch, val_map_at_k)
ax.plot(epoch3[:25], val_map_at_k3[:25])
plt.xticks(epoch)
plt.xlabel('Epoch')
plt.ylabel('Val MAP@3')
plt.title('Val MAP@3')
plt.legend(['noshake','shake'])
plt.show()

fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(epoch, val_acc)
ax.plot(epoch3[:25], val_acc3[:25])
plt.xticks(epoch)
plt.xlabel('Epoch')
plt.ylabel('Val accuracy')
plt.title('Val accuracy')
plt.legend(['noshake','shake'])
plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111)
ax.plot(epoch, val_loss)
ax.plot(epoch3[:25], val_loss3[:25])
plt.xticks(epoch)
plt.xlabel('Epoch')
plt.ylabel('Val loss')
plt.title('Val loss')
plt.legend(['noshake','shake'])
plt.show()

fig3 = plt.figure()
ax = fig3.add_subplot(111)
ax.plot(epoch, train_loss)
ax.plot(epoch3[:25], train_loss3[:25])
plt.xticks(epoch)
plt.xlabel('Epoch')
plt.ylabel('Train loss')
plt.title('Train loss')
plt.legend(['noshake','shake'])
plt.show()

fig4 = plt.figure()
ax = fig4.add_subplot(111)
ax.plot(epoch, LR)
ax.plot(epoch3[:25], LR3[:25])
plt.xticks(epoch)
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.title('Learning Rate')
plt.legend(['noshake','shake'])
plt.show()
