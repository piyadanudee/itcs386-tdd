# Part B: Reflection

## 1. Tests and Production Code
I wrote tests for quantity creation, multiplication, addition, and unit conversion. I wrote 15 tests and 70 lines of production code. The ratio was 15:70, or about 1:4.7.

## 2. Longest Red Bar
Mixed-unit addition took the longest because I needed to handle different units and convert them to the same unit before adding.

## 3. Fake It, Triangulate, and Obvious Implementation
I used Fake It by returning a fixed value first. I used Triangulate by adding more tests to find the correct implementation. I used Obvious Implementation for simple methods like `times()`. These choices helped me write the code step by step.

## 4. Test List
All planned tests are complete. I would test more unit conversions in the future. I would remove tests that are not needed or are based only on guesses.

## 5. Quantity.reduce
I probably would not have created `Quantity.reduce()` at first. The tests helped me discover that this method was needed to convert quantities between units.

## 6. Part 0 versus Part A
In Part 0, I wrote tests after the code, so the tests checked the existing implementation. In Part A, I wrote tests first, which helped me find problems early and guided my design.
