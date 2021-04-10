def validity(domain, username):
    """ Function to check if Email is valid or not."""
    conditions = ("." in domain), (domain[0] != "."), (domain[-1] != "."), \
                 (username != ''), ("." not in username)

    if all(conditions):
        return True
    else:
        print("\033[1;31m[-] Invalid Email.")
        return False


def slicer(mail):
    """ Function to slice and return domain and username of the email. """
    domain = mail.split("@")[-1]
    ind = mail.find(domain)
    username = mail[:ind - 1]
    return domain, username


if __name__ == '__main__':
    print('\033[1;35m--------------------------- Email Slicer ---------------------------')
    while 1:
        email = input("\033[1;;m>>> Enter Email here (Quit to exit program): ").strip()
        if email.lower() in ("q","quit","exit"):
            quit()
        elif "@" not in email:
            print("\033[1;31m [-] Invalid Email.")
        else:
            domain, username = slicer(email)
            if validity(domain, username):
                print(f"\033[1;35m [+] Username :\033[1;34m {username}")
                print(f"\033[1;35m [+] Domain   :\033[1;34m {domain}")
