rm output*
python3 parallel_processing.py 0 33333333 &> output1 &
python3 parallel_processing.py 33333333 66666666  &> output2 &
python3 parallel_processing.py 66666666 100000000  &> output3 &
