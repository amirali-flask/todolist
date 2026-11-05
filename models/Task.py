from extentions import db

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer,autoincrement = True)
    user_id = db.Column(db.Integer)
    description = db.Column(db.String(500),nullable = True)
    user = db.relationship("User",back_populates = "tasks")

    __table_args__ = (
        db.PrimaryKeyConstraint("id",name = "pk_id"),
        db.ForeignKeyConstraint(["user_id"],["users.id"],onupdate = "CASCADE",ondelete = "CASCADE")
    )