from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# --- Basic configuration ---
Base = declarative_base()

# --- Models ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
class Task(Base): 
    __tablename__= "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task(title={self.title}, user={self.user.name})>"
    

# --- Create database ---
engine = create_engine(r"sqlite:///C:/Users/Julian Michelsy/dev/db/demo.db", echo=True)
    # MUY IMPORTANTE: 
        # - Usar /// despues de sqlite: para indicar que es una ruta absoluta local
        # - Usar r" al incio para indicar que es una url "raw string" y evitar errores

Base.metadata.create_all(engine)

# --- Session ---
Session = sessionmaker(bind=engine)
session = Session()

# --- Empty tables
for table in reversed(Base.metadata.sorted_tables):
    session.execute(table.delete())

session.commit()

# --- Insert data ---
user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")

task1 = Task(title="Learn SQLAlchemy", description="Follow the tutorial", user=user1)
task2 = Task(title="Write ORM code", description="Build the models", user=user1)
task3 = Task(title="Debug app", description="Fix issues", user=user2)

session.add_all([user1, user2, task1, task2, task3])
session.commit()

# --- Querys ---
print("\n--- Users ---")
for user in session.query(User).all():
    print(user)

print("\n--- Alice's Tasks ---")
alice_tasks = session.query(Task).join(User).filter(User.name == "Alice").all()
for task in alice_tasks:
    print(task)
