import matplotlib.pyplot as plt

courses=['math','art','science','pe']
scores=[98,89,91,100]

pos=list(range(4))
plt.barh(pos,scores, color='blue')
plt.yticks(pos,labels=courses)
plt.show()