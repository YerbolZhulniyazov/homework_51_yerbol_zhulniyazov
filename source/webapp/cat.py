import random


class Cat:
    name = None
    age = random.randint(1, 15)
    happiness = 30
    satiety = 50
    image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbiIZgIifqt6gfvZzh3vQtjsEDMSET_TgXlg&usqp=CAU'
    status = 'active'

    @classmethod
    def action(cls, action_form):
        if action_form:
            if action_form == 'sleep':
                message = cls.sleep()
            elif action_form == 'eat':
                message = cls.eat()
            else:
                message = cls.play()
            cls.set_image()
            return message

    @classmethod
    def get_status(cls):
        if cls.satiety >= 0:
            return True
        else:
            return None

    @classmethod
    def eat(cls):
        if cls.status == 'sleep':
            return 'На данный момент кот спит, его нельзя покормить'
        cls.satiety += 15
        cls.happiness += 5
        if cls.satiety >= 80:
            cls.happiness -= 35
        return 'Кота покормили'

    @classmethod
    def play(cls):
        if cls.status == 'sleep':
            cls.happiness -= 5
            cls.status = 'active'
            return 'Кота разбудили и поиграли с ним'

        cls.happiness += 15
        cls.satiety -= 10

        if random.uniform(0, 1) <= 0.33:
            cls.happiness = 0
        return 'С котом поиграли'

    @classmethod
    def sleep(cls):
        if cls.status == 'sleep':
            return 'Кот уже спит'
        cls.status = 'sleep'
        return 'Кота уложили спать'

    @classmethod
    def set_image(cls):
        if cls.happiness <= 10:
            cls.image = 'https://cdn.shopify.com/s/files/1/0011/0552/articles/RCF_blog_1600x.jpg?v=1556467722'
        if 10 < cls.happiness <= 30:
            cls.image = 'https://people.com/thmb/bHUHVDp056iy-uwjxIWVtQLH9f4=/1500x0/filters:no_upscale():' \
                        'max_bytes(150000):strip_icc():focal(779x560:781x562)/' \
                        'startled-cat-5-e1d007b13bf14746a4f4dfe369d6d6ce.jpg'
        if 35 < cls.happiness <= 65:
            cls.image = 'https://i.pinimg.com/originals/9b/f5/35/9bf5358ee5f817ca785463de59192eab.jpg'
        if cls.happiness > 65:
            cls.image = 'https://encrypted-tbn0.gstatic.com/' \
                        'images?q=tbn:ANd9GcTzQ87975v6COPw8cTp0nzhiUN8N_wc-0wRGg&usqp=CAU'


