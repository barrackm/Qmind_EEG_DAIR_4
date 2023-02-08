from brainflow import *
import time
import numpy as np
import pandas as pd

params = BrainFlowInputParams()
params.serial_port = "/dev/cu.usbserial-D200PWD5"
board = BoardShim(BoardIds.CYTON_BOARD, params)


board.prepare_session()
board.start_stream()

time.sleep(10)

data = board.get_board_data()
board.stop_stream()
board.release_session()

print(data)

DataFilter.write_file(data, 'test.csv', 'w')  # use 'a' for append mode
restored_data = DataFilter.read_file('test.csv')
restored_df = pd.DataFrame(np.transpose(restored_data))
print('Data From the File')
print(restored_df.head(10))
