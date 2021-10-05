#!/usr/bin/env python3`


def main():
                # grab a string.... then ensure it is all lowercase
    hostname = input("What is the hostname? ").lower() 

    # test logic with the `if` statement
    # what to do if this statement is found to be true
    if hostname == "mtg":
        print("The hostname was found to be mtg")
    elif hostname == "qfg":
        print("The hostname was found to be qfg")
    elif hostname == "sq":
        print("the hostname was found to be sq")
    else:
        print("I am unaware of that hostname.")


    # grab string data, and normalize it (make it all lowercase for testing purposes)
    hostname = input("Try this again, what is the hostname? ").lower()
    new_hosts = ["demeter", "zeus", "hera", "posedion", "iris"]

    if hostname in new_hosts:
        print(f"The hostname was found to be {hostname}")
        #print("The hostname was found to be" + hostname)
    else:
        print("I am unaware of that hostname.")



# ensures others can import our code correctly
# this conditional is ONLY true IF someone runs the script directly
# it is NOT true when others IMPORT our code
if __name__ == "__main__":
    main()
