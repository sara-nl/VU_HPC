#!/bin/bash

echo "Running simple command..."
sleep 2
echo

lscpu --help > cpu.log
lscpu >> cpu.log

echo "Done"

