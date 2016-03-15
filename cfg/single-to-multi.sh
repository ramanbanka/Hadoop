#!/bin/bash

if [ $(id -u) -ne 0 ]; then
 echo "This script must be run as root";
 exit 1;
fi

fromDir=multi-node
toDir=/home/hduser/hadoop/etc/hadoop/

cp $fromDir/hdfs-site.xml $toDir
cp $fromDir/yarn-site.xml $toDir
cp $fromDir/core-site.xml $toDir
cp $fromDir/mapred-site.xml $toDir
cp $fromDir/masters $toDir
cp $fromDir/master $toDir
cp $fromDir/slaves $toDir
cp $fromDir/hosts /etc/

