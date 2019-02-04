from random import choice

names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles", "Christopher",
         "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth", "George", "Joshua", "Kevin",
         "Brian", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Stephen",
         "Jonathan", "Larry", "Justin", "Scott", "Brandon", "Frank", "Benjamin", "Gregory", "Raymond", "Samuel", "Patrick",
         "Alexander", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Henry", "Jose", "Douglas", "Peter", "Adam", "Nathan",
         "Zachary", "Walter", "Kyle", "Harold", "Carl", "Jeremy", "Gerald", "Keith", "Roger", "Arthur", "Terry", "Lawrence",
         "Sean", "Christian", "Ethan", "Austin", "Joe", "Albert", "Jesse", "Willie", "Billy", "Bryan", "Bruce", "Noah",
         "Jordan", "Dylan", "Ralph", "Roy", "Alan", "Wayne", "Eugene", "Juan", "Gabriel", "Louis", "Russell", "Randy",
         "Vincent", "Philip", "Logan", "Bobby", "Harry", "Johnny"]

surnames = ["Smith", "Jones", "Taylor", "Williams", "Brown", "Davies", "Evans", "Wilson", "Thomas", "Roberts", "Johnson",
            "Lewis", "Walker", "Robinson", "Wood", "Thompson", "White", "Watson", "Jackson", "Wright", "Green", "Harris",
            "Cooper", "King", "Lee", "Martin", "Clarke", "James", "Morgan", "Hughes", "Edwards", "Hill", "Moore", "Clark",
            "Harrison", "Scott", "Young", "Morris", "Hall", "Ward", "Turner", "Carter", "Phillips", "Mitchell", "Patel",
            "Adams", "Campbell", "Anderson", "Allen", "Cook", "Bailey", "Parker", "Miller", "Davis", "Murphy", "Price", "Bell",
            "Baker", "Griffiths", "Kelly", "Simpson", "Marshall", "Collins", "Bennett", "Cox", "Richardson", "Fox", "Gray",
            "Rose", "Chapman", "Hunt", "Robertson", "Shaw", "Reynolds", "Lloyd", "Ellis", "Richards", "Russell", "Wilkinson",
            "Khan", "Graham", "Stewart", "Reid", "Murray", "Powell", "Palmer", "Holmes", "Rogers", "Stevens", "Walsh", "Hunter",
            "Thomson", "Matthews", "Ross", "Owen", "Mason", "Knight", "Kennedy", "Butler", "Saunders", "Cole", "Pearce", "Dean",
            "Foster", "Harvey", "Hudson", "Gibson", "Mills", "Berry", "Barnes", "Pearson", "Kaur", "Booth", "Dixon", "Grant",
            "Gordon", "Lane", "Harper", "Ali", "Hart", "Mcdonald", "Brooks", "Ryan", "Carr", "Macdonald", "Hamilton",
            "Johnston", "West", "Gill", "Dawson", "Armstrong", "Gardner", "Stone", "Andrews", "Williamson", "Barker", "George",
            "Fisher", "Cunningham", "Watts", "Webb", "Lawrence", "Bradley", "Jenkins", "Wells", "Chambers", "Spencer", "Poole",
            "Atkinson", "Lawson"]


def fake_name():
    return choice(names)


def fake_surname():
    return choice(surnames)


def fake_fullname():
    return choice(names) + " " + choice(surnames)
