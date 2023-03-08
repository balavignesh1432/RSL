import boto3
from datetime import datetime

client = boto3.client('cloudwatch')

# response = client.list_metrics(
#     Namespace='AWS/EC2',
#     MetricName='CPUUtilization',
#     Dimensions=[
#         {
#             'Name': 'InstanceId',
#             'Value': 'i-08b762b8da506ff0d'
#         },
#     ],
# )

# response = client.get_metric_statistics(
#     Namespace='AWS/EC2',
#     MetricName='CPUUtilization',
#     Dimensions=[
#         {
#             'Name': 'InstanceId',
#             'Value': 'i-08b762b8da506ff0d'
#         },
#     ],
#     StartTime=datetime(2023, 2, 10, 9),
#     EndTime=datetime(2023, 2, 10, 11),
#     Period=180,
#     Statistics=['Average'], 
#     # Unit='Percent'
# )


response = client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'utilisation',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/EC2',
                    'MetricName': 'CPUUtilization',
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': 'i-08b762b8da506ff0d'
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Average',
                'Unit': 'Kilobits/Second' 
            },
            # 'ReturnData': True,
        },
    ],
    StartTime='2023-02-10T10:00:00Z',
    EndTime='2023-02-12T22:00:00Z',
    MaxDatapoints=20,
    ScanBy='TimestampAscending'
)
# 'Unit': 'Count/Second'


# print(response)
respObject = response['MetricDataResults'][0]
print("CPU-Utilization (in Percent): ")
print("Timestamps\t\t\tPercentage Utilization")
for i in range(len(respObject['Timestamps'])):
    print(respObject['Timestamps'][i], ' : ', respObject['Values'][i])