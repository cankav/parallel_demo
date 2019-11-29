rm output*
MAX=100000000
for i in {1..10}
do
    python3 parallel_processing.py $((MAX/8*($i-1))) $((MAX/8*$i)) &> output$i &
done
