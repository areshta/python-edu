import os

def cmd_exec (cmd,  err_comment = "execution failed", need_exit = True):
    ret = os.system( cmd )
    if ret != 0:
        print (err_comment)
        if need_exit:
            exit(-1)
