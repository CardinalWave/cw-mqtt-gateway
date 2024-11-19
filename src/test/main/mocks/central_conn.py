from src.domain.use_cases.central.central_conn import CentralConnInterface


class CentralConnSpy(CentralConnInterface):

    def request(self,  params: any, action: str) -> any:
        json_data = ""
        if action== "/user/login":
            json_data = {
                'payload': {
                    'token': 'session_id0000',
                    'email': 'lua@email.com',
                    'username': 'example_user'
                }
            }

        elif action== "/user/register":
            json_data = {
                'payload': {
                    'token': 'session_id0000',
                    'email': 'lua@email.com',
                    'username': 'example_user'
                }
            }
        elif action== "/group/list":
            json_data = {
                'payload': [
                    {
                        'title': 'Admin Group',
                        'group_id': "1"
                    },
                    {
                        'title': 'Users Group',
                        'group_id': "2"
                    },
                    {
                        'title': 'Guests Group',
                        'group_id': "3"
                    }
                ]
            }
        elif action== "/group/create":
            json_data = {
                'payload':
                    {
                        'title': 'Admin Group',
                        'group_id': "1"
                    }
            }
        elif action== "/group/join":
            json_data = {
                'payload':
                    {
                        'group_title': 'Admin Group',
                        'group_id': "1"
                    }
            }
        elif action== "/chat/join":
            json_data = {}
        elif action== "/chat/join":
            json_data = {}
        return json_data
