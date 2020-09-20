# School_District_Analysis

**Recreate the district and school summary DataFrames.**
  **How is the district summary affected? (note: numbers are rounded)**
      -Total Schools: 15 (no change)
      -Total Students: 39,170 (no change)
      -Total Budget: $24,649,428.00 (no change)
      -Average Math Score: 78.9 (-0.1 change)
      -Average Reading Score: 81.9 (no change)
      -% Passing Math: 74 (-1 change)
      -% Passing Reading: 85 (-1 change)
      -% Overall Passing: 64 (-1 change)
  **How is the school summary affected? (note: numbers are rounded)**
       -After replacing the reading and math scores for ninth graders at Thomas High School with NaN, only changes are for Thomas High          School
          --Average Math Score: 83.35 (-0.07 change)
          --Average Reading Score: 83.90 (0.05 change)
          --% Passing Math: 66.91 (-26.36 change)
          --% Passing Reading: 69.66 (-27.65 change)
          --% Overall Passing: 65.08 (-25.87 change)
**Recalculate the high- and low-performing schools.**
  **How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance, relative to the other           schools?**
       -Average Math Score: 6th highest school (previously 4th highest school)
       -Average Reading Score: 5th highest school out of 15 (no change)
       -% Passing Math: 9th highest school out of 15 (previously 7th highest school)
       -% Passing Reading: 15th highest school out of 15 (previously 1st highest school)
       -% Overall Passing: 8th highest school out of 15 (previously 2nd highest school)
**Recalculate the scores by grade, scores by school spending, scores by school size, and scores by school type.**
  **How does replacing the ninth-grade scores affect the following?**
       -Math and Reading Scores by Grade
            --Math Score: no change except for 9th grade at Thomas High School which is now NaN (previously 83.6)
            --Reading Score: no change except for 9th grade at Thomas High School which is now NaN (previously 83.7)
       -Scores by School Spending (note: numbers are rounded)
            -<$584
                --Average Math Score: 83.5 (no change)
                --Average Reading Score: 83.9 (no change)
                --% Passing Math: 93 (no change)
                --% Passing Reading: 97 (no change)
                --% Overall Passing: 90 (no change)           
            -$585-629
                --Average Math Score: 81.9 (no change)
                --Average Reading Score: 83.2 (no change)
                --% Passing Math: 87 (no change)
                --% Passing Reading: 93 (no change)
                --% Overall Passing: 81 (no change)                       
            -$630-644
                --Average Math Score: 78.5 (no change)
                --Average Reading Score: 81.6 (no change)
                --% Passing Math: 67 (-6 change)
                --% Passing Reading: 77 (-7 change)
                --% Overall Passing: 56 (-7 change)
            -$645-675
                --Average Math Score: 77.0 (no change)
                --Average Reading Score: 81.0 (no change)
                --% Passing Math: 66 (no change)
                --% Passing Reading: 81 (no change)
                --% Overall Passing: 54 (no change)                       
       -Scores by School Size (note: numbers are rounded)
            -Small (<1000)
                --Average Math Score: 83.8 (no change)
                --Average Reading Score: 83.9 (no change)
                --% Passing Math: 94 (no change)
                --% Passing Reading: 96 (no change)
                --% Overall Passing: 90 (no change)
            -Medium (1000-2000)
                --Average Math Score: 83.4 (no change)
                --Average Reading Score: 83.9 (no change)
                --% Passing Math: 88 (-6 change)
                --% Passing Reading: 91 (-6 change)
                --% Overall Passing: 85 (-6 change)
            -Large (2000-5000)
                --Average Math Score: 77.7 (no change)
                --Average Reading Score: 81.3 (no change)
                --% Passing Math: 70 (no change)
                --% Passing Reading: 83 (no change)
                --% Overall Passing: 58 (no change)               
       -Scores by School Type (note: numbers are rounded)
            -Charter
                --Average Math Score: 83.5 (no change)
                --Average Reading Score: 83.9 (no change)
                --% Passing Math: 90 (-4 change)
                --% Passing Reading: 93 (-4 change)
                --% Overall Passing: 87 (-3 change)
            -District
                --Average Math Score: 77.0 (no change)
                --Average Reading Score: 81.0 (no change)
                --% Passing Math: 67 (no change)
                --% Passing Reading: 81 (no change)
                --% Overall Passing: 54 (no change)               
