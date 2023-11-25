import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import utils
from models import User
from config import *
import shepard


class MyLongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print(e)


class VkBot:

    def __init__(self):
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = MyLongPoll(self.vk_session, 223593064)

    def run(self):
        for event in self.longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                msg = event.object.message
                user_id = msg['from_id']
                user = utils.get_user_by_id(user_id=user_id)
                text = msg['text']

                fwd = self.vk_session.method('messages.getByConversationMessageId',
                                             {'conversation_message_ids': msg['conversation_message_id'],
                                              'peer_id': msg['peer_id']
                                              })['items'][0]

                if "test shepard" in text:
                    self.vk_session.method('messages.send', {
                        'chat_id': msg['peer_id'] - 2000000000,
                        'message': "ВИ Шепард на связи",
                        'random_id': 0
                    })

                if 'reply_message' in fwd:
                    fwd = fwd['reply_message']
                else:
                    fwd = None
                    continue

                fwd_user = utils.get_user_by_id(fwd['from_id'])
                if fwd_user.name == 'need_update':
                    fwd_user.name = self.vk_session.method('users.get', {
                                    'user_id': fwd_user.vk_id,
                                    })[0]['first_name']

                receiving = shepard.receive_message(msg, fwd_user)
                if receiving == 'received':
                    print(receiving)
                else:
                    try:
                        self.vk_session.method('messages.send', {
                            'chat_id': msg['peer_id'] - 2000000000,
                            'message': receiving,
                            'random_id': 0
                        })
                    except:

                        print(msg)
                        print(fwd_user)


if __name__ == '__main__':
    VkBot().run()


