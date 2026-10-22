import socket  # Built-in module for network-related operations (no external packages needed)

try:
    # Ask the user how many domain-to-IP lookups they want to perform
    times = int(input("Enter the number of times to resolve the IP address: "))
    attempt = 1  # Counter to display which attempt is currently running

    # Loop until the requested number of lookups is completed
    while times > 0:
        print("Attempt", attempt)

        # Get the website/domain name from the user
        url = input("Enter Website (eg. www.example.com): ")

        # Resolve the domain name to its IPv4 address using DNS lookup
        ip = socket.gethostbyname(url)

        # Display the result
        print("The IP address of", url, "is:", ip)

        # Decrease remaining lookups and increase attempt counter
        times -= 1
        attempt += 1

except Exception as e:
    # Catch any error (invalid domain, network issue, non-integer input, etc.)
    # and print a friendly message instead of crashing
    print("Error:", e)
