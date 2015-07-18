#!/usr/bin/env bash

cd robot
ls *.robot | xargs pybot
cd -