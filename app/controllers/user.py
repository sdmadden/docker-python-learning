from db import db
from models.user import User

class UserController():
  def add_user(self, name, fruit) -> None:
    user = User(name=name, fruit=fruit)
    db.session.add(user)
    db.session.commit()

  def get_user(self, id) -> User:
    user = User.query.get_or_404(id)
    return user

  def update_user(self, id, name, fruit) -> None:
    user = User.query.get_or_404(id)
    user.name = name
    user.fruit = fruit
    db.session.add(user)
    db.session.commit()

  def delete_user(self, id) -> None:
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

  def get_all_users(self) -> list:
    users = User.query.all()
    return users