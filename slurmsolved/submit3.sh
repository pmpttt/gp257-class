#!/bin/bash
#SBASH --ntasks=1
#SBASH --ntime=0-2:0:0
#SBASH --cpus-per-task=1
#SBASH --mem=1gb
#SBASH --partition=debug

spack load /tye3sty
python3 ./averands.py
