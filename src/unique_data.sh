for i in `ls ../data/raw_data/`
do
	eval "awk '{x[\$2]++;if(x[\$2]==1 && \$2!=0){ var++;if(var==2) {start = \$1-1;print 0, 80320;}if(var>1) print \$1-start, \$2}}' < ../data/raw_data/$i > ../data/processed_data/$i" 
done