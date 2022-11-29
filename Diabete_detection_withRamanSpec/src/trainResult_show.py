import matplotlib.pyplot as plt

def loss_plot_sub(train_loss_each_location,val_loss_each_location,val_acc_each_location,DATALABEL,model_name):
    fig, axs = plt.subplots(2,2, figsize=(10, 10))
    fig.suptitle(f'loss_plot for {model_name}')
    for ax,trainloss,valloss,valacc,label in zip(axs.flat,train_loss_each_location,val_loss_each_location,val_acc_each_location,DATALABEL):
        ax.plot(trainloss,label=f'train loss')
        ax.plot(valloss,label=f'val loss with acc = {valacc}')
        ax.set_title(label)
        ax.legend()

        # pass
    plt.show()