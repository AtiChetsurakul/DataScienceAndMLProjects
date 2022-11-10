import pandas as pd
import scipy.io
import sys
print(len(sys.argv))
assert len(
    sys.argv) == 2, 'data require 1 to use -> python3 mat_to_csv.py PATH_OF_FILE_HERE'
mat = scipy.io.loadmat(sys.argv[1])
mat = {k: v for k, v in mat.items() if k[0] != '_'}
# compatible for both python 2.x and python 3.x
data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})

data.to_csv("test_file.csv")

SRC = 'https://gist.github.com/sasadep/b2c174cdb8613b908480c605b2c2788a'
print(f'CODE from {SRC}')
