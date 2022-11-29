import torch
from torch.utils.data import TensorDataset

def shuffleloadertorch(ds_earloop,ds_inarm,ds_thumbnail,ds_vain,seed,train_size = 12, val_size = 4,batch_size=12,valbatch_size=4):
    '''This function'''
    torch.manual_seed(seed)
    train_set0, val_set0 = torch.utils.data.random_split(ds_earloop, [train_size, val_size])
    train_set1, val_set1 = torch.utils.data.random_split(ds_inarm, [train_size, val_size])
    train_set2, val_set2 = torch.utils.data.random_split(ds_thumbnail, [train_size, val_size])
    train_set3, val_set3 = torch.utils.data.random_split(ds_vain, [train_size, val_size])

    train_loader0 = torch.utils.data.DataLoader(dataset=train_set0,batch_size=batch_size,shuffle=True)
    val_loader0 = torch.utils.data.DataLoader(dataset=val_set0, batch_size=valbatch_size, shuffle=True)

    train_loader1 = torch.utils.data.DataLoader(dataset=train_set1,batch_size=batch_size,shuffle=True)
    val_loader1 = torch.utils.data.DataLoader(dataset=val_set1, batch_size=valbatch_size, shuffle=True)

    train_loader2 = torch.utils.data.DataLoader(dataset=train_set2,batch_size=batch_size,shuffle=True)
    val_loader2 = torch.utils.data.DataLoader(dataset=val_set2, batch_size=valbatch_size, shuffle=True)

    train_loader3 = torch.utils.data.DataLoader(dataset=train_set3,batch_size=batch_size,shuffle=True)
    val_loader3 = torch.utils.data.DataLoader(dataset=val_set3, batch_size=valbatch_size, shuffle=True)


    train_loader_all = [train_loader0,train_loader1,train_loader2,train_loader3]
    val_loader_all = [val_loader0,val_loader1,val_loader2,val_loader3]
    return train_loader_all,val_loader_all
