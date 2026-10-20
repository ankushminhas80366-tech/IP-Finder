# IP Address Resolver

A lightweight Python command-line utility that resolves website domain names into their corresponding IPv4 addresses. The script prompts the user to specify how many domains they want to look up, then sequentially requests URLs and returns their IP addresses.

## Features
* **Batch Resolution:** Specify the number of queries upfront to resolve multiple domains in a single session.
* **Standard Library Built-in:** Uses Python's native `socket` module, requiring no external dependencies or third-party installations.
* **Graceful Error Handling:** Includes a generic `try-except` block to catch and display errors without abruptly crashing the script (e.g., if an invalid domain is entered or the network is disconnected).

## Prerequisites
* Python 3.x

## Usage

1. Save the code into a file named `ip_resolver.py`.
2. Open your terminal or command prompt.
3. Run the script using the following command:

        python ip_resolver.py

4. Follow the on-screen prompts to enter the number of attempts and the target URLs.

### Example Interaction

        Enter the number of times to resolve the IP address: 2
        Attempt 1
        Enter Website (eg. www.example.com): www.google.com
        The IP address of www.google.com is: 142.250.190.36
        Attempt 2
        Enter Website (eg. www.example.com): www.github.com
        The IP address of www.github.com is: 140.82.113.3

## Error Handling
If you input a domain that does not exist or omit the standard domain format (e.g., typing `invalid-website` without a TLD), the `socket` module will raise a `socket.gaierror`. The script catches this and outputs the specific error message to the console before terminating.