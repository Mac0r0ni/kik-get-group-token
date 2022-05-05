from kik_unofficial.datatypes.xmpp.roster import GroupSearchResponse
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.login import LoginResponse


 
username = ""
password = ""
 
 
class RegisterClient(KikClientCallback):
 
    def on_login_ended(self, response: LoginResponse):
        print("Logging In...")
 
    def on_authenticated(self):
        print("You are now logged in")
        id = client.search_group("activeandautistic")
        
    def on_group_search_response(self, response: GroupSearchResponse):
        print(response.groups)


if __name__ == '__main__':
    # logging.basicConfig(format=KikClient.log_format(), level=logging.DEBUG)
    client = KikClient(callback=RegisterClient(),
                       kik_username=username, kik_password=password)
while True: pass
