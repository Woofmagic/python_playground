# Experiment 01: Make a Decimal Wrapper Integrate with NumPy

## Objective:
Find a lightweight method for existing functions designed to handle NumPy arrays of floats or integers to now handle Decimal types. 

## Result:
That got too janky to figure out easily. We would have to refactor thousands of subfunctions.

# Experiment 02: Integrate Existing `Complex` Operations with  

## Objective:
Earlier code utilizes the `.conjugate()` method in a desired way: first, `complex` types are initialized and then passed in whole --- either as they are defined or as conjugated --- as arguments into functions. Now, we need to ensure `complex` types work with `Decimal` types within their initalization.

## Result: