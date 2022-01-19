import requests


# list all URLS - 

urls = ['https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D',
'https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D']



print(urls)
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