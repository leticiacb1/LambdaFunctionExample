import boto3
import random
import string

from config.config import Config

class Gateway():
    
    def __init__(self):
        self.lambda_target = None
        self.lambda_function = None
        self.api_gateway = None
        self.id_num = "".join(random.choices(string.digits, k=7))

        self.protocol_type = "HTTP"
        self.version = "1.0"

        # Load environment variables
        self.config = Config()
        self.config.load()

    def create_client(self) -> None:
        self.api_gateway = boto3.client( "apigatewayv2",
                                         aws_access_key_id=self.config.ACCESS_KEY,
                                         aws_secret_access_key=self.config.SECRET_KEY,
                                         region_name=self.config.REGION
                                       )
        print("\n    [INFO] Create AWS API Gateway client. \n")

    def get_lambda_function(self, function_name: str) -> None:
        
        lambda_client = boto3.client( "lambda",
                                      aws_access_key_id=self.config.ACCESS_KEY,
                                      aws_secret_access_key=self.config.SECRET_KEY,
                                      region_name=self.config.REGION
                                    )

        self.lambda_function= lambda_client.get_function(FunctionName=function_name)
        self.lambda_target= self.lambda_function["Configuration"]["FunctionArn"]

        print("\n    [INFO] Get lambda function. \n")
        print(self.lambda_function)

    def create_api(self, api_name : str, function_name: str) -> None:
        print(f"\n    [INFO] Create API with name {api_name} \n")
        api_gateway_create = self.api_gateway.create_api( Name=api_name,
                                                          ProtocolType=self.protocol_type,
                                                          Version=self.version,
                                                          RouteKey="ANY /", # Here you can change to GET POST and provide route like "GET /hello"
                                                          Target=self.lambda_target,
        )


        print(f"\n    [INFO] Set lambda function permissions for API.\n")
        lambda_client = boto3.client( "lambda",
                                      aws_access_key_id=self.config.ACCESS_KEY,
                                      aws_secret_access_key=self.config.SECRET_KEY,
                                      region_name=self.config.REGION
                                    )
        
        api_gateway_permissions = lambda_client.add_permission( FunctionName=function_name,
                                                                       StatementId="api-gateway-permission-statement-" + self.id_num,
                                                                       Action="lambda:InvokeFunction",
                                                                       Principal="apigateway.amazonaws.com",
                                                                     )
        print(f'\n    [INFO] Check API Endpoint : {api_gateway_create["ApiEndpoint"]} \n')

    def see_all_gateways(self):
        response = self.api_gateway.get_apis(MaxResults="2000")

        print(f"\n    [INFO] See all apis associated to the account id \n")
        print(f"\n           > APIs : ")
        for api in response["Items"]:
            print(f"             - {api['Name']} ({api['ApiEndpoint']})")
