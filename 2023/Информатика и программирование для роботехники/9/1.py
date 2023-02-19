from time import time, ctime

class Server:
    def __init__(self):
        self.records = list()
    
    def add(self, from_id, to_id, msg, status):
        self.records.append({
            'from_id': from_id,
            'to_id': to_id,
            'msg': msg,
            'time': ctime(time()),
            'status': status
        })

    def all(self):
        for x in self.records:
            print(x)

    def head_10(self):
        for i in range(min(len(self.records), 10)):
            print(self.records[i])
    
    def foot_10(self):
        for i in range(max(len(self.records) - 11, 0), len(self.records)):
            print(self.records[i])
    
    def lost_message(self):
        for x in self.records:
            if x['status'] == False:
                print(x)
    
    def ok_message(self):
        for x in self.records:
            if x['status'] == True:
                print(x)

    def messages_by_user(self, user_id):
        messages = []
        for x in self.records:
            if x['from_id'] == user_id:
                messages.append(x)
        return messages

    def message_by_user(self, user_id):
        messages = self.messages_by_user(user_id)
        for x in messages:
            print(x)

    def statistic(self):
        users = set()
        msgs = ok_msgs = lost_msgs = 0
        for x in self.records:
            users.add(x['from_id'])
            msgs += 1
            if x['status'] == True:
                ok_msgs += 1
            else:
                lost_msgs += 1
        print(len(users), msgs, ok_msgs, lost_msgs)

class User:
    def __init__(self, user_id, username, status):
        self.id = user_id
        self.username = username
        self.status = status

    def info(self, server):
        print(self.id, self.username, len(server.messages_by_user(self.id)))

    def send_message(self, user_id_to_message, content_of_message, user_to, server):
        server.add(self.id, user_id_to_message, content_of_message, user_to.status)

class Admin(User):
    def remove(self, user_id, server):
        i = 0
        while i < len(server.records):
            if server.records[i]['from_id'] == user_id:
                server.records.pop(i)
                i -= 1
            i += 1
    
    def clear(self, server):
        server.records.clear()


server = Server()
admin = Admin(0, 'admin', True)
user_1 = User(1, 'user_1', True)
user_2 = User(2, 'user_2', True)
user_3 = User(3, 'user_3', False)
user_1.send_message(2, 'message_1', user_2, server)
user_2.send_message(3, 'message_2', user_3, server)
user_1.send_message(0, 'message_3', admin, server)
user_2.send_message(0, 'message_4', admin, server)
server.all()
admin.remove(1, server)
server.all()
admin.clear(server)
