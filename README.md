# **DOCUMENTATION**
   
### **TelegramBOT** – отправка сообщении боту через микросервис.
**Микросервис написан на djangorestframework**

**Инструкция: Сперва регистрируемся на сайте. Дальше подключаемся к боту перейдя по сгенерированной ссылке. После подключения, можем отправлять сообщения урлу, котороя потом придет вам в телеграм от бота**


### URLS

**Registration. POST request** 
> https://factoryproject.herokuapp.com/users/create/
1. **username** (*Str*) - Логин пользователя.
2. **email** (*Str*) -  Емейл.
3. **first_name** (*Str*) - Имя пользователя.
4. **password** (*Str*) - Пароль.
5. **password2** (*Str*) - Подтверждение пароля.


**Authorization. POST request** 
> https://factoryproject.herokuapp.com/users/token-auth/
1. **username** (*Str*) - Логин пользователя.
2. **password** (*Str*) -  Пароль.
**Для авторизации** - Добавляем в хедер: Authorization Token: Your token


**Bot connection. GET request** 
> https://factoryproject.herokuapp.com/bot/connection/
**Авторизованным пользователям. После запроса заходим на сгенерированную ссылку и жмем /start в телеграме**


**Send message. POST request** 
> https://factoryproject.herokuapp.com/bot/send-message/
**Авторизованным пользователям.**
1. **text** (*Str*) - Ваше сообщение.



