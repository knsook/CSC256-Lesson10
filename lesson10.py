
url_ddg = "https://api.duckduckgo.com"

presidents = ["George Washington", "John Adams", "Thomas Jefferson",
              "James Madison", "James Monroe", "John Quincy Adams",
              "Andrew Jackson", "Martin Van Buren", "William Henry Harrison",
              "John Tyler", "James K Polk", "Zachary Taylor",
              "Millard Fillmore", "Franklin Pierce", "James Buchanan",
              "Abraham Lincoln", "Andrew Johnson", "Ulysses S Grant",
              "Rutherford B Hayes", "James Garfield", "Chester A Arthur",
              "Grover Cleveland", "William Howard Taft", "Woodrow Wilson",
              "Warren G Harding", "Calvin Coolidge", "Herbert Hoover",
              "Theodore Roosevelt", "William McKinley", "Benjamin Harrison",
              "Franklin D Roosevelt", "Harry S Truman", "Dwight D Eisenhower",
              "John F Kennedy", "Lyndon B Johnson", "Richard M Nixon",
              "Gerald R Ford", "James Carter", "Ronald Reagan",
              "George H W Bush", "William J Clinton", "George W Bush",
              "Barack Obama", "Donald J Trump"]

def test_ddg0():

    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()

    assert "DuckDuckGo" in rsp_data["presidents of the united states"]
