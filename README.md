### ☁️  Function as a Service (AWS Lambda Function)

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

Create your lmabda function in a file called `my_lambda.py` than run the compress to transform the function in `.zip` file.

```bash
    python3 compress.py
```

Create your lmabda function: 

```bash
    python3 create_lambda_function.py
```

See all lambda functions created with your account:

```bash
    python3 see_lambda_functions.py
```

Check if your funtion is returning what is expected:

```bash
    python3 check_lambda_function.py
```

Create your own API : 


```bash
     ________            _____________           __________
    |        |          |             |         |          |
    |  API   |   <--->  | API Gateway |  <--->  |  Lambda  |
    |________|          |_____________|         |__________|
```

```bash
    python3 create_api.py
```

Acesse the provider API and check if the API works. Is expected that you see the return of your lambda function.

Show API register in account:

```bash
    python3 show_apis.py
```

<br>
@2024, Insper. 9° Semester,  Computer Engineering.
_Machine Learning Ops & Interviews Discipline_