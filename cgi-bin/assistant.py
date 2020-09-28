#!/usr/bin/python3

print("content-type:text/html\n")

print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<title>Output</title>')
print('<style>')
print('.container { width: 75%; margin: 0 auto; font-family: sans-serif; }')
print('.heading { width: 100%; background-color: black; color: white; padding: 0.4em 0; margin: 0 auto; }')
print('.heading p { text-align: center; margin: 10px 0; font-size: 2em; font-weight: bold; }')
print('h1 { text-align: center; padding: 15px 0; font-size: 1.8em; }')
print('input { width: 98.5%; margin: 5px 0; padding: 15px 0; }')
print('button { width: 100%; margin: 5px 0; padding: 15px 5px; font-size: 1em; font-weight: bold; }')
print('</style>')
print('</head>')
print('<body>')
print('<div class="container"><hr><div class="heading"><p>Output</p></div><hr>')

import sys
import cgi
import webbrowser as browser
import subprocess as sp
import platform

if __name__ == "__main__":

    # Check OS Type
    sys_type = platform.system()

    # Validate For Windows And Linux Only
    if sys_type != "Linux":
        print("****** This System Not Supported ******")
        sys.exit("Closing Assistant")

    form = cgi.FieldStorage()

    # Taking Query From User
    query = form.getvalue("cmd").lower()
    print("<h1>Your Query : {0}</h1>".format(query))
    print()
    spout = ()


    if ("show" in query or "what" in query or "system" in query or "print" in query) and (
        "ip" in query or "ip address" in query or "address" in query
    ):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("ifconfig")
            if spout[0] == 0:
                output = sp.check_output("ifconfig", shell=True)
                output = output.decode("utf-8")
                print("<h3><pre>{0}</pre></h3>".format(output))
            else:
                print("Command Failed")
    elif (
        "open" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
        or "print" in query
    ) and "date" in query:
        if sys_type == "Linux":
            spout = sp.getstatusoutput("date")
            if spout[0] == 0:
                print("<h3>{0}</h3>".format(spout[1]))
            else:
                print("Command Failed")
    elif (
        "open" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
    ) and "calendar" in query:
        if sys_type == "Linux":
            spout = sp.getstatusoutput("cal")
            if spout[0] == 0:
                output = sp.check_output("cal", shell=True)
                output = output.decode("utf-8")
                print("<h3><pre>{0}</pre></h3>".format(output))
            else:
                print("Command Failed")
    elif ("show" in query or "show all" in query or "give" in query or "print" in query) and ("process" in query or "running process" in query):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("ps -aux")
            if spout[0] == 0:
                output = sp.check_output("ps -aux", shell=True)
                output = output.decode("utf-8")
                print("<h3><pre>{0}</pre></h3>".format(output))
            else:
                print("Command Failed")
    elif ("show" in query or "run" in query or "print" in query or "give" in query) and ("working" in query or "current" in query or "present working" in query) and "directory" in query:
        if sys_type == "Linux":
            spout = sp.getstatusoutput("pwd")
            if spout[0] == 0:
                print("<h3>{0}</h3>".format(spout[1]))
            else:
                print("Command Failed")
    elif ("show" in query or "show all" in query or "give" in query or "execute" in query) and ("running" in query) and ("docker" in query or "dockers" in query or "container" in query or "containers" in query):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("sudo docker ps")
            if spout[0] == 0:
                output = sp.check_output("sudo docker ps", shell=True)
                output = output.decode("utf-8")
                print('<h3><pre>{0}</pre></h3>'.format(output))
            else:
                print("<h3>Command Failed</h3>")
                print("<h3>{0}</h3>".format(spout))
    elif ("launch" in query or "create" in query or "run" in query) and ("docker" in query or "container" in query):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("sudo docker run -dit centos:latest")
            if spout[0] == 0:
                print("<h3>Your Centos Container Is Running</h3><br>")
                print('<h3>Running Containers</h3><br>')
                output = sp.check_output("sudo docker ps", shell=True)
                output = output.decode("utf-8")
                print('<h3><pre>{0}</pre></h3>'.format(output))
            else:
                print("<h3>Failed To Start Container</h3>")
                print("<h3>{0}</h3>".format(spout))
    elif ("show" in query or "show all" in query or "print" in query or "give" in query or "execute" in query) and ("docker" in query or "container" in query) and ("images" in query or "image" in query):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("sudo docker images")
            if spout[0] == 0:
                output = sp.check_output("sudo docker images", shell=True)
                output = output.decode("utf-8")
                print('<h3><pre>{0}</pre></h3>'.format(output))
            else:
                print("<h3>Command Failed</h3>")
                print("<h3>{0}</h3>".format(spout))
    elif ("show" in query or "show all" in query or "print" in query or "give" in query or "execute" in query) and ("docker" in query or "dockers" in query or "container" in query or "containers" in query):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("sudo docker ps -a")
            if spout[0] == 0:
                output = sp.check_output("sudo docker ps -a", shell=True)
                output = output.decode("utf-8")
                print('<h3><pre>{0}</pre></h3>'.format(output))
            else:
                print("<h3>Command Failed</h3>")
                print("<h3>{0}</h3>".format(spout))
    elif ("remove" in query or "remove all" in query or "delete" in query or "delete all" in query or "clear" in query) and ("docker" in query or "dockers" in query or "container" in query or "containers" in query):
        if sys_type == "Linux":
            spout = sp.getstatusoutput("sudo docker rm -f $(sudo docker container ps -a -q)")
            if spout[0] == 0:
                print('<h3>All Containers Removed</h3>')
            else:
                print("<h3>Command Failed</h3>")
                print("<h3>{0}</h3>".format(spout))
    elif (
        "open" in query
        or "start" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
    ) and ("facebook" in query or "fb" in query):
        if sys_type == "Linux":
            print('<meta http-equiv="refresh" content="0;url={0}" />'.format("https://facebook.com/"))
            print('<h3>Opening Facebook...')
    elif ("open" in query
        or "start" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
    ) and ("instagram" in query or "ig" in query):
        if sys_type == "Linux":
            print('<meta http-equiv="refresh" content="0;url={0}" />'.format("https://instagram.com/"))
            print('<h3>Opening Instagram...')
    elif (
        "open" in query
        or "start" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
    ) and "twitter" in query:
        if sys_type == "Linux":
            print('<meta http-equiv="refresh" content="0;url={0}" />'.format("https://twitter.com/"))
            print('<h3>Opening Twitter...')
    elif (
        "open" in query
        or "start" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
    ) and "linkedin" in query:
        if sys_type == "Linux":
            print('<meta http-equiv="refresh" content="0;url={0}" />'.format("https://in.linkedin.com/"))
            print('<h3>Opening LinkedIn...')
    elif (
        "open" in query
        or "start" in query
        or "run" in query
        or "execute" in query
        or "launch" in query
        or "show" in query
    ) and "discord" in query:
        if sys_type == "Linux":
            print('<meta http-equiv="refresh" content="0;url={0}" />'.format("https://discord.com/"))
            print('<h3>Opening Discord...')
    else:
        print("<h3>**** This Feature Is Not Supported ****</h3>")
        
print('<form><table>')
print('<tr><td>')
print('<a href="http://192.168.1.11/"><button type="button">Retry ? </button></a>')
print('</td></tr>')
print('</table></form>')
print('</div>')
print('</body>')
print('</html>')
