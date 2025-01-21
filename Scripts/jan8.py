from calibrationFunctions import openFiles, calculateForce, calculateTetherExtension, findTetheredBeads
import matplotlib.pyplot as plt
import numpy as np


folderPath1 = r"C:\Users\Perkins Lab\Desktop\Caleb Maddry\Data\2025\January\8\Test1\DataTSV"

dataFrame1 = openFiles(folderPath1, numRef=3, numExp=7, fps=400)


# plt.plot(dataFrame1["linearMotor"][21000:39000])
lowStart = 21000
lowEnd = 39000

refBead = dataFrame1["zRefBead1"]
bead = dataFrame1["zExpBead4"]

# what is happening to 1,3
# 4 seems good
# 5,6 is mid

# plt.plot(bead - refBead)

lowForceIdx = [lowStart, lowEnd]

tetherBeads = findTetheredBeads(dataFrame1, lowForceIdx); 
dataFrame = calculateTetherExtension(dataFrame1, tetherBeads, lowForceIdx); 


plt.plot(dataFrame1["extensionExpBead4"])
plt.axvline(glassPosition, color="red")
plt.show()

