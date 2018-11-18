import matplotlib.pyplot as plt

#przeżywalność
dane=[10,18]
index = ["kobiety","mężczyźni"]
colors=["r","g"]

plt.bar(index,dane)

# index to odpowiednik osi x
# dane to odp

plt.bar(index,dane, color=colors)
plt.show()