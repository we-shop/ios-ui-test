import boto3
import pprint
import re
import requests
import os
import glob
import json


pp = pprint.PrettyPrinter(indent=4)

########################################
# get apps from s3 bucket
########################################
# Local credentials
# ACCESS_KEY = "xtest"
# SECRET_KEY = "xtest"
# SESSION_TOKEN = "xtest"

# AWS credentials
# ACCESS_KEY = os.getenv("ACCESS_KEY_ID")
# SECRET_KEY = os.getenv("SECRET_ACCESS_KEY")
# SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
# REGION = os.getenv("AWS_REGION")

# BS credentials
# BS_USERNAME = os.getenv("BS_USERNAME")
# BS_ACCESS_KEY = os.getenv("BS_ACCESS_KEY")

# BS CREDENTIALS
BS_LOGIN = os.getenv("BS_LOGIN")
BS_SECRET = os.getenv("BS_SECRET")

# CREDS
credentials = boto3.Session().get_credentials()

ACCESS_KEY = credentials.access_key
SECRET_KEY = credentials.secret_key
SESSION_TOKEN = credentials.token

session = boto3.Session( 
		 aws_access_key_id=ACCESS_KEY, 
		 aws_secret_access_key=SECRET_KEY,
		 aws_session_token=SESSION_TOKEN)

client = boto3.client(
	's3',
	aws_access_key_id=ACCESS_KEY,
	aws_secret_access_key=SECRET_KEY,
	aws_session_token=SESSION_TOKEN
)


#######################
# generate Json (final action)
#######################
def generate_json(bucket_tags):
	app_link = []

	for i in bucket_tags:
		if "bs_link" in i.get("Key"):
			app_link.append(i.get("Value"))

	desired_cap = {
	  "device" : "iPhone 11",
	  "os_version" : "15",
	  "project" : "iOS Weshop", 
	  "build" : "browserstack-iOS",
	  "name" : "iOS test",
	  "app_url": app_link[0]
	}


	with open(os.getcwd() + '/ios_caps.json', 'w', encoding='utf-8') as f:
		json.dump(desired_cap, f, ensure_ascii=False, indent=4)

	print("Successfully updated ios_caps.json caps!")

# Filter all iOS apps and get latest file path and app id
def ios_get_app_path():
	ios_lst = []

	s3 = session.resource('s3')
	response_ios = s3.Bucket('ss-travis-ci').objects.filter(Prefix='we-shop/iOS/')

	for i in response_ios:
		if i.key.startswith("we-shop/iOS/") and i.key.endswith("/WeShop.ipa"):
			if "build" not in i.key:
				ios_lst.append(i.key)


	#get_direct = [i.key for i in s3.Bucket('ss-travis-ci').objects.filter(Prefix=sorted(ios_lst)[-1])][0] # debug

	# get direct ios path, looks like this "we-shop/iOS/9143/WeShop.ipa"
	get_direct_path_ios = sorted(ios_lst)[-1]

	# get build id, looks like this "9143"
	getting_id_of_ios_build = re.findall("\\d+", get_direct_path_ios)[0]

	return get_direct_path_ios, getting_id_of_ios_build


LATEST_APP_PATH_AND_ID = ios_get_app_path()

# get tags of file
def get_tag_of_certain_file(path_app_id):
	response = client.get_object_tagging(
		Bucket='ss-travis-ci',
		Key=f"we-shop/iOS/{path_app_id}/WeShop.ipa", #file_path
	)

	return response['TagSet']

# download certain (according to passed argument) file 
def download_ios_app(path_to_file):
	# re-name downloaded file
	new_name = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')

# get whole list of downloaded (locally) files
def get_whole_scope_of_files():
	#print(glob.glob(os.getcwd() + "/*.ipa")[0])
	return str(glob.glob(os.getcwd() + "/*.ipa"))

# getting latest local (downloaded) file
def get_latest_file(all_files):
	#downloading latest build
	#download_ios_app(ios_get_app_path())

	all_nums = max(re.findall("\\d+", all_files))

	#print(glob.glob(os.getcwd() + "/*.ipa")[0]) # debug
	#return str(glob.glob(os.getcwd() + "/*.ipa")) # debug

	for i in glob.glob(os.getcwd() + "/*.ipa"):
		if all_nums in i:
			return i
	else:
		print(f"{SOMETHING_WRONG_WITH_FILE_NAME}")


# uploading downloaded latest app file
def upload_app_to_BS():
	LATEST_FILE_IOS = get_latest_file(get_whole_scope_of_files())

	files = {'file': (LATEST_FILE_IOS, open(LATEST_FILE_IOS, 'rb'))}
	response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', 
				files=files, 
				auth=(BS_LOGIN, BS_SECRET))


	return json.loads(response.text)["app_url"]


def check_ios_app_tags(path_to_file, tag_set):
	# re-name downloaded file
	app_id_build = re.findall("\\d+", path_to_file)[0]

	# download file to current folder
	# doc https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
	#client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')


	if len(tag_set) == 0:
		print("Download started!")
		# download app file
		download_ios_app(path_to_file)
		uploaded_bs_file_data = upload_app_to_BS()


		# update tags	
		response = client.put_object_tagging(
		Bucket="ss-travis-ci",
		Key=f"we-shop/iOS/{app_id_build}/WeShop.ipa", #file_path
		Tagging={
		'TagSet': [
			{
				'Key': 'ios_build_id',
				'Value': app_id_build,
			},
			{
				'Key': 'bs_link',
				'Value': uploaded_bs_file_data,
			},
		  ],
		 } 
	    )

		return [{'Key': 'bs_link', 'Value': uploaded_bs_file_data}, {'Key': 'ios_build_id', 'Value': app_id_build}]

	else:
		print("Not needed")
		return get_tag_of_certain_file(app_id_build)


generate_json(check_ios_app_tags(LATEST_APP_PATH_AND_ID[0], get_tag_of_certain_file(LATEST_APP_PATH_AND_ID[1])))

# debug block, can be removed
# json_f = open(os.getcwd() + "/ios_caps.json")
# #json_f = open('ios_caps.json') # local
# desired_cap = json.load(json_f)
# json_f.close()

# print(desired_cap)

#################################
# DEBUG Just download latest app
#################################
# def only_download_ios_app(path_to_file):
# 	# re-name downloaded file
# 	new_name = re.findall("\\d+", path_to_file)[0]

# 	# download file to current folder
# 	client.download_file('ss-travis-ci', path_to_file, f'WeShop{new_name}.ipa') #'WeShop.ipa')
# 	print(f"iOS app downloaded, version: {new_name}")

#print(LATEST_APP_PATH_AND_ID) # output format ('we-shop/iOS/9287/WeShop.ipa', '9287')
#only_download_ios_app(LATEST_APP_PATH_AND_ID[0])
#only_download_ios_app("we-shop/iOS/9328/WeShop.ipa")