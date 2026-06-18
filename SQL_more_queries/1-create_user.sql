-- creates a server user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd'
GRANT PRIVILEGE ON hbtn_0c_0.* TO user_0d_1