# Gnuplot script file for plotting data in file "test01.txt"
# This file is called  term_gnuplot.p
set terminal pslatex rotate
set output "test01.tex"
reset

unset label                            # remove any previous labels
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set xlabel "ρ" 
set ylabel "Ν"  rotate by 90 left
plot    "test01.txt" using 1:2 title 'simulation' with linespoints lt -1 pt 8, \
      "test01.txt" using 1:3 title 'theory' with linespoints lt -1 pt 5
set terminal png
set output "test01.png"
replot

#  To run ---> gnuplot  test_gnuplot1.p
