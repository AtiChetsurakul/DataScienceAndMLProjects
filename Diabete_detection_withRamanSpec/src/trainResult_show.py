import matplotlib.pyplot as plt

def loss_plot_sub(train_loss_each_location,val_loss_each_location,val_acc_each_location,DATALABEL):
    fig, axs = plt.subplots(2,2, figsize=(10, 10))
    fig.suptitle('loss_plot')
    for ax,trainloss,valloss,valacc,label in zip(axs.flat,train_loss_each_location,val_loss_each_location,val_acc_each_location,DATALABEL):
        ax.plot(trainloss,label=f'train loss on {label}')
        ax.plot(valloss,label=f'val loss on {label} with acc = {valacc}')
        ax.set_title(label)
        ax.legend()

        # pass
    plt.show()