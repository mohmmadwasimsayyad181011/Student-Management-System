# Testing Report
**Project:** Student Record and Academic Management System  
**PRN:** 2126UMLM1123

Run the application and record the actual result observed. The results below are expected outcomes, not claims that screenshots have already been captured.

| ID | Test | Input/condition | Expected result |
|---|---|---|---|
| T01 | Add student | New unique roll number and valid details | Record added successfully |
| T02 | Duplicate prevention | Add a roll number already in the list | Duplicate warning; no second record |
| T03 | Search existing | Search for a known roll number | Matching profile displayed |
| T04 | Search missing | Search for `999` when absent | Student not found |
| T05 | Update name | Select an existing student and choose Name | Name updated |
| T06 | Invalid attendance | Enter -5 or 120 | Invalid attendance message; old value retained |
| T07 | Delete existing | Delete a known roll number | Record removed |
| T08 | Delete missing | Delete unknown roll number | Student not found |
| T09 | Empty display | Start with no records and display all | Friendly empty-state message |
| T10 | Average marks | Marks 80, 90, 70 | Average is 80.00 |
| T11 | No marks | Calculate average for student with no marks | No marks available message |
| T12 | Highest scorer | Demo data | Sara Khan has average 90.67 |
| T13 | Department filter | Computer Science | Aarav Patil and Rohan Deshmukh shown in demo data |
| T14 | Count | Demo data loaded | Total students: 3 |
| T15 | Unique data | Load demo data and show unique data | Duplicate departments/subjects/clubs appear once |
| T16 | Invalid menu | Enter an unsupported menu number | Invalid menu option message |

## Sample dry run: average marks
Input marks: 80, 90, 70  
Total = 80 + 90 + 70 = 240  
Number of marks = 3  
Average = 240 / 3 = 80.00

## Trace table: adding a student
| Step | Action | Expected state |
|---|---|---|
| 1 | Start with empty list | `students = []` |
| 2 | Enter roll number `201` | Check list for duplicate |
| 3 | No matching record exists | Continue to read details |
| 4 | Create student dictionary | Dictionary has the entered fields |
| 5 | Append dictionary | List length becomes 1 |
| 6 | Print confirmation | `Student added successfully.` |

## Evidence to add
After you run your own program, save screenshots showing:
1. Main menu.
2. Successful add and duplicate prevention.
3. Search result.
4. Average marks and highest scorer.
5. Department filtering and unique-data output.
6. An empty or invalid-input case.

Do not submit expected outcomes as if they were screenshots or test runs you personally performed.
