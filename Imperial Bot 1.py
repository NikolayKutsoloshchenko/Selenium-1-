#encoding=utf-8

import vk
from random import choice
import time

class Imperial():
    def __init__(self):
        Session = vk.Session(access_token='1c3e54d0678327e723d057cc5efd76e24f53184efcf882486e40a39f98a889082eec83886f75e4e62fd1f')
        self.bot= vk.API(Session)
        self.id = '363590949'
        self.get_faces()
        self.help_file= []
        self.get_help()
        self.cotsman_array = []
        self.kind_mail = {}

    def kind_mail_send(self,message):
        text = message['body']
        text = text.split('%')
        print(text)
        domain = text[1][1:]
        message_text = text[2]
        text_1 = u'Привет! Вас беспокоит Имперская почта. Вам письмо от анонима (ниже)'
        self.bot.messages.send(domain=domain, message=text_1)
        self.bot.messages.send(domain=domain, message=message_text)
        self.bot.messages.send(domain= domain, message=u'Я смогу переслать первое ваше сообщение анониму, жду вашего ответа.')
        self.send_to_chat(message, u'Отправленно')
        user = self.bot.users.get(user_ids = domain)
        if message['uid'] in self.kind_mail:
            self.kind_mail[message['uid']].append(user[0]['uid'])
        else:
            self.kind_mail[message['uid']] = [user[0]['uid']]

    def cotsman(self,message):
        if  not self.cotsman_array:
            file = open('.\\cotsman.txt', 'r', encoding='UTF-8')
            file_raw= file.read()
            file.close()
            self.cotsman_array = file_raw.split('\n')

        if choice(range(2)) == 0:
            self.send_to_chat(message, choice(self.cotsman_array))
        else:
            attachment = 'photo' + self.id + '_' + str(choice(self.cotsman_photo))
            self.send_to_chat(message, u'Коцман', attachment=attachment)

    def get_help(self,message=0):
            file = open('help', 'r', encoding='UTF-8')
            file = file.read()
            #file = file.split('\n')
            self.help_file = file

    def get_faces(self):
        photos_raw = self.bot.photos.get(album_id=239144351)
        cotsman_raw = self.bot.photos.get(album_id=239221597)
        self.cotsman_photo = []
        self.faces = []
        for photo in photos_raw:
            self.faces.append(photo['pid'])
        for photo in cotsman_raw:
            self.cotsman_photo.append(photo['pid'])

    def get_messages_unread_message(self):
        Income = self.bot.messages.get(time_offset=0)
        unread_messages = []
        for message in Income[1:]:
            if message['read_state'] == 0:
                unread_messages.append(message)
        return unread_messages

    def come_back(self,message):
        file = open('D:\\Telebot\\auto_kick', 'r')
        file_raw = file.read()
        file.close()
        IDs = file_raw.split(',')
        for id in IDs:
            id = id[:-1]

        Names = []
        for id in IDs:
            if id:
              name = self.bot.users.get(user_ids=int(id))
              Names.append(name)

        text = message['body'].split()
        text_1 = text[-1]
        text_1 = text_1[:-1]
        text_2 = text[-2]
        text_2 = text_2[:-1]
        for name in Names:
            print(text_1,text_2,name[0]['last_name'],name[0]['first_name'])
            if text_1 in name[0]['last_name'] and text_2 in name[0]['first_name']:
                self.bot.messages.removeChatUser(chat_id=message['chat_id'], user_id=name[0]['uid'])
                self.send_to_chat(message, u'Пошел вон, пёс')
                return
        name = message['body'].split()
        text = u'Дальше вы не пройдете пока не получити бумаги ' + name[-1] + ' ' + name[-2]
        self.send_to_chat(message, text)

    def kick(self,message):
        if message['body'][:5].lower() != u'кикни':
            self.send_to_chat(message,u'себе анус кикни, пёс')
            return
        file = open('D:\\Telebot\\kick', 'r')
        file_raw = file.read()
        file.close()
        temp_number = []
        strings = file_raw.split('\n')
        for number in range(len(strings)):
            temp_1 = strings[number]
            temp = strings[number].split(',')
            if temp[0] == message['body'][6:]:
                temp_number= number
                break
            temp= []

        if not temp:
            temp = []
            text= str(message['body'][6:]) + ','
            strings.append(text)
            temp_number = -1
            temp.append(text)
        print(strings)

        if str(message['uid']) in temp:
            self.send_to_chat(message, u'Вы уже голосовали за этого Васяна')
            return
        else:
            text = str(message['uid'])+ ','
            print(text)
            temp.append(text)

        if len(temp) >= 5:
            users = self.bot.messages.getChatUsers(chat_id=message['chat_id'], fields='screen_name')
            kick_id = 0
            for user in users:
                if user['screen_name'] in temp[0]:
                    kick_id = user['uid']
                    break
            if kick_id:
              self.bot.messages.removeChatUser(chat_id= message['chat_id'], user_id = kick_id)
              file = open('D:\\Telebot\\auto_kick', 'a')
              text = str(kick_id) + ','
              file.write(text)
              file.close()
            else:
                self.send_to_chat(message,u'Пользователь уже удаленно из беседы, балда')

        print(temp)

        string_out_of_temp = ''
        for i in temp:
            string_out_of_temp = string_out_of_temp + i

        if temp_number:
            strings[temp_number] = string_out_of_temp

        print(strings)
        file = open('D:\\Telebot\\kick', 'w')
        for string in strings:
            file.write(string + '\n')

        self.send_to_chat(message, text= u'Голос учтен')

    def search(self,unread_messages):
        print(self.kind_mail)
        for message in unread_messages:
            if message['uid'] == 179033736:
                self.cotsman(message)

            for user_pending in self.kind_mail:
                if message['uid'] in self.kind_mail[user_pending]:
                    time.sleep(1)
                    self.bot.messages.send(user_id=user_pending, message=u'Вот ответ', forward_messages= message['mid'])
                    time.sleep(1)
                    self.send_to_chat(message, u'Отправленно, спасибо что пользуетесь Имперской Почтой')
                    for number in range(len(self.kind_mail[user_pending])):
                        if self.kind_mail[user_pending][number] == message['uid']:
                            self.kind_mail[user_pending].pop(number)

            if 'chat_id' in message:
              if u'кикни' in message['body'].lower() and (message['chat_id'] == 6):
                self.kick(message)

            if u'покинул беседу' in message['body'].lower():
                self.send_to_chat(message, u'Если это существо прийдёт еще раз, я думаю Я НЕ БУДУ ВЫБИРАТЬ ВЫРАЖЕНИЯ')

            if u'вернулся в беседу' in message['body'].lower():
                self.send_to_chat(message, u'Мы следим за тобой, ничтожество')

            if u'пригласил' in message['body'].lower():
                if message['chat_id'] == 6:
                  self.come_back(message)
                else:
                    name = message['body'].split()
                    text = u'Дальше вы не пройдете пока не получити бумаги ' + name[-1] + ' ' + name[-2]
                    self.send_to_chat(message, text)


            if u'исключил' in message['body'].lower():
                self.send_to_chat(message, u'Так и нужно этому псу')

            if u'имперец' in message['body'].lower():
                if u'инфа' in message['body'].lower():
                    self.info(message)
                elif u'привет' in message['body'].lower():
                    self.send_to_chat(message, u'Под этим солнцем и небом мы тепло преветствует тебя!', reply=1)
                elif u'извинися' in message['body'].lower():
                    self.send_to_chat(message, u'Я прошу прощения за свои слова',reply=1)
                elif u'спасибо' in message['body'].lower():
                    self.send_to_chat(message, u'Ваша благодарность - высшая награда',reply=1)
                elif u'спокойной ночи' in message['body'].lower():
                    self.send_to_chat(message, u'Пускай АЛЬМСИВИ охраняют твой сон!',reply=1)
                elif u'доброе утро' in message['body'].lower():
                    self.send_to_chat(message, u'Доброе утро! Говорите свободно!',reply=1)
                elif u'мперец, лицо' in message['body'].lower():
                    attachment= 'photo'+self.id+'_'+str(choice(self.faces))
                    text = u'Твоё' + message['body'][8:]
                    self.send_to_chat(message, text, attachment=attachment)
                elif u'помощь' in message['body'].lower():
                    self.send_to_chat(message=message,text=self.help_file)
                elif u'комикс' in message['body'].lower():
                    self.send_to_chat(message,text=u'Смотри', attachment='nedroid.com/comics/2009-08-17-beartato-favor.gif')

            if u'добропочта%' in message['body'].lower():
                self.kind_mail_send(message)

            if u'или' in message['body'].lower():
                self.send_to_chat(message,text=choice(self.choose_or(message['body'])))

    def choose_or(self,text):
        temp=text.split()
        h = 0
        first = ''
        second = ''
        for i in temp:
            if i.lower() == u'или':
                h = 1
                continue
            if h == 0:
                first = first + ' ' + i
            else:
                second = second + ' ' + i
        temp = [first, second]
        return temp

    def send_to_chat(self,message,text,reply=0,attachment=0):
        if reply:
          if 'chat_id' in message:
            self.bot.messages.send(chat_id=message['chat_id'], message=text, forward_messages = message['mid'], attachment=attachment)
          else:
            self.bot.messages.send(user_id=message['uid'], message=text, forward_messages = message['mid'], attachment=attachment)
        else:
          if 'chat_id' in message:
            self.bot.messages.send(chat_id=message['chat_id'], message=text, attachment=attachment)
          else:
            self.bot.messages.send(user_id=message['uid'], message=text, attachment=attachment)

    def info(self,message):
        percent = u'Вероятность события = ' + str(choice(range(101))) + '%'
        self.send_to_chat(message,percent,reply=1)



if __name__ == '__main__':
  Reginald = Imperial()
  k= 1
  while k:
      time.sleep(1)
      Reginald.search(Reginald.get_messages_unread_message())
#      Reginald.bot.messages.markAsRead(peer_id=2000000006)