#!/bin/sh -
#
# This script generates a UUID. For Linux systems, this will be a time-based UUID.

if [ "$(uname)" == Linux ]
then
    uuidgen -t
else
    uuidgen
fi
