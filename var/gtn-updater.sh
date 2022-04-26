#!/bin/bash
for topicdir in /training-material/topics/*
do
    topic=$(basename $topicdir)
    echo "TOPIC: ${topic^^} "
    echo "----------------------------------------------" 
    for tutdir in $topicdir/tutorials/*
    do
        tut=$(basename $tutdir)
        # install tools and workflows
        if [ -d $tutdir/workflows/ ];
        then
            for w in $tutdir/workflows/*.ga
            do
                python3 ./gtn-updater.py $w $topic
            done
        fi
    done
done