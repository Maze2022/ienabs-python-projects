# 1) Create an empty AWS Services list
AWS_serv_list = [ ]

# 2) Populate the list with AWS services
AWS_serv_list.insert(0, "EC2")
AWS_serv_list.insert(1,"Lambda")
AWS_serv_list.insert(2, "Elastic Beanstalk")
AWS_serv_list.insert(3, "SQS")
AWS_serv_list.insert(4, "CloudTrail")
AWS_serv_list.insert(5, "DynamoDB")
AWS_serv_list.insert(6, "SNS")
AWS_serv_list.insert(7, "Lightsail")
AWS_serv_list.insert(8, "S3")

# 3) Print the list and length of the list
print(len(AWS_serv_list))


# 4) Remove two specific services from the list by name or by index
del AWS_serv_list [3]
del AWS_serv_list [7]





