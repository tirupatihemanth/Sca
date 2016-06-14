
from matplotlib import pyplot;
from pylab import genfromtxt;
from scipy.stats import pearsonr;
# with open("../data/raw_data/www.google.com1") as f:
#     time = [];
#     footprint = [];
#     for line in f:
#         line = str(line).rstrip();
#         line = line.split();
#         time.append(line[0]);
#         footprint.append(line[1]);

mat = genfromtxt("../data/attack_data/processed_dtw27074")
mat1 = genfromtxt("../data/processed_dtw/www.google.com5");
mat2 = genfromtxt("../data/processed_dtw/www.google.com2");
mat3 = genfromtxt("../data/processed_dtw/www.facebook.com1");
mat4 = genfromtxt("../data/processed_dtw/www.youtube.com1");
mat5 = genfromtxt("../data/processed_dtw/www.github.com1");
mat6 = genfromtxt("../data/processed_dtw/www.gmail.com1");

matLen = len(mat[:,1]);
print pearsonr(mat[:,1][matLen-(len(mat1[:,1])):], mat1[:,1]);

# print str(mat); 
# pyplot.plot(mat[:,0], mat[:,1], label = "data1");
# pyplot.plot(mat1[:,0], mat1[:,1], label = "data2");
# pyplot.plot(mat2[:,0], mat2[:,1], label = "data3");
# pyplot.legend();
# pyplot.show();
