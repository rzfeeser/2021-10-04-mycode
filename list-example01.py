#!/usr/bin/python3
"""Alta3 Research | Zach Feeser
   List - An example of working with python lists"""


# define our main function (run time code goes here)
def main():

    # create a list to contain IPs to ban
    ban = []  # create an empty list
    # ban = list() # does the same thing as the line above

    # add an IP address to our list
    ban.append("172.16.8.2") # adds a SINGLE VALUE to the end of our list
    
    # add a second IP address to our list
    ban.append("10.8.3.22")

    # create a second list of host names to ban
    ban_hosts = ["acme.example.org", "smith.example.org", "*.example.com"]

    # combine both lists into a single list
    # ban = ban + ban_hosts
    # all_ban = ban + ban_hosts
    
    #ban.extend(ban_hosts)   # extend is the way to combine both lists via ITERATION
    #["172.16.8.2", "10.8.3.22", "acme.example.org", "smith.example.org", "*.example.com"]

    #ban.append(ban_hosts)
    #["172.16.8.2", "10.8.3.22", ["acme.example.org", "smith.example.org", "*.example.com"]]

    # display our list to the screen
    print(ban)

main()

