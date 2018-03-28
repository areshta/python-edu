#!/bin/bash

openssl des3 -salt -in in.txt -out in.des3 -k mypassword
openssl des3 -d -salt -in in.des3 -out out.txt -k mypassword
cat out.txt
