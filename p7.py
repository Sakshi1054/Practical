def calculate_power(x, y, P):
    # Function to calculate (x^y) % P
    if y == 1:
        return x
    else:
        return pow(x, y, P)  # Using Python's built-in pow() with three arguments for modular exponentiation

def main():
    # Input for public keys and private keys
    print("Both the users should be agreed upon the public keys G and P")

    G = int(input("Enter value for public key G: "))
    P = int(input("Enter value for public key P: "))

    a = int(input("Enter value for private key a selected by user1: "))
    b = int(input("Enter value for private key b selected by user2: "))

    # Calculating the values for both users
    x = calculate_power(G, a, P)
    y = calculate_power(G, b, P)

    # Calculating the secret keys
    ka = calculate_power(y, a, P)
    kb = calculate_power(x, b, P)

    # Output the secret keys
    print(f"Secret key for User1 is: {ka}")
    print(f"Secret key for User2 is: {kb}")

if __name__ == "__main__":
    main()