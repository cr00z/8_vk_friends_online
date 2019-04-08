import vk


APP_ID = 6934498


def get_user_login():
    return input("User login: ")


def get_user_password():
    return input("User password: ")


def get_online_friends(login, password):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
        )
        api = vk.API(session, v='5.0')
        friends_all = api.friends.get(fields='online')
    except Exception:
        friends_online = None
    else:
        friends_online = []
        for friend in friends_all['items']:
            #if friend['online']:
                friend_info = '{} {}'.format(friend['last_name'], friend['first_name'])
                friends_online.append(friend_info)
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    if friends_online is None:
        exit('Vk API Error')
    output_friends_to_console(friends_online)
