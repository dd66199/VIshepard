import datetime

from models import User


def get_user_by_id(user_id):
    try:
        return User().get(vk_id=user_id)
    except:
        User(
            vk_id=user_id,
            name='need_update',
            good=0,
            evil=0,
            clown=0
        ).save()
        return User().get(vk_id=user_id)
