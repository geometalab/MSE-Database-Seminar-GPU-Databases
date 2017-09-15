#!/bin/bash

blazing_arch="$1"

if [ -z "$blazing_arch" ]; then
    blazing_arch="x86_64"
fi

if [ "$blazing_arch" != "x86_64" ] && [ "$blazing_arch" != "ppc64le" ]; then
    echo "Unsupported architecture '$blazing_arch' for BlazingDB Community Edition!"
    exit 1
fi

simplicity_url="http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/ubuntu16.04/Simplicity_CommunityRelease_$blazing_arch"

echo "Installing BlazingDB for '$blazing_arch' architecture ..."

# Install tools & utils
apt-get install -y --no-install-recommends sudo bzip2 wget curl nano lsof htop net-tools

# Install Simplicity runtime dependencies
apt-get install -y --no-install-recommends libxerces-c3.1 libcurl3 libssl1.0.0 zlib1g libuuid1

# Install Webapp runtime dependencies
apt-get install -y --no-install-recommends openjdk-8-jre

#BEGIN Create BlazingDB Folders
#read -p "Enter the BlazingDB root folder [/opt/blazing/]: " anaconda2_home
echo "The BlazingDB Server folders are in /opt/blazing"
blazing_root_folder=/opt/blazing/
mkdir -p ${blazing_root_folder}/disk1
mkdir -p ${blazing_root_folder}/disk1/blazing
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing/default
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing-rows-data
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing-rows-data/default
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing-r-connector
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing-uploads
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing-uploads/default
mkdir -p ${blazing_root_folder}/disk1/blazing/blazing-uploads/admin
mkdir -p ${blazing_root_folder}/disk2
wget http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/blazing.conf -O ${blazing_root_folder}/disk1/blazing/blazing.conf
wget http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/nodes.config -O ${blazing_root_folder}/disk1/blazing/blazing/nodes.config
#END BlazingDB Folders

#BEGIN Install BlazingDB Server
echo "The BlazingDB server is /usr/bin/Simplicity"
wget $simplicity_url -O ${blazing_root_folder}/Simplicity
chmod +x ${blazing_root_folder}/Simplicity
#END Install BlazingDB Server

#BEGIN Install Blazing Workbench
mkdir -p ${blazing_root_folder}/workbench
wget http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/driver.properties -O ${blazing_root_folder}/driver.properties
wget http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/blazing-workbench.jar -O ${blazing_root_folder}/workbench/blazing-workbench.jar
wget http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/data.mv.db -O ${blazing_root_folder}/workbench/data.mv.db
wget http://blazing-public-downloads.s3-website-us-west-2.amazonaws.com/installer/v1.3/data.trace.db -O ${blazing_root_folder}/workbench/data.trace.db
#END Install Blazing Workbench

echo "Installation complete!"
