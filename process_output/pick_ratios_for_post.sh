#!/bin/bash
set -e
for ratio in 0.01 0.10 0.15 0.20
do
	python3 picklist_ratio.py ../output/alive_during_1809/profileid_alive_during_1809.txt alive_1809_$ratio.txt $ratio
	java ReadNodes ../../familinx/relations-anon.txt alive_1809_$ratio.txt output_$ratio.txt
done
