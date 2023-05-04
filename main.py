import datetime, re

def create_membership():
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    whether_valid = False

    while not whether_valid:
      user = {}

      while True:
          username = input('username(사용자 이름): ')
          username_p = re.compile('^[가-힇]{2,4}$')
          if username_p.match(username):
              user['username'] = username
              break
          else:
              print('username이 2-4글자 사이 한글로 입력되었는지 확인해주세요.')
      
      while True:
          password = input('password(비밀번호): ')
          if password[0].isupper() and len(password) >= 8 and ('!' in password or '@' in password or '#' in password or '$' in password):
              user['password'] = password
              break
          else:
              print('password 제한 조건을 확인해주세요.')
      
      while True:
          email = input('e-mail: ')
          email_p = re.compile('^[a-zA-Z0-9]+$')
          if not email.endswith('.com'):
              print('e-mail 포맷을 다시 확인해주세요.')
              continue
          email_chk = email.replace('@', '')[:-4]
          if email_p.match(email_chk) and '@' in email:
              user['email'] = email
              break
          else:
              print('e-mail 포맷을 다시 확인해주세요.')

      user['stnr_date'] = stnr_date
      users.append(user)

      ask = input('새로운 user를 등록하시겠습니까? (y or n)')
      if ask == 'y':
          continue
      else:
          whether_valid = True

    return users


def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    for data in user_list:
        f.write(', '.join(i for i in data.values()) + '\n')
    f.close()
    

def run():
    user_list = create_membership()
    load_to_txt(user_list)
    
run()