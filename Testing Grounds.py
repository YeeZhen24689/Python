import numpy as np

root = np.roots([1,2.3,4.5,1.0])
print(root)
for i in root:
    if isinstance(i,complex):
        print("Complex Detected!!")
    else:
        print("Not Complex")


