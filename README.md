# ev_228
Code for EV228

# 10/28/25 First Import Code
- Imported KRDU data to VScode
- Selected NOV data frame and YEARS
- Converted YEARS to datetime in %Y format
- Removed the last datapoint as it was 999.9
- Plotted NOV temperature data against YEARS
  
No generative AI was used for this assignment

# 10/29/25 Practical 4
- The first file is the KRDU file. In this file the KRDU data is imported and selected to display one variable
- In the rest of the file I define two functions. The first allows the selection of a defined variable in a defined dataset
- The second function does the same thing but also calculates statistics and generates a graph. I also replaced 999.90 values with NaN values to create accurate graphs
- The station-data file imports the KRDU.py file so that I can call the previously defined functions into a seperate script
- To use the function in this script you would start by calling the KRDU module with krdu. then you would call the function either select_variable or complete_var and define the two arguments. The first argument is the file path and the second argumenent is the variable you want to select

No generative AI was used for this assignment