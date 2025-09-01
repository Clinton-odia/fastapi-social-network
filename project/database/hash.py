from passlib.context import CryptContext

pwd_cxt = CryptContext("bcrypt", depecated="auto")


class Hash:
    def bcrypt(password):
        return pwd_cxt.hash(password)

    def verify(plain_password, hash_password):
        return pwd_cxt.verify(plain_password, hash_password)
