# Cyber Start Walkthrough Intern Camp

## L02 C04 
### ***Actual Problem Solving Goal***: 
    Find the login information inside of the JavaScript code 

### ***Secuirty Concept*** :
    Leaving plain text login information in functions

### Steps:
    
1. Right Click *Inspect Element* on **Sign In** button
2. Go to Console tab
3. Type ```this.email``` 
4. Type ```this.password```
    > ![L02 C04 - A](./Screen%20Shot%202022-01-19%20at%208.49.10%20AM.png) 
    
    *We know that these are funcitons in this code by seeing the preview of functions used in the code.
    ```this.``` referes to the owener of the object*
    > ![L02 C04 - B](./Screen%20Shot%202022-01-19%20at%208.56.31%20AM.png) 
5. Take output from steps 3 and 4 and login



## L03 C01

### ***Actual Problem Solving Goal***: 
    Figure out how to take the two Hexadecimal elements and combine them to find the passphrase

### ***Secuirty Concept*** :
    Be able to calculate two binary values

> ![L03 C01 - A](./Screen%20Shot%202022-01-19%20at%209.11.42%20AM.png) 
1. We need to figure how what type of calculation needed. I know it is ```XOR``` because they give us a clue in the name <span style="color:red">*ROXy* </span>. This is ```XOR``` Backwards. This is like a key. 
   
2. We know that these are <span style="color:blue">*Hexadecimal* </span> values because they start with ``0x``

3. Solve -
    > ***Option A (Easy)***: Google *XOR Hexadecimal Calculator*

    > ***Option B (Will Get One Further in Life)***: Solve in Python
    ```python
    swz@Ss-MacBook-Pro / % python3 
    >>> a = 0xB105F00D 
    >>> b = 0xAAA8400A
    >>> bitwise_xor = a ^ b  # ^ is used for XOR binary
    >>> hex_string = hex(bitwise_xor) # Call built in hex() function
    >>> print(hex_string)
    0x1badb007 

    ```
4. The answer is ```0x1badb007``` as the flag


## L03 C02
### ***Actual Problem Solving Goal***: 
    Be able to watch how variables and functions change when code is executed

### ***Secuirty Concept*** :
    Be able to manipulate poorly written code from the client side to alter the program's function


### Steps:
    
1. DON'T SPIN JUST YET! Right Click *Inspect Element* on **Sping for Question** button
2. Notice the ***defualt state*** and notice what ```action="/flashfast/answer"``` is set:
   > ![L03 C02 - A](./Screen%20Shot%202022-01-19%20at%209.58.13%20AM.png)
   
3. Click on the button to execute code and watch for how the state changes
    
    ***New State***:  



    >![L03 C02 - B](./Screen%20Shot%202022-01-19%20at%209.46.16%20AM.png) Notice how ```action=""``` is empty when there is a Locked Out status
4. If you keep clicking on Spin you will see it change over and over again once the conditional timer is up
5. After it is done spinning, go to the line where ```action=""``` >
    Right click ***'Edit HTML'*** and fill in: ```action="/flashfast/answer"```
    > ![L03 C02 - C](./Screen%20Shot%202022-01-19%20at%2010.49.52%20AM.png)
6. Hit ```Command/Ctrl + Enter``` to save the edited HTML
7. Calculate the numbers on the calculator
8. The answer from the calculation is the flag
> ![L03 C02 - D](./Screen%20Shot%202022-01-19%20at%2010.56.05%20AM.png)

***Note*** for some reason editing the HTML breaks in FireFox, which is the next browswer we need for L03 - C03. Just use a different browswer if you get a 404 error


## L03 C03
### ***Actual Problem Solving Goal***: 
    Be able to identify and observe when values don't align and how direct the app where to go to solve the issue (basically debugging + API realted concepts)

### ***Secuirty Concept*** :
    Be able to manipulate API fields and redirect them to where you want them to go

***Note** I used FireFox to solve this problem. There is an advanced CURL method here, but I want to keep it simple.

1. Right Click on ***Balances*** tab on the iPhone  to inspect the element
2. Go to the ***Networking Tab*** and click on all of the tabs on the iPhone (Balances, Transactions, Payments) so that all of the API requests populate in the ***Networking Tab***. 
   
   Notice the ```404 error status code ```. This means the reason the ***Balances*** tab is not populating is because the API cannot find the server it is being directed to.
    >![L03 C03 - A](./Screen%20Shot%202022-01-19%20at%2011.53.25%20AM.png)

    This makes sense when we go to the ***XHR*** tab and look and the ```JSON Responce``` tab, the error is there. 

    > ![L03 C03 - B](./Screen%20Shot%202022-01-19%20at%2011.59.04%20AM.png)
    ***[ ! ]*** XHR is short for XMLhttpRequest and allows websites to fetch data from a server and actively update a website without refresh. Thus, API. 

3. Go to any of the get-transactions or get-payements fields in the Network Tab and go to ```JSON Responce``` again. This time it is filled out because the API worked and the ```200 status code``` was successful.

    ***[ ! ]*** Note the <span style="color:yellow">*Parent URL* </span> 
    
    Also see how each of the successful requests end with <span style="color:yellow">*cloudninebank.com/* </span> get-transactions.
    > ![L03 C03 - C](./Screen%20Shot%202022-01-19%20at%2012.34.24%20PM.png)

4. Move across to the (A) ***Headers tab*** on the XHR request tab and on the (B) ***Resend*** dropdown select ***"Edit and Resend***
 > ![L03 C03 - D](./Screen%20Shot%202022-01-19%20at%2012.41.34%20PM.png)

5. Delete everything up until the <span style="color:yellow">*Parent URL - cloudninebank.com/* </span> so we can request data from the previous domain level. Now hit ***Send***
 > ![L03 C03 - D](./Screen%20Shot%202022-01-19%20at%2012.41.51%20PM.png)

6. Now we have a new request that we can do the same same steps as in # 3. 
> ![L03 C03 - E](./Screen%20Shot%202022-01-19%20at%201.05.47%20PM.png)

The reason why get-balances was broken! It was the wrong URL. It's actually ***get-accounts***
    
> ![L03 C03 - F](./Screen%20Shot%202022-01-19%20at%201.06.16%20PM.png)

7. Now we repeat step 5 and this time we take the parent URL and add ***get-accounts*** to the <span style="color:yellow">*Parent URL - cloudninebank.com/get-accounts*  </span>  and resend the request again. 
> ![L03 C03 - G](./Screen%20Shot%202022-01-19%20at%203.03.44%20PM.png)

8. Now we go back to the ***get-accounts*** and ```JSON Responce``` to find the flag

> ![L03 C03 - H](./Screen%20Shot%202022-01-19%20at%201.10.22%20PM.png)


## L03 C04
### ***Actual Problem Solving Goal***: 
    The timer changes to fast to concatenate the different links by hand so we have to write something that is quicker.

### ***Secuirty Concept***:
    High level - be able to beat lock out timers and be faster than security controls as well as show that validation strings in URLs are insecure because it be manipulated.

All code is found in ```request_code.py``` 
Requirements to run: Python 3 and the Python moduel ```Requests``` is installed. 

1. For this we have to write code to get the data from the links. Each of the links has a part of the flag that needs to be pieced together and then fed into a differnt link to validate. 

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
    codeResponce = r.text
    code.append(codeResponce) #get all responces in a list


codeString = ''.join(code) # concat all responces from url into string 
validateUrl = f'https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string={codeString}' # dump into validation url 

validateResonce = requests.get(validateUrl) # kick off validation 
print(validateResonce.text) # get the code 

```

> ![L03 C04 - A](./Screen%20Shot%202022-01-19%20at%203.33.08%20PM.png)