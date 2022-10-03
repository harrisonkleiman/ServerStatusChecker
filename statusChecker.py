# Initiate socket
import socket

# Check if the server is up
def server_running(website):
    try:
        socket.gethostbyname(website) # Get IP address
        return True 
    except socket.error: # If the server is down
        return False 
    
if __name__ == "__main__":
    while True:
        website = input("Enter the website (use '.com' at the end): ")
        if server_running(website):
            print(f"{website} is up!")
        else:
            print(f"{website} is down!")
        
        # Ask if the user wants to check another website
        check_again = input("Do you want to check another website? (y/n): ")
        if check_again.lower() == "n":
            break
        
    print("Thank you for using this program!")
    
     

    
