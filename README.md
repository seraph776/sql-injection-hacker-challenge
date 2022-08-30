<div id="top" align="center">

# SQL Injection 💉

![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=for-the-badge&labelColor=grey)
![GitHub Repo stars](https://img.shields.io/github/stars/seraph776/sql-injection-hacker-challenge?color=yellow&style=for-the-badge&labelColor=grey&label=stars&logo=github)
![GitHub forks](https://img.shields.io/github/forks/seraph776/sql-injection-hacker-challenge?color=green&style=for-the-badge&labelColor=grey&label=folks&logo=github)
![GitHub issues](https://img.shields.io/github/issues-raw/seraph776/sql-injection-hacker-challenge?color=red&style=for-the-badge&labelColor=grey&label=issues&logo=github)
![GitHub](https://img.shields.io/github/license/seraph776/sql-injection-hacker-challenge?color=blue&style=for-the-badge&labelColor=grey&label=License)

<img src="https://user-images.githubusercontent.com/72005563/187315379-005a9c12-3f37-4bdb-b70d-66254fd4837b.png" width="675"/> 



### HACK3R Challenge!

🐛 [Report Bugz](https://github.com/seraph776/sql-injection-hacker-challenge/issues/new?assignees=seraph776&labels=bug&template=bug-report---.md&title=Report+a+Bug) · 📫 [Contact me](#contact-me) · ☕[Buy me Coffee](https://www.buymeacoffee.com/seraph776) 

Show your support and give this repo a 💫 

</div>

<details>
<summary> ℹ️ Table of Content</summary>
 
 1. [Overview](#overview)
 2. [Requirements](#requirements)
 3. [Source Code](#source-code)
 4. [Screenshot](#screenshot)
 5. [Demonstration](#demonstration)
 6. [Setup Instructions](#setup-instructions)
 7. [Usage](#usage)
 8. [Discussions](#discussions)
 9. [Contact me](#contact-me)
 10. [License](#license)
 
</details> 


## 💡Overview

`SQL injection` is a type of cybersecurity attack that targets data-driven applications by inserting or "injecting" malicious SQL statements in the input field of a web page. Run this script, and try to execute a SQL Injection attack on a mock database that was designed for this challenge. If successful, you’ll have an opportunity to answer some fun **Bonus Challenge Questions**.

### 💥 Bonus Challenge Questions

After succefully dumping the database, try solving the following Bonus Questions:

1. `Decrypt` the administrator’s `password`. **Hint**: `MD(101)`
2. What 1995 `"crime/action/romance`" movie did these `users` played in? **Hint**: _Solve the first bonus question._


## Requirements

| Required | Version  |
| -------- | -------- |
| Python   | 3.0 +    |
| sqlite3  | 3.39.2   | 
| requests | 2.28.1   | 



## Source Code

<details>
<summary> Click to view source code </summary>

```python


import sqlite3
import requests

# SQL statements:
CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS usernames (id INTEGER PRIMARY KEY, username TEXT, password TEXT);"
INSERT_USER_DATA = "INSERT INTO usernames (username, password) VALUES (?, ?)"


def get_userdata() -> list:
    """Returns username, and password in tuple from online username.dat file."""
    # url to username and password file
    URL = "https://pastebin.com/raw/ih7szSSv"
    raw = [i.strip() for i in requests.get(URL).text.split('\n')]
    output = []
    for i in raw:
        users = i.split(', ')[0].split(',')[0]
        passwords = i.split(', ')[0].split(',')[1]
        output.append((users, passwords))
    return output


# Create database in memory
conn = sqlite3.connect(":memory:")
# Get usernames and passwords
user_data = get_userdata()

# Create table
conn.execute(CREATE_USERS_TABLE)
# Insert username, passwords into database
conn.executemany(INSERT_USER_DATA, user_data)


while True:
    INJECTION = input("Enter your SQL Injection:\n>  ")
    sql = f"SELECT * FROM usernames WHERE id = 776 {INJECTION}"
    try:
        results = conn.execute(sql).fetchall()
        if results:
            print(f"\n\033[92m" + "Good job, you did it!" + "\033[0m")
            with conn:
                for row in results:
                    print(row)
            conn.close()
            break
    except sqlite3.OperationalError as e:
        print("\n\033[91m" + "Nope, try again!" + "\033[0m")
        pass


```
</details>



## Screenshot

![image](https://user-images.githubusercontent.com/72005563/187289535-bed7a69d-965c-4a79-b317-2f1295705217.png)


## Demonstration
[![Replit Demo](https://img.shields.io/badge/Demo-blue?&logo=replit&logoColor=white&label=Replit&style=for-the-badge&labelColor=grey)](https://replit.com/@seraph776/SQL-Injection-Hacker-Challenge)


## Setup Instructions 

<details>
<summary>Create a Virtual Environment using Pipenv </summary>

1. Download [zip file](https://github.com/seraph776/sql-injection-hacker-challenge/archive/refs/heads/main.zip) 
2. Extract zip files
3. Change directory into the `sql-injection-attack-challenge\app` directory:

```
$ cd sql-injection-attack-challenege
```

4. Install from Pipfile:

```
$ pipenv install  
```

5. Run the application from within virtual environment:

```
$ pipenv run python app/script.py
```
ℹ️ [Virtual Environment Reference](https://docs.python-guide.org/dev/virtualenvs/).

</details>




## Usage
Once you run the script, you will be prompted to `"Enter you SQL Injection"`. Keep trying until you successfully achieve a SQL Injection attack! 
For more information read [documentation](https://github.com/seraph776/sql-injection-hacker-challenge/wiki).

## Reporting Issues

For instructions on reporting issues please read our [Contributing Guidelines](https://github.com/seraph776/sql-injection-hacker-challenge/blob/main/CONTRIBUTING.md). 



## Discussions

Have any Questions or suggestions? Visit [Discussions](https://github.com/seraph776/sql-injection-hacker-challenege/discussions) which is a space for our community to have conversations, ask questions and post answers without opening issues. Please read our [Code of Conduct](https://github.com/seraph776/sql-injection-hacker-challenge/blob/main/CODE-OF-CONDUCT.md) which defines the  standards for engaging with the community!

## Contact me

If you have any questions or wish to collaborate please contact me please feel free to contact me:  
- **Seraph** : [seraph776@gmail.com](mailto:seraph776@gmail.com)



## License 


[MIT](https://github.com/seraph776/sql-injection-hacker-challenge/blob/main/LICENSE) © [Seraph 天](https://github.com/seraph776) 



<div align="right">

[[↑] Back to top](#top)

</div>  


