from util import data_manager


def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    status = data_manager.execute_select(
        """
        SELECT * FROM statuses s
        WHERE s.id = %(status_id)s
        ;
        """
        , {"status_id": status_id})

    return status


def get_boards():
    """
    Gather all boards
    :return:
    """
    # remove this code once you implement the database
    # return [{"title": "board1", "id": 1}, {"title": "board2", "id": 2}]

    return data_manager.execute_select(
        """
        SELECT * FROM boards
        ;
        """
    )


def get_cards_for_board(board_id):
    # remove this code once you implement the database
    # return [{"title": "title1", "id": 1}, {"title": "board2", "id": 2}]

    matching_cards = data_manager.execute_select(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ;
        """
        , {"board_id": board_id})

    return matching_cards


def add_user(user_name,email,password,registration_time):
    data_manager.execute_insert( 
                """
                INSERT into 
                users (user_name, email, password, registration_time)
                values 
                (%(user_name)s, %(email)s, %(password)s, %(registration_time)s)"""
                , {'user_name': user_name, 'email': email, 'password':password,
                 'registration_time': registration_time})

def users_emails():
    users_emails = data_manager.execute_select(
        """
        SELECT email FROM users
        """)
    # print(users_emails)
    return users_emails

def user_data(email):
    user_data = data_manager.execute_select(
        """
        SELECT * FROM users
        WHERE email = %(email)s
        ;
        """
        , {"email": email}, fetchall=None)
    # print(user_data)
    # print(user_data['password'])
    return user_data

# user_data('piotr@piotr.pl')