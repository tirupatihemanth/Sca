for i in `ls ../data/raw_data/`
do
    eval "awk 'BEGIN{var=0;blah=-1;}{if((var==0 || blah==\$2) && \$2!=0){ var++;blah=\$2;}else if(var>0 && \$2!=0){start = \$1-1;var=-1;print 0, blah;print \$1-start, \$2;}else if(\$2!=0){ print \$1-start, \$2;}}' < ../data/raw_data/$i > ../data/processed_data/$i" 
done
