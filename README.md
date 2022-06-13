# Linear-ODE-Solver
Numerically solves any order linear ODE with any forcing function and function coefficients.

HOW TO USE

  - ODE must be in this form
  
  c1(x)y^(m) + c2(x)y^(m-1) + c3(x)y^(m-2) + ... + cm(x)y^(m-m) = D(x)
  
    - m inidicates the order of the derivative
    - c1, c2, ..., cm are arbitrary functions of x
    - D is the forcing function, can be 0;
    
   - Create a linear object using ODE.linear(functions array)

    - must provide an array of callable functions in the format:
      - [c1, c2, ..., cm, D]
      - D must be the last element of the array

   - Invoke the run function using the new object.
      
      ex: test_object.run(initial conditions, stop value)
        - the initial conditions argument is an array of floats
        - the length is always one less than the order of the ODE 
        - the form of the array is [y^m(0), y^(m-1)(0), ..., y(0)]
        - The stop value is the x value that you want to stop at
  
  
  - The returned data is a 2D array containing the x and y values of the solution
