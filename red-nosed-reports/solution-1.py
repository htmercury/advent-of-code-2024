from pathlib import Path
current_working_directory = Path.cwd()
input_file = open(str(current_working_directory) + '/input.txt', 'r')
report_lines = input_file.readlines()

def parse_inputs(lines):
    report_lines = []
    
    for line in lines:
        line = line.strip().split(' ')
        report_lines.append(list(map(lambda x: int(x), line)))

    return report_lines

def solution():
    reports = parse_inputs(report_lines)
    
    safe_reports = 0
    
    for report in reports:
        is_greater = report[0] > report[1]
        
        is_safe = True
        
        for i in range(1, len(report)):
            level_offset = abs(report[i - 1] - report[i])
            if level_offset < 1 or level_offset > 3:
                is_safe = False
                break
            
            if is_greater:
                if report[i - 1] <= report[i]:
                    is_safe = False
                    break
            else:
                if report[i - 1] >= report[i]:
                    is_safe = False
                    break
                
        if is_safe:
            # print(report)
            safe_reports += 1
    
    return safe_reports
    

print(solution())
