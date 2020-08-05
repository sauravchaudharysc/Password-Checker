import requests
import hashlib
import sys

def request_api_data(query_char):
  #Api to get the hash and count
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  #if status code is 200 its working fine and 400 it's not working fine
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
 #split the response optained by api on the basis of hash and count i.e form a tuple
  hashes = (line.split(':') for line in hashes.text.splitlines())
  #iterate through the list of tuples and check for matching hash
  for h, count in hashes:
    if h == hash_to_check:
      #return it's count
      return count
  return 0

def pwned_api_check(password):
  #encode the password in sha1 format using inbuilt python module
  #hexdigest() returns a string object of double length consisting only hexadecimal digit
  #upper() to convert it into upper case
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  #extract first 5 characters, remaining character in tail
  first5_char, tail = sha1password[:5], sha1password[5:]
  #pass the first 5 character and get equivalent matching hashes and count of how many times password is hacked
  response = request_api_data(first5_char)
  #iterate to hash and get count of our password used
  return get_password_leaks_count(response, tail)

#accepts all the input in the command line as a list
def main(args):
#iterates through the list to check the password one by one
  for password in args:
    #Get the count of the password how many times it has been used or hacker
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

#run only if the main file runs not when imported
if __name__ == '__main__':
#[1:] to take multiple input at a time  
  sys.exit(main(sys.argv[1:]))

