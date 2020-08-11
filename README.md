# Password Checker

**Hackers uses something called dictionary attack and just tries to log into websites using this massive list information.**

​														In this project we will use the API provided by the website for us to check our password in secure way. **Troy Hunt** who’s a very famous security researches created this website [Know More](https://haveibeenpwned.com/About)

This site provide the breaches occurred . So if we type our password and check it will return the count how many times it has been hacked. But checking this on the website is risky even. Even though the website is https encrypted,we shouldn’t trust this for password we don’t want to send your password like this over the internet because what’s happening as soon as I click this is being transferred to some server somewhere in world. So we are going to use API for this.

## Password API 

- Install request module. $ pip install requests

  ​	Request module allows us to make request. It's kind of like having a browser without the actual browser. So, we can use our request module with the password API URL.

  #### **<u>How secure it is ??</u>**

  So this API uses something called hashing 

  So we will send the hash password. But let us think of case where the hacker by hit and trial gets the hashed code matched with the input. So this is also not that secure. So a better way for this is to use K-Anonymity.

  **What is K-Anonymity ??**

  A key concepts that was introduced to address the risk of reidentification of anonymized data through linkage to other datasets.

  For example :- 87% of **USA** population can be uniquely identified with just their 5 digit zip code,gender and date of birth taken together . It lead to a secure privacy breach for the individuals. Suppose we have two data medical data and voter list data. Suppose the medical list data hides the name and zipcode. But from voter list data and medical list data we can come to know about that person. This kind of attack is known as Re-Identification attack.

  So we use :- 

  1. Suppression

  2. Generalization

     <u>**This a modern technique that google,Netflix and amazon uses. K anonymity allows somebody to receive information about us still not know who we are.**</u>		

- Using K-Anonymity

  We only give the first 5 character of our hashed password. So this way API is never going to know our full hash and therefore never ever be able to guess our password.

  To check the password through API a hash version of password is required.

  **import hashlib** :- A built is module for hashing. So, with this we can do SHA1 hashing. 

         *Sha1password=hashlib.sha1(password.encode(‘utf-8’).hexdigest().upper()
          Hexdigest():- It returns a string object of double length, containing only hexadecimal digits.
          upper():-To convert it into upper case.

  <u>Hash Function</u>

  A function that simply generates a value of fixed length for each input that it gets

  Md5 Hash generator

     Type of hash function

  Others SHA-1,SHA-256 hash generator

  For a single input it gives a unique hash value. Change in one character changes the whole value. If I give same it’s going to give me the same result but I have no idea how to convert it back. This is called indempotent.

- To Send Password through API

  First Five character to API
     first5_char=sha1password[:5]

     Tail=sha1passsword[5:]

  Pass the first5_char to API and get all the response. So,this response returns the hashed password corresponding to the beginning of our hashed password. And we even get the count of the password.

**Demerit**

Even the password is safe online from breaches but as i am using the terminal it might get saved anywhere on my local computer drives. So to avoid this we can read the password from a text file.
