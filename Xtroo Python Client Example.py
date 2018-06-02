# Import the required libraries
import urllib.request
import json

def GetContent(url):
    # Build our request and add our API key into the header.
    request = urllib.request.build_opener()
    # Replace your_api_key with the API key found under your Account Management page.
    request.addheaders = [('api','your_api_key')]
    # Send our request to the API along with our argument.
    response = request.open('https://xtroo.io/api/content?url=' + url)
    # Convert the response into a string, then encode that into usable JSON.
    strResponse = response.read().decode("UTF-8");
    # print(strResponse)
    jsonResponse = json.loads(strResponse)
    # Return the encoded JSON.
    return jsonResponse

# Call the GetContent function, pass in the web page you wish to run extraction on here.
jsonResult = GetContent("http://www.webpage-to-extract.co.uk/");

# Call each section of the returned JSON and print it. 
print("Title" + jsonResult['title'])
print("Text" + jsonResult['text'])
print("HTML" + jsonResult['html'])
# As both Links and Images are arrays, we need to print them slightly differently. We print the header, then
# Print each item in the list, seperated by a newline.
print("Links")
print(jsonResult['links'], sep='\n')
print("Images")
print(jsonResult['images'], sep='\n')

