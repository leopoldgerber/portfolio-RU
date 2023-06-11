# Report Automation Script

<code>[V7001 (Py)](V7001.py)</code>
<code>[V7002 (Py)](V7002.py)</code>
<code>[V7003 (Py)](V7003.py)</code>
<code>[V7004 (Py)](V7004.py)</code>
<code>[V7001 (SQL)](v7001_sql.sql)</code>
<code>[V7003 (SQL)](v7003_sql.sql)</code>

- [1 - Task information](#--objective--)
- [2 - Examples of scripts and queries](#examples-of-scripts-and-queries)

<br>

### - Objective -
Eliminate the need to hire an employee to manually assemble reports on weekends. 

### - Expected result -
A family of scripts for automating reports on closed and open trades, deposits and withdrawals, and hedge fund information for a national bank. A bot for sending reports to everyone assigned.

### - Technical tasks -
- Data collection
- Data preprocessing
- Feature engineering
- Report automation

### - NOTE -
The project contains 4 scripts, each of which performs its individual assembly at different reporting times (weekly and monthly). All external queries are written individually according to the tasks of the report. The directory contains 2 shortened queries. Due to commercial confidentiality, the data has been changed and key points have been removed. The reduction does not affect the skills shown.


<br>

## Examples of scripts and queries
### Script

The <b>mysql</b> library for connecting to a database. Using the <b>configuration</b> file to further connect all scripts to the same login source and due to the confidentiality of login data. Using an <b>external query</b> for convenient editing.

![image](https://github.com/leopoldgerber/portfolio/assets/114569329/b916f91e-23ec-4957-9709-b15cc438a107)

<br>

### Query
Create and fill additional tables in the test base to optimize performance.

![image](https://github.com/leopoldgerber/portfolio/assets/114569329/27757d60-9db4-42ce-9f95-5eb4e5d06991)

[Scroll up](#report-automation-script)
