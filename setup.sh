# http://www.couchbase.com/communities/c-client-library
sudo wget -O/etc/apt/sources.list.d/couchbase.list http://packages.couchbase.com/ubuntu/couchbase-ubuntu1404.list
wget -O- http://packages.couchbase.com/ubuntu/couchbase.key | sudo apt-key add - 
sudo apt-get update
sudo apt-get install libcouchbase2-libevent libcouchbase-dev
