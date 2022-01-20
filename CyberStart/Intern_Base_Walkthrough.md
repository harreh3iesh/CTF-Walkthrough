# Cyber Start Walkthrough Intern Camp

## L02 C04 
### ***Actual Problem Solving Goal***: 
    Tactical knowledge of being able to look through code to find what we want.

### ***Security Concept*** :
    Leaving plain text login information in functions

### Steps:
    
1. Right Click *Inspect Element* on **Sign In** button
2. Go to Console tab
3. Type ```this.email``` 
4. Type ```this.password```
    > ![L02 C04 - A](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%208.49.10%20AM.png) 

    *We know that these are functions in this code by seeing the preview of functions used in the code.
    ```this.``` refers to the owner of the object*
    > ![L02 C04 - B](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%208.56.31%20AM.png) 
5. Take output from steps 3 and 4 and login



## L03 C01

### ***Actual Problem Solving Goal***: 
    Figure out how to take the two Hexadecimal elements and combine them to find the passphrase

### ***Security Concept*** :
    Be able to calculate two binary values

> ![L03 C01 - A](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%209.11.42%20AM.png) 
1. We need to figure how what type of calculation needed. I know it is ```XOR``` because they give us a clue in the name <span style="color:red">*ROXy* </span>. This is ```XOR``` Backwards. This is like a key. 
   
2. We know that these are <span style="color:blue">*Hexadecimal* </span> values because they start with ``0x``

3. Solve -
   
    > ***Option A (Easy)***: Google *XOR Hexadecimal Calculator*

    > ***Option B (Let's code it!)***: Solve in Python -
    This code is in the file ```XOR.py``` and does not need any requirements to run other than Python3.
    
    ```python
    sz@Ss-MacBook-Pro / % python3 
    >>> a = 0xB105F00D 
    >>> b = 0xAAA8400A
    >>> bitwise_xor = a ^ b  # ^ is used for XOR binary
    >>> hex_string = hex(bitwise_xor) # Call built in hex() function
    >>> print(hex_string)
    0x1badb007 

    ```
5. The answer is ```0x1badb007``` as the flag


## L03 C02
### ***Actual Problem Solving Goal***: 
    Be able to watch how variables and functions change when code is executed

### ***Security Concept*** :
    Be able to manipulate poorly written code from the client side to alter the program's function


### Steps:
    
1. DON'T SPIN JUST YET! Right Click *Inspect Element* on **Spin for Question** button
2. Notice the ***default state*** and notice what ```action="/flashfast/answer"``` is set:
   > ![L03 C02 - A](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%209.58.13%20AM.png)
   
3. Click on the button to execute code and watch for how the state changes
    
    ***New State***:  

    >![L03 C02 - B](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%209.46.16%20AM.png) Notice how ```action=""``` is empty when there is a Locked Out status
4. If you keep clicking on Spin you will see it change over and over again once the conditional timer is up
5. After it is done spinning, go to the line where ```action=""``` >
    Right click ***'Edit HTML'*** and fill in: ```action="/flashfast/answer"```
    > ![L03 C02 - C](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2010.49.52%20AM.png)
6. Hit ```Command/Ctrl + Enter``` to save the edited HTML
7. Calculate the numbers on the calculator
8. The answer from the calculation is the flag
> ![L03 C02 - D](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2010.56.05%20AM.png)

***Note*** For some reason editing the HTML breaks in Firefox. I used Firefox for L03 - C03. Just use a different browser if you get a 404 error when editing this challenge's code. 


## L03 C03
### ***Actual Problem Solving Goal***: 
    Be able to 1. Fix errors by observing behavior (debugging) as well as be able to observe suspicious subtle changes in variables that throw alarms.

### ***Security Concept*** :
    Be able to manipulate API fields and redirect them to where you want them to go

***Note** I used FireFox to solve this problem. There is an advanced CURL method here as directed by the Hint, but that is beyond what I can do with POST requests. I took a graphical approach instead.  

1. Right Click on ***Balances*** tab on the iPhone  to inspect the element
2. Go to the ***Networking Tab*** and click on all of the tabs on the iPhone (Balances, Transactions, Payments) so that all of the API requests populate in the ***Networking Tab***. 
   
   Notice the ```404 error status code ```. This means the reason the ***Balances*** tab is not populating is because the API cannot find the server it is being directed to.
    >![L03 C03 - A](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2011.53.25%20AM.png)

    This makes sense when we go to the ***XHR*** tab and look and the ```JSON Response``` tab, the error is there. 

    > ![L03 C03 - B](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2011.59.04%20AM.png)
    ***[ ! ]*** XHR is short for XMLhttpRequest and allows websites to fetch data from a server and actively update a website without refresh. Thus, API. 

3. Go to any of the get-transactions or get-payments fields in the Network Tab and go to ```JSON Response``` again. This time it is filled out because the API worked and the ```200 status code``` was successful.

    ***[ ! ]*** Note the <span style="color:yellow">*Parent URL* </span> 
    
    Also see how each of the successful requests end with <span style="color:yellow">*cloudninebank.com/* </span> get-transactions.
    > ![L03 C03 - C](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2012.34.24%20PM.png)

4. Move across to the (A) ***Headers tab*** on the XHR request tab and on the (B) ***Resend*** dropdown select ***"Edit and Resend***
 > ![L03 C03 - D](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2012.41.34%20PM.png)

5. Delete everything up until the <span style="color:yellow">*Parent URL - cloudninebank.com/* </span> so we can request data from the previous domain level. Now hit ***Send***
 > ![L03 C03 - D](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%2012.41.51%20PM.png)

6. Now we have a new request that we can do the same same steps as in # 3. 
> ![L03 C03 - E](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%201.05.47%20PM.png)

The reason why get-balances was broken! It was the wrong URL. It's actually ***get-accounts***
    
> ![L03 C03 - F](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%201.06.16%20PM.png)

7. Now we repeat step 5 and this time we take the parent URL and add ***get-accounts*** to the <span style="color:yellow">*Parent URL - cloudninebank.com/get-accounts*  </span>  and resend the request again. 
> ![L03 C03 - G](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%203.03.44%20PM.png)

8. Now we go back to the ***get-accounts*** and ```JSON Response``` to find the flag

> ![L03 C03 - H](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%201.10.22%20PM.png)


## L03 C04
### ***Actual Problem Solving Goal***: 
    The timer changes to fast to concatenate the content from the different links by hand, therefore we have to write something that is quicker.

### ***Security Concept***:
    High level - be able to beat lock out timers and be faster than security controls as well as show that validation strings in URLs are insecure because it be manipulated.

All code is found in ```request_code.py``` 
Requirements to run: Python 3 and the Python module ```Requests``` is installed. 

1. For this we have to write code to get the data from the links. Each of the links has a part of the flag that needs to be pieced together and then fed into a different link to validate. 

```python 

import requests


# list all URLS - 

urls = ['https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D']

code = []
for url in urls: 
    r = requests.get(url)
    print(r.text)
    codeResponse = r.text
    code.append(codeResponse) #get all responses in a list


codeString = ''.join(code) # concat all responses from url into string 
validateUrl = f'https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string={codeString}' # dump into validation url 

validateResponse = requests.get(validateUrl) # kick off validation 
print(validateResponse.text) # get the code 

```

> ![L03 C04 - A](/SCREENSHOTS/Screen%20Shot%202022-01-19%20at%203.33.08%20PM.png)