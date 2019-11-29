rm output*
python3 parallel_processing.py 0 50000000 &> output1 &
python3 parallel_processing.py 50000000 100000000 &> output2 &
