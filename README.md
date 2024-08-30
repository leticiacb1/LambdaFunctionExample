### ☁️  Function as a Service (AWS Lambda Function)

**Function as a Service (FaaS)** refers to a cloud computing model that allows developers to build and run applications and functions without having to worry about infrastructure management.

With FaaS, we are able to deploy their code in the form of stateless functions or event handlers that can be invoked on-demand or in response to events.

Every time there is a call to the API endpoint, whether through the browser or an application, the Lambda function will be triggered.

This will be the schematic drawing:

```bash
     ________            _____________           __________
    |        |          |             |         |          |
    |  API   |   <--->  | API Gateway |  <--->  |  Lambda  |
    |________|          |_____________|         |__________|
```

#### Run the project

Create a `venv` and install dependencies:

```bash
    # Create environment
    python3 -m venv venv  

    # Activate environment
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
``` 

Create a `.env` file inside `config/` folder with user and password of RabbitMQ:

```bash
    # .env content'
    AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXX"
    AWS_SECRET_ACCESS_KEY="aaaaaaaaaaaaaaaaaaaaaaaaaaa"
    AWS_REGION="xx-xxxx-2"
    AWS_LAMBDA_ROLE_ARN="arn:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
``` 

For run the code example that only return a "Hello World" message : 

```bash
    # The lambda function is in hello.py file
    python3 hello_world.py
``` 

For run the code example that recived a sentence as input and return the number of words in the sentence : 

```bash
    # The lambda function is in count.py file
    python3 count_words.py
``` 

⚠️ It is possible that running the code more than once will report an error because the lambda function with that name has already been created. If this happens, change the code variable responsible for the function name (`lambda_function_name`) .

```bash
    # Error example:
    raise error_class(parsed_response, operation_name)
    botocore.errorfactory.ResourceConflictException: An error occurred (ResourceConflictException) 
    when calling the CreateFunction operation: Function already exist: say_hello3_leticiacb1
```

```python 
   # ---- Omitted Code ----

    lambda_filename = # Filename that contain the lambda function that will be deployed
    lambda_compress = # Name of filename that contain the zipped lambda function

    lambda_function_name =  # Lambda Function Name in AWS Lambda
    handler_function_name = # Funcion name that will be deplyed
    username = # Username of the account (Optional value)

    api_gateway_name = # Api name

    # ---- Omitted Code ----
``` 

<br>
@2024, Insper. 9° Semester,  Computer Engineering.
<br>

_Machine Learning Ops & Interviews Discipline_