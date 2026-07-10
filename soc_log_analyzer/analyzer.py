import re
import os

# ==========================
# SOC LOG ANALYZER
# ==========================

print("=" * 55)
print("               SOC LOG ANALYZER")
print("=" * 55)

# Ask user for log file
log_file_name = input("\nEnter the path to the log file: ").strip().strip('"').strip("'")

# Check if file exists
if not os.path.isfile(log_file_name):
    print("\n❌ Error: File not found!")
    exit()

# Read the log file
with open(log_file_name, "r") as file:
    logs = file.readlines()

print("\n✅ Log file loaded successfully.")

# Regex
pattern = r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"

failed_attempts = {}
users_per_ip = {}

total_failed = 0

# Analyze logs
for line in logs:

    match = re.search(pattern, line)

    if match:

        username = match.group(1)
        ip = match.group(2)

        total_failed += 1

        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1

        if ip not in users_per_ip:
            users_per_ip[ip] = set()

        users_per_ip[ip].add(username)

# Summary
print("\n" + "=" * 55)
print("                 ANALYSIS SUMMARY")
print("=" * 55)

print(f"Total Failed Logins : {total_failed}")
print(f"Unique IP Addresses : {len(failed_attempts)}")

# Most active IP
most_active_ip = None
highest_attempts = 0

for ip, count in failed_attempts.items():

    if count > highest_attempts:
        highest_attempts = count
        most_active_ip = ip

if most_active_ip:
    print(f"Most Active IP      : {most_active_ip}")
    print(f"Highest Attempts    : {highest_attempts}")

print("\n" + "=" * 55)
print("                 RISK ANALYSIS")
print("=" * 55)

# Sort highest first
sorted_ips = sorted(
    failed_attempts.items(),
    key=lambda item: item[1],
    reverse=True
)

for ip, count in sorted_ips:

    if count >= 6:
        risk = "HIGH 🔴"

    elif count >= 3:
        risk = "MEDIUM 🟡"

    else:
        risk = "LOW 🟢"

    print(f"\nIP Address : {ip}")
    print(f"Attempts   : {count}")
    print(f"Risk Level : {risk}")

    print("Users Targeted:")

    for user in users_per_ip[ip]:
        print(f"  - {user}")

print("\n" + "=" * 55)
print("Analysis Complete ✅")
print("=" * 55)