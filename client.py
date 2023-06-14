import requests
import dotenv
import os
import keyring
import jwt
import time

from PySide2.QtGui import QPixmap
from PySide2.QtCore import QSize, Qt

dotenv.load_dotenv()

class APIClient:
    def __init__(self):
        self.URL = os.getenv('URL')
        self.SERVICE_NAME = "ikarma"
        self.USERNAME = "access-token"
        
    ##########################################################################
    ## Get Access Token "Authorization": "Bearer" Format
    #########################################################################
    def ACCESS_TOKEN(self):
        access_token = keyring.get_password(self.SERVICE_NAME, self.USERNAME)
        print("#################", access_token)
        # if access_token:
        #     # try:
        #     # Decode the access token to get the expiration time
        #     token_payload = jwt.decode(access_token,"9f7e8d3a19d4a13532b569264ac29830eab9dfa8f4d46990fe3e4343ab93", algorithms=["HS256"], verify=False)
        #     exp = token_payload.get('exp')
        #     print('#################Here not access token########################')
        #     print(exp)
        #     # Check if the token has expired
        #     if exp and exp < time.time():
        #         # Delete the keyring password if the token has expired
        #         keyring.delete_password(self.SERVICE_NAME, self.USERNAME)
        #         access_token = None
        #     # except jwt.exceptions.InvalidTokenError:
        #     #     # If the access token is invalid, delete the keyring password
        #     #     keyring.delete_password(self.SERVICE_NAME, self.USERNAME)
        #     #     access_token = None
        return {"Authorization": f"Bearer {access_token}"}

    def login(self, username, password):
        response = requests.post(f'{self.URL}/login', data={"username": username, "password": password})
        response.raise_for_status()
        access_token = response.json()['access_token']
        keyring.set_password(self.SERVICE_NAME, self.USERNAME, access_token)



    def get_current_user(self):
        response = requests.get(f'{self.URL}/users/me/', headers=self.ACCESS_TOKEN())
        response.raise_for_status()
        return response.json()

    def add_user(self, data):
        response = requests.post(f'{self.URL}/add_user', json=data)
        response.raise_for_status()
        return response.json()
    
    def delete_user(self):
        response = requests.delete(f'{self.URL}/users/', headers=self.ACCESS_TOKEN())
        response.raise_for_status()

    
    def patch_user_data(self, data):
        response = requests.patch(f'{self.URL}/users/',headers= self.ACCESS_TOKEN(), json=data)
        response.raise_for_status()
        return response.json()
    
    def update_avatar(self, files):
        response = requests.put(f'{self.URL}/users/avatar/', headers= self.ACCESS_TOKEN(), files=files)
        response.raise_for_status()
        return response.content
    

    def get_user_avatar(self, user_id):
        response = requests.get(f"{self.URL}/users/avatar/{user_id}")
        if response.status_code == 200:
            return response.content
        else:
            return None

    def get_user_posts(self):
        response = requests.get(f'{self.URL}/user/posts/', headers=self.ACCESS_TOKEN())
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def get_all_posts(self):
        response = requests.get(f'{self.URL}/posts')
        response.raise_for_status()
        return response.json()

    
    def upload_video_file(self, title, description, files):
        data = {
                "title": title, 
                "description": description
            }
        response = requests.post(f'{self.URL}/posts', headers= self.ACCESS_TOKEN(), data=data, files = files)
        response.raise_for_status()


    def get_thumbnail(self, title, width, height):
           
            response = requests.get(f'{self.URL}/posts/thumbnail/{title}', stream=True)
            if response.status_code == 200:
                pixmap = QPixmap()
                
                pixmap.loadFromData(response.content)
                dim = QSize(width, height)
                
                scaled_pix= pixmap.scaled(dim, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                print("Store Thumbnail to Local Repo")
                scaled_pix.save(f"images/thumbnail/{title}{width}x{height}.png") 
                return scaled_pix
            else:
                print("Error Request !!")   

    def get_video_data(self, title):
        # Make the GET request to retrieve the video data
        response = requests.get(f'{self.URL}/posts/video/{title}', stream=True)
        video_path = f'videos/{title}.mp4'
        if response.status_code == 200:
            with open(video_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
        else:
            print(f"Request failed with status code {response.status_code}")


    
       
    def patch_post(self, id, data):
        response = requests.patch(f'{self.URL}/post/{id}', json=data)
        response.raise_for_status()
        return response.json()
    
    def delete_post(self, id):
        response = requests.delete(f'{self.URL}/posts/{id}', headers= self.ACCESS_TOKEN())
        response.raise_for_status()
        return response.text