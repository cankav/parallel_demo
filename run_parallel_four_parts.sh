rm output*
python3 parallel_processing.py 0 25000000 &> output1 &
python3 parallel_processing.py 25000000 50000000 &> output2 &
python3 parallel_processing.py 50000000 75000000 &> output3 &
python3 parallel_processing.py 75000000 100000000 &> output4 &
