/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

function gradingStudents(grades) {
    // Write your code here   
    for (let i = 0; i < grades.length; i++) {        
        if (((grades[i] + 2) % 5 == 0) && (grades[i] + 2 > 39)) {
            grades[i] = grades[i] + 2;
        } else if (((grades[i] + 1) % 5 == 0) && (grades[i] + 2 > 39)) {
            grades[i] = grades[i] + 1;
        }
    }
    return grades;
}
