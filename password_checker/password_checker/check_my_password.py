import sys

import requests  # needed to make an api request
import hashlib


# Make a request to api for the first 5 chars of our Hashed password and receive
# the api's list of compromised passwords starting with our first 5 chars
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res


# read api response
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())  # creates a tuple of (hash, count) for each line
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# Create hashed password and receive response
def pwned_api_check(password):
    # create hashed password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_char, tail = sha1password[:5], sha1password[5:]

    # make api req w. first 5 char of hashed password
    res = request_api_data(first_five_char)
    return get_password_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
