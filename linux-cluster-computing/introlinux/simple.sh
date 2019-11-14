#!/bin/bash

echo "Running lscpu command."
echo "This is what it does:"
lscpu --help 
echo

echo "Printing results in cpu.log..."
lscpu > cpu.log
sleep 1
date >> cpu.log
echo

echo "Done"

