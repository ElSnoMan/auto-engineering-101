def login_with(py, username, password):
    py.visit('http://saucedemo.com')
    py.get('#user-name').type(username)
    py.get('#password').type(password)
    py.get('#login-button').click()
