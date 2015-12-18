#!/bin/bash
pmap -d $1 | grep "writeable/private" | awk '{print $4}'
