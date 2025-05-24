a = '''
'The CPU is often referred to as the brain of the computer.', true

'HTML is a programming language.', false

'Binary code consists of 0s and 1s.', true

'Python is a compiled language.', false

'RAM is volatile memory.', true

'HTTP stands for HyperText Transfer Protocol.', true

'JavaScript is the same as Java.', false

'A byte consists of 8 bits.', true

'CSS is used for styling web pages.', true

'Linux is an open-source operating system.', true

'All programming languages require a compiler.', false

'The cloud refers to physical storage devices.', false

'SQL is used for database management.', true

'IPv6 addresses are 128 bits long.', true

'Machine learning is a subset of artificial intelligence.', true

'Git and GitHub are the same thing.', false

'The first computer bug was an actual insect.', true

'CSS stands for Cascading Style Sheets.', true

'The Internet and the World Wide Web are the same thing.', false

'Python uses curly braces {} for code blocks.', false

'A compiler translates code line by line as it executes.', false

'JavaScript can only run in web browsers.', false

'The motherboard connects all computer components.', true

'TCP/IP is the protocol suite of the Internet.', true

'Machine code is the lowest-level programming language.', true

'All algorithms must have a finite number of steps.', true

'CSS can change the content of HTML elements.', false

'The DOM represents a document as a tree structure.', true

'Python lists are mutable.', true

'Java is platform-independent because of the JVM.', true

'Big O notation describes algorithm efficiency.', true

'A stack follows FIFO (First In First Out) principle.', false

'IPv4 addresses are 32 bits long.', true

'The blockchain is a type of database.', true

'All web browsers use the same rendering engine.', false

'Recursion is when a function calls itself.', true

'Assembly language is a high-level language.', false

'The BIOS is responsible for booting the computer.', true

'JSON stands for JavaScript Object Notation.', true

'All programming languages are case-sensitive.', false

'The GPU is only used for graphics processing.', false

'DNS translates domain names to IP addresses.', true

'Python uses dynamic typing.', true

'All operating systems use the same file system.', false

'A quantum bit (qubit) can be 0 and 1 simultaneously.', true

'AJAX can only work with XML data.', false

'The CPU cache is faster than RAM.', true

'Regular expressions are used for pattern matching.', true

'All web applications require JavaScript.', false

'A VPN encrypts your internet connection.', true

'The term "bit" comes from "binary digit".', true

'CSS Grid and Flexbox are the same technology.', false

'All computer viruses can replicate themselves.', false

'The first electronic computer was ENIAC.', true

'SQL injection is a type of cyber attack.', true

'Python was named after the snake.', true

'All programming languages have garbage collection.', false

'The Linux kernel was created by Linus Torvalds.', true

'HTTP is more secure than HTTPS.', false

'A tuple in Python is mutable.', false

'All web pages must have a doctype declaration.', false

'The XOR gate returns true when both inputs are true.', false

'CSS can create animations without JavaScript.', true

'All sorting algorithms have the same time complexity.', false

'The first computer programmer was Ada Lovelace.', true

'JavaScript is a single-threaded language.', true

'All databases use SQL.', false

'The @ symbol in CSS is used for at-rules.', true

'Python 2 and Python 3 are fully compatible.', false

'All encryption algorithms are unbreakable.', false

'The term "API" stands for Application Programming Interface.', true

'React is a JavaScript framework.', false

'All computer networks use TCP/IP.', false

'The <div> element is a block-level element.', true

'Python supports multiple inheritance.', true

'All programming languages use the same operators.', false

'The first webpage is still online.', true

'JavaScript is the only client-side scripting language.', false

'All search algorithms have O(1) time complexity.', false

'The
tag is a self-closing tag in HTML.', true

'Python lists can contain elements of different types.', true

'All programming languages have built-in hash tables.', false

'The first computer mouse was made of wood.', true

'JavaScript can manipulate the DOM.', true

'All sorting algorithms are stable.', false

'The <span> element is an inline element.', true

'Python dictionaries are unordered (before Python 3.7).', true

'All web servers run on Linux.', false

'The first computer virus was created in the 1980s.', true

'JavaScript has a Date object for handling dates.', true

'All programming languages use zero-based indexing.', false

'The <meta> tag provides metadata about the HTML document.', true

'Python has a built-in function called print().', true

'All computer processors have the same architecture.', false

'The first domain name ever registered was symbolics.com.', true

'JavaScript can be used for server-side programming.', true

'All programming problems can be solved recursively.', true

'The <head> section is visible on the webpage.', false

'Python supports function overloading.', false

'All programming languages are Turing complete.', false

'''

for line in a.split("\n"):
    try:
        a, b = line.split(", ")
    except:
        continue
    print(f"db.query(\"INSERT INTO questions VALUES (DEFAULT, {a}, {b});\")")