import boto3

# 各サービスのリソースを取得する関数
def list_resources(region, service_name):
    session = boto3.Session(region_name=region)
    client = session.client(service_name)
    resource_list = []
    
    try:
        if service_name == 'ec2':
            ec2 = session.resource('ec2')
            instances = ec2.instances.all()
            for instance in instances:
                resource_list.append(f'EC2 Instance: {instance.id}')
        
        elif service_name == 's3':
            response = client.list_buckets()
            for bucket in response['Buckets']:
                resource_list.append(f'S3 Bucket: {bucket["Name"]}')
        
        # 他のサービスのリソースリストを追加
        # elif service_name == '...':
        
    except Exception as e:
        print(f'Error listing {service_name} resources in region {region}: {e}')
    
    return resource_list

# メイン関数
def list_all_resources():
    session = boto3.Session()
    regions = session.get_available_regions('ec2')
    services = ['ec2', 's3']  # リストするサービスをここに追加

    all_resources = {}

    for region in regions:
        all_resources[region] = {}
        for service in services:
            resources = list_resources(region, service)
            all_resources[region][service] = resources

    return all_resources

if __name__ == "__main__":
    all_resources = list_all_resources()
    for region, services in all_resources.items():
        print(f'Region: {region}')
        for service, resources in services.items():
            print(f'  Service: {service}')
            for resource in resources:
                print(f'    {resource}')
