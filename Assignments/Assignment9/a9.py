import firewall as fw
import packet as p
import requests

#### DO NOT MODIFY FUNCTION BELOW ####
### The function below simulates
def simulateTraffic(question,fwObj,showTraffic = False): # modified the function to make verbose optional
    print("*************************Question ",question,"*************************")
    fwObj.verbose = showTraffic
    networkLog = open("networkLog.txt","r")
    for line in networkLog.readlines():
        x = line.split(" ")
        a = p.Packet(x[0],x[1],x[2])
        fwObj.inspectPacket(a)

    
    print("Total Packets:",fwObj.totalPacketsBlocked + fwObj.totalPacketsAllowed)
    print("Total Packets Blocked:",fwObj.totalPacketsBlocked)
    print("Total Packets Allowed:",fwObj.totalPacketsAllowed)
    print("Rules Used:",fwObj.rules)

    fwObj.resetPacketCount()

### BEGIN ASSIGNMENT BELOW ###

# 1. Your organization is in need of a firewall to block malicious 
# network traffic. You are being asked to implement a software based 
# firewall built in python. Follow the comments below to implement it.
# Create a new Firewall object with name "CS1411 Firewall". Review 
# the firewall class to see how the object initiated
# Note: Use "cs1411FW" as the object name
# Run your script to see traffic flow in. You should see 747 allowed packets.
# Your code here
cs1411FW = fw.Firewall("CS1411 Firewall")


#Uncomment line below when ready to test your solution
simulateTraffic("1",cs1411FW,False)


# 2. Now that traffic is flowing through the firewall, the security ops team
# has identified suspicious RDP traffic from 206.14.8.100 to 202.13.6.223. 
# Add a new firewall rule to your firewall to block the traffic.
# You may need to look up the port number for RDP.
# Refer to the firewall class for examples to add a rule.
# You should see 1 rule added
# Blocked: 7
# Your code here
cs1411FW.addRule("206.14.8.100", "202.13.6.223", "3389", "Block")



#Uncomment lines below when ready to test your solution
# Optional: Verbose Mode, change the value of v to True or False to see traffic blocked.
simulateTraffic("2",cs1411FW)

print("*************************Question  3a/3b *************************")
# 3a. What object type is the rules property of the firewall object?
# Use a print statement of the answer
# Your code here
print(type(cs1411FW.rules))

# 3b. What object type is a rule in the rules property of the firewall object?
# Use a print statement of the answer
# Your code here
print(type(cs1411FW.rules[0]))



# 4. More RDP attempts and now SMTP are being attacked to systems inside your network. 
# Adding individual rules for each source and destination is becoming 
# a laborious effort. Since you have the source code for the firewall
# you can add a way to accept wildcard rules like the following example:
# Rule {"id":1,"src":"*","dst":"*","port":"123","action":"Block"}
# Modify the firewall class method "findRuleMatch" to account for 
# wildcard source and destination addresses.
# After finishing your modification, add two rules below
# with the wildcards that will block SMTP and RDP ports.
# A successful solution will show 3 rules (1 from previous question, 2 from this one)
# Blocked: 201 
# Your code here
cs1411FW.addRule("*", "*", "3389", "Block")
cs1411FW.addRule("*", "*", "25", "Block")


#Uncomment lines below when ready to test your solution
# Optional: Verbose Mode, change the value of v to True or False to see traffic blocked.
simulateTraffic("4",cs1411FW)


# 5. Great Job! The firewall is working as intended but would be better to "pull" a list of 
# IP address and port numbers from another system that the Information Security team maintains.
# Use your knowledge with APIs to retrieve the list and parse out the information to block the
# traffic. Use this address for your API URL: https://faculty.ung.edu/lhundt/blockList.json
# Researching foreach loops with key/value pairs may be helpful here ;)
# A successful solution will show 4 rules (2 from previous questions, 2 from the API)
# Blocked: 327
r = requests.get("https://faculty.ung.edu/lhundt/blockList.json")
for rule in r.json()['firewallRules']:
    for ruleVal in rule.values(): #only here because each array object has its own name (Rule1 and Rule2)? I don't care about the name, only value. overcomplicated json tbh
        cs1411FW.addRule(ruleVal['srcIP'], ruleVal['dstIP'], ruleVal['port'], ruleVal['action'])


#Uncomment lines below when ready to test your solution
# Optional: Verbose Mode, change the value of v to True or False to see traffic blocked.
simulateTraffic("5",cs1411FW)