# SOC Log Analyzer for SSH Authentication Logs

A Python-based Security Operations Center (SOC) Log Analyzer that parses Linux SSH authentication logs to detect failed login attempts, identify suspicious IP addresses, and perform basic threat analysis.

---

## Features

- Reads authentication logs from any file path
- Detects failed SSH login attempts
- Extracts usernames and IP addresses using Regular Expressions (Regex)
- Counts failed login attempts by IP address
- Identifies the most active attacking IP
- Assigns risk levels (LOW, MEDIUM, HIGH)
- Displays targeted usernames for each IP
- Provides a clean analysis summary in the terminal

---

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- File Handling
- Dictionaries
- Sets
- OS Module

---

## Project Structure

```
soc_log_analyzer/
│
├── analyzer.py
├── auth.log
├── README.md
├── requirements.txt
├── test.py
└── logs/
```

---

## How to Run

Clone the repository

```bash
git clone <your-repository-link>
```

Move into the project directory

```bash
cd soc_log_analyzer
```

Run the analyzer

```bash
python analyzer.py
```

Enter the path to the log file when prompted.

Example

```
auth.log
```

or

```
C:\Users\Username\Downloads\auth.log
```

---

## Sample Output

```
=======================================================
                SOC LOG ANALYZER
=======================================================

Total Failed Logins : 8
Unique IP Addresses : 3

Most Active IP      : 192.168.1.10
Highest Attempts    : 6

=======================================================
                 RISK ANALYSIS
=======================================================

IP Address : 192.168.1.10
Attempts   : 6
Risk Level : HIGH

Users Targeted:
 - root
 - admin
```

---

## Skills Demonstrated

- Python Programming
- Cybersecurity Fundamentals
- Log Analysis
- Regular Expressions
- Data Processing
- Threat Detection
- Blue Team Concepts

---

## Future Improvements

- Windows Event Log Support
- Real-time Log Monitoring
- Dashboard using Flask
- Export Results to CSV/JSON
- SQLite Database Integration
- Threat Scoring System

---

## Author

**Moolya Nishmitha Narayana**

Cybersecurity Student | SOC & Blue Team Enthusiast