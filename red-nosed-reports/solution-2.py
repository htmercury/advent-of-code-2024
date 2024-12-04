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

def is_report_safe(report):
    is_safe = True
    
    for i in range(1, len(report)):
        level_offset = abs(report[i - 1] - report[i])
        if level_offset < 1 or level_offset > 3:
            is_safe = False
            break
            
    sorted_report = sorted(report)
    if sorted_report != report and sorted_report[::-1] != report:
        is_safe = False
            
    return is_safe

def solution():
    reports = parse_inputs(report_lines)
    
    safe_reports = 0
    
    for report in reports:
        if is_report_safe(report):
            # print(report)
            safe_reports += 1
        else:
            for i in range(len(report)):
                altered_report = report[:i] + report[i + 1:]
                if is_report_safe(altered_report):
                    # print(altered_report)
                    safe_reports += 1
                    break
    
    return safe_reports
    

print(solution())
