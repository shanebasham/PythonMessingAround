
hrsystemtxt = 'C:\\Users\\shane\\OneDrive\\Desktop\\PythonMessingAround\\Week 11 + 12\\hr_system.txt'
with open(hrsystemtxt) as file:
    for line in file:
        stripped = line.strip()
        parts = stripped.split(' ')
        salary = float(parts[3])
        amount = salary / 24
        if parts[2].lower() == 'engineer':
            amount += 1000
        print(f'{parts[0]} (ID: {parts[1]}), {parts[2]} - ${amount:.2f}, Salary: ${salary:.2f}')


