from dataclass.compress import CompressFile
from dataclass.lambda_function import LambdaFunction
from dataclass.gateway import Gateway
import time

# Variaveis
lambda_filename = "count.py"
lambda_compress = "countWords.zip"

lambda_function_name = "count_words2"  # Change Function Name in AWS Lambda
handler_function_name = "count_words"  # Funcion name in file hello.py
username = "leticiacb1"

input = {
    "sentence": "This is an example sentence to count words."
}

api_gateway_name = "api_countWords_leticiacb1"

handler = lambda_filename.split('.')[0] + "." + handler_function_name
function_name = lambda_function_name + "_" + username 

# Compress
compress = CompressFile()
compress.run(lambda_filename=lambda_filename, compress_filename=lambda_compress)

# Instantiate Lambda Function
deploy = LambdaFunction()
deploy.create_client()
deploy.read_function(compress_filename=lambda_compress)
deploy.create_function(function_handler= handler, function_name=function_name)

time.sleep(1) # Wait lambda function to be deployed

deploy.check_function(function_name=function_name, input = input)
deploy.see_all_lambda_functions()

# Create API for access lambda function
# gateway = Gateway()
# gateway.create_client()
# gateway.get_lambda_function(function_name=function_name)
# gateway.create_api(api_name= api_gateway_name, function_name=function_name)
# gateway.see_all_gateways()