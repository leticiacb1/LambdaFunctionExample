import boto3
import io

from config.config import Config

class LambdaFunction():
    def __init__(self):
        self.lambda_client  = None
        self.content_to_deploy = None

        self.runtime = "python3.9"

        # Load environment variables
        self.config = Config()
        self.config.load()

    def create_client(self) -> None:
        self.lambda_client = boto3.client( "lambda",
                                            aws_access_key_id=self.config.ACCESS_KEY,
                                            aws_secret_access_key=self.config.SECRET_KEY,
                                            region_name=self.config.REGION
                                        )
        print("\n    [INFO] Create AWS lambda client. \n")

    def read_function(self, compress_filename: str) -> None:
        
        with open(compress_filename, "rb") as f:
            self.content_to_deploy = f.read()

        print("\n    [INFO] Read Content that will be deployed. \n")
        print(self.content_to_deploy )

    def create_function(self, function_handler: str, function_name: str) -> None:
        lambda_response = self.lambda_client.create_function( FunctionName=function_name,
                                                              Runtime=self.runtime,
                                                              Role=self.config.ROLE_ARN,
                                                              Handler=function_handler, 
                                                              Code={"ZipFile": self.content_to_deploy},
                                                            )

        print("\n    [INFO] Function ARN Response: \n")
        print("\n           > " + lambda_response["FunctionArn"])

    def check_function(self, function_name: str):

        try:
            response = self.lambda_client.invoke( FunctionName=function_name,
                                                  InvocationType="RequestResponse",
                                                )
                                                
            payload = response["Payload"]

            txt = io.BytesIO(payload.read()).read().decode("utf-8")

            print(f"\n    [INFO] Invoke Function {function_name}() \n")
            print("\n           > Response :" + txt)

        except Exception as e:

            print(f"\n    [ERROR] Invoke Function {function_name}() \n")
            print(e)

    def see_all_lambda_functions(self):
        response = self.lambda_client.list_functions(MaxItems=1000)
        functions = response["Functions"]

        print(f"\n    [INFO] See all lambda functions associated to the account id \n")
        print(f"\n           > You have {len(functions)} Lambda functions")
        print(f"\n           > Functions names:")

        for function in functions:
            function_name = function["FunctionName"]
            print(f"           {function_name}")