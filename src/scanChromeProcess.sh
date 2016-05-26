#!/bin/bash
for i in `ps -aux | grep "chrome --type=renderer" | grep -v " --extension-process"| grep -v " grep .*chrome --type=renderer"| awk '{print $2}' `
do
	echo $i
done
