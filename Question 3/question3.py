import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
import datasets
torch.set_default_tensor_type(torch.FloatTensor)
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()


        self.fc1 = nn.Linear(3 * 1, 4)
        self.fc2 = nn.Linear(4, 4)
        self.fc3 = nn.Linear(4, 1)


    def forward(self, x):
        x = x.view(-1, 3 * 1)
        x = F.relu(self.fc1(x))


        x = F.relu(self.fc2(x))


        x = self.fc3(x)
        #     x = F.log_softmax(x,dim = 1)

        return x


model = Net()

criterion = nn.MSELoss()
# criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(params = model.parameters(),lr = 0.01)

num_workers = 0

batch_size = 1
datatmp = open('train_data.txt','r')
data = datatmp.readlines()[1:]
data = [dt.strip().split('\t') for dt in data]
data = np.array(data,dtype='float')
data= list(data)
labeltmp = open('train_truth.txt','r')
label = labeltmp.readlines()[1:]
label = [dt.strip().split('\t') for dt in label]
label = np.array(label,dtype='float')
label = list(label)
# label = torch.FloatTensor(label)
train_data = []
for k in range(len(data[1:])):
    kl = []
    ml = []
    kl.append(data[k][0])
    kl.append(data[k][1])
    kl.append(data[k][2])
    kl.append(label[k][0])
    train_data.append(kl)
# train_data = train_data.astype(float)
train_data = np.array(train_data)
# train_data = torch.from_numpy(train_data)

train_data = torch.from_numpy(train_data)
test_datatmp = open('test_data.txt','r')
test_data = test_datatmp.readlines()[1:]
test_data = [dt.strip().split('\t') for dt in test_data]
test_data = np.array(test_data,dtype='float')
test_data = np.array(test_data, dtype=float)
test_data = torch.FloatTensor(test_data)
# print(train_data.dtype)
train_loader = torch.utils.data.DataLoader(train_data,batch_size = batch_size,
                                           num_workers = num_workers)
test_loader = torch.utils.data.DataLoader(test_data,batch_size = batch_size,
                                         num_workers = num_workers)
def train():
    n_epochs = 1
    for epoch in range(n_epochs):
        train_loss = 0.0
        for dataandlabel in train_loader:
            datax1,datax2,datax3, target = dataandlabel.split(1,dim=1)
            data = torch.cat([datax1,datax2,datax3],dim=1)
            data = torch.tensor(data,dtype = torch.float)
            optimizer.zero_grad()
            output = model(data)  

            loss = criterion(output, target.float())
            loss.backward()

            optimizer.step()
            train_loss += loss.item() * data.size(0)
        train_loss = train_loss / len(train_loader.dataset)
        print('Epoch:  {}  \tTraining Loss: {:.6f}'.format(
            epoch + 1,
            train_loss))
def test():
    model.eval()  # prep model for *evaluation*
    fop = open('1.txt', 'w')
    for dataandlabel in test_loader:
        # forward pass: compute predicted outputs by passing inputs to the model
        datax1, datax2, datax3 = dataandlabel.split(1, dim=1)
        data = torch.cat([datax1, datax2, datax3], dim=1)
        data = torch.tensor(data, dtype=torch.float)
        output = model(data)
        ot = output.detach().numpy()

        fop.write(str(ot[0][0])+'\n')

train()
test()