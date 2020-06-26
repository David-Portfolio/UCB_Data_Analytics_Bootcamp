# Pewlett-Hackard-Analysis

  The purpose of this project is to analyze the employee population at Pewlett-Hackard. Specifically, as baby-boomers begin to retire, identify (1) employees that are close to retirement (2) positions that will need to be backfilled due to their retirement (3) employees that are eligible for mentorship. 6 csv files were available for the data source. Since each csv file contained different data sets, we used SQL to create a database that allowed us to query this information by joining the files through the primary/foreign keys (see ERD). This is an upgrade from the previous method of Excel/VBA and will allow for the data to scale and be optimized for query for future business needs.
  Based on the criteria for retiring employees (those born 1952-1955), there are a total of 90,398 identified employees eligible for the retirement package. Grouping these employees by their recent title, below is the count and as a % of the total retiring employees:
          -Engineer: 14,222 (16%)
          -Senior Engineer: 29,414 (33%)
          -Manager: 2 (<1%)
          -Assistant Engineer: 1,761 (2%)
          -Staff: 12,243 (14%)
          -Senior Staff: 28,254 (31%)
          -Technique Leader: 4,502 (5%)
It is possible that we could further group titles to consolidate the above i.e. Engineer/Senior Engineer/Assistant Engineer into Engineer, or Staff/Senior Staff into Staff, which would decrease the title count from 7 to 4. However, there is value in that distinction for backfill purposes and the mentorship program.
  To help with the transition of the forecasted retirement, there are a total of 1,940 employees eligible for mentorship based on the criteria (those born 01/01/1965-12/31/1965). This data is available in the mentorship_eligibility.csv. You'll note that may be multiple records for an employee as it is displaying all the titles the employee had at Pewlett-Hackard (one row record for each title). This is helpful to know for the mentorship program as it shows progression during the company tenure and that the employee is knowledgeable/skilled in their area. 

**Next Steps:**
-Compare mentor count against the retirement count by title. The mentorship_eligibility.csv will need to be updated by querying the employees for only the recent title, otherwise the number of mentors will be overstated.
-Query for list of potential mentees based on defined criteria
-Confirm retirees, mentors, mentees and flag in database
-Assign mentors to mentees

**Files References:**
-Employee_DB.png (ERD)
-departments.csv (data source)
-dept_emp.csv (data source)
-dept_manager.csv (data source)
-employees.csv (data source)
-salaries.csv (data source)
-titles.csv (data source)
-retiring_emp_by_recent title (deliverable1: SQL query)
-num_recent_titles_retiring (deliverable1: SQL query)
-current_emp_born_19520101_to_19551231 (deliverable1: SQL query)
-mentorship_eligibility (deliverable2: SQL query)
