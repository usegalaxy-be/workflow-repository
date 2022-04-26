#!/bin/bash
echo $PWD
for topicdir in $PWD/training-material/topics/*
do
    topic=$(basename $topicdir)
    echo "TOPIC: ${topic^^} - ${topicdir}"
    echo "----------------------------------------------" 
    for tutdir in $topicdir/tutorials/*
    do
        tut=$(basename $tutdir)
        # install tools and workflows
        if [ -d $tutdir/workflows/ ];
        then
            for w in $tutdir/workflows/*.ga
            do
                python3 $PWD/var/gtn-updater.py $PWD $w $topic
            done
        fi
    done
done