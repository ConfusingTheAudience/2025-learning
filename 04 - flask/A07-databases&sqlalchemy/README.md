# SQLAlchemy
Clean SQLAlchemy, SQLAlchemy with Flask
<br />
-> create_engine, config, class, create_all

<br />
<br />

**1. Basic connection to SQLAlchemy**
<br />
<br />
```diff
+ pip install sqlalchemy

+ from sqlalchemy import create_engine, text
```
begin()
```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydatabase.db', echo=True)

with engine.begin() as conn:
    conn.execute(text('CREATE TABLE people AS SELECT NULL AS name, NULL AS age WHERE 0'))
```
connect()
```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydatabase.db', echo=True)

with engine.connect() as conn:
    conn.execute(text('SELECT NULL AS name, NULL AS age'))
```

engine.begin() <br />
Transaction: Automatic <br />
Commit/Rollback: Done automatically <br />
Exception handling:	Automatic rollback on exception <br />
Use case:	Safe transactional execution <br />

engine.connect() <br />
Transaction: Manual <br />
Commit/Rollback: You must do it <br />
Exception handling:	Manual <br />
Use case:	Low-level SQL execution <br />

<br />
<br />

**1. Basic connection to SQLAlchemy with Flask**
```diff
+ pip install Flask-SQLAlchemy

+ from flask_sqlalchemy import SQLAlchemy
```
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
```

<br />
<br />

**2. Basic class with pure SQLAlchemy**
```python
from sqlalchemy import create_engine, text

# 1. Create the engine — connect to the SQLite file
engine = create_engine("sqlite:///mydatabase.db", echo=True)

# 2. Create the table (raw SQL)
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """))

# 3. Insert data into the table
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO people (name, age) VALUES (:name, :age)"),
        [{"name": "Ala", "age": 20}, {"name": "Olek", "age": 25}]
    )

# 4. Read data from the table
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM people"))
    for row in result:
        print(row)
```

or

```diff
+ from sqlalchemy import create_engine, Column, Integer, String
+ from sqlalchemy.orm import declarative_base, sessionmaker
```
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Create the engine (connects to the database)
engine = create_engine("sqlite:///example.db", echo=True)

# 2. Base class for ORM
Base = declarative_base()

# 3. Define the class representing the table
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 4. Create the tables in the database
Base.metadata.create_all(engine)

# 5. Create a session for database operations
Session = sessionmaker(bind=engine)
session = Session()

# 6. Add a record
alice = Person(name="Alice", age=30)
session.add(alice)
session.commit()

# 7. Read records
people = session.query(Person).all()
for p in people:
    print(p.name, p.age)

```

**2. Basic class SQLAlchemy with Flask**
```diff
+ from flask import Flask
+ from flask_sqlalchemy import SQLAlchemy
```
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 1. Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example_flask.db'

# 2. Initialize SQLAlchemy with Flask
db = SQLAlchemy(app)

# 3. Define ORM model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

with app.app_context():
    # 4. Create tables in the database
    db.create_all()

    # 5. Add a record
    alice = Person(name="Alice", age=30)
    db.session.add(alice)
    db.session.commit()

    # 6. Read records
    people = Person.query.all()
    for p in people:
        print(p.name, p.age)
```
Pure SQLAlchemy <br />
Base class:	declarative_base()<br />
Session:	sessionmaker() <br />
Commit:	manual <br />
Web integration:	none <br />
Migrations:	Alembic separately <br />

Flask SQLAlchemy <br />
Base class:	db.Model <br />
Session:	db.session <br />
Commit:	manual (within Flask context) <br />
Web integration:	automatic, linked to Flask <br />
Migrations:	Flask-Migrate integration <br />

<br />
<br />

**3. Create tables in the database pure SQLAlchemy**
```python
with engine.connect() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)
```

or

```python
Base.metadata.create_all(engine)
```
After calling Base.metadata.create_all(engine) the tables will only be created once. If you run the code again, the tables will not be created again unless you modify the model class (like by adding a new column)

**3. Create tables in the database with Flask**
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example_flask.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

with app.app_context():
    db.create_all()
```

or

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

if __name__ == "__main__":
    with app.app_context():  # MUST HAVE in flask to work with database
        db.create_all()  # Create if not exist
    app.run()
```

<br />
<br />

**repr use**
```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Person {self.name}, {self.age}>"
```
repr - is a special method in Python that defines how an object is represented as a string, especially when you try to print or log the object. It's useful for providing a human-readable output for debugging and logging purposes

<br />
