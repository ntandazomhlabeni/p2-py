#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
DEBIAN_FRONTEND=noninteractive
export TERM=xterm

apt update
apt -y upgrade

cat /etc/*-release

