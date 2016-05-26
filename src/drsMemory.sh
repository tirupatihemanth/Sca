#!/bin/bash
cat /proc/$1/statm | awk '{print $6}'
