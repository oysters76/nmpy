import sys
import numpy as np

from nmpy_tasks.decorators import task_skipper, task


@task("Print the numpy version and the configuration (★☆☆)")
@task_skipper(skip=True)
def task2():
    print("np version:", np.__version__)
    np.show_config()


@task("Create a null vector of size 10 (★☆☆)")
@task_skipper(skip=True)
def task3():
    v = np.full(10, np.nan)
    print(v)


@task("How to find the memory size of any array (★☆☆)")
@task_skipper(skip=True)
def task4():
    a = np.zeros((10, 10), dtype=np.float32)
    b = np.ones((10, 10), dtype=np.float32)
    c = np.ones((20, 20), dtype=np.int16)

    def memory_view(a):
        print(f"Memory size of the array: {a.nbytes} bytes")
        print(f"\titemsize = {a.itemsize}")
        print(f"\tshape = {a.shape}")
        print(f"\tdtype = {a.dtype}")
        print(f"\tsizeof {sys.getsizeof(a)} bytes (data + python object overhead)")
        print(f"\thuman readable size = {a.nbytes/1024**2:.2f} MB")

    memory_view(a)
    memory_view(b)
    memory_view(c)


@task("How to get the documentation of the numpy add function from the command line? (★☆☆)")
@task_skipper(skip=True)
def task5():
    np.info(np.add)


@task("Create a null vector of size 10 but the fifth value which is 1 (★☆☆)")
@task_skipper(skip=True)
def task6():
    a = np.full(10, np.nan) 
    a[4] = 1 
    print(a) 


@task("Create a vector with values ranging from 10 to 49 (★☆☆)")
@task_skipper(skip=True)
def task7():
    a = np.arange(10, 50)
    print(a)


@task("Reverse a vector (first element becomes last) (★☆☆)")
@task_skipper(skip=False)
def task8():
    a = np.arange(10)
    print(a) 
    a = np.flip(a)
    print(a) 


@task("Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)")
@task_skipper(skip=False)
def task9():
    a = np.arange(0,9).reshape(3,3)
    print(a)


@task("Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)")
@task_skipper(skip=False)
def task10():
    a = np.array([1,2,0,0,4,0]) 
    print(np.nonzero(a))
    print(a[np.nonzero(a)])


@task("Create a 3x3 identity matrix (★☆☆)")
@task_skipper(skip=False)
def task11():
    print(np.identity(3))


@task("Create a 3x3x3 array with random values (★☆☆)")
@task_skipper(skip=False)
def task12():
    import secrets 
    key = secrets.randbits(128) 
    rng = np.random.default_rng(key) 
    print(rng.random((3,3,3))) 



@task("Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)")
@task_skipper(skip=False)
def task13():
    import secrets 
    key = secrets.randbits(128) 
    rng = np.random.default_rng(key) 
    A = np.matrix(rng.random((10, 10)) * 100)
    print(A) 
    print(np.max(A)) 
    print(np.min(A))

@task("Create a random vector of size 30 and find the mean value (★☆☆)")
@task_skipper(skip=False)
def task14():
    a = np.arange(20,20+30)
    print(np.mean(a))


@task("Create a 2d array with 1 on the border and 0 inside (★☆☆)")
@task_skipper(skip=False)
def task15():
    a = np.zeros((5,5)) 
    a[0, 0:5] = 1
    a[4, 0:5] = 1
    a[0:5, 0] = 1
    a[0:5, 4] = 1
    print(a)


@task("How to add a border (filled with 0's) around an existing array? (★☆☆)")
@task_skipper(skip=False)
def task16():
    A = np.zeros((2, 2)) 
    A = np.pad(A, 1, constant_values=69)
    print(A)


@task("What is the result of the following expression? (★☆☆)")
@task_skipper(skip=False)
def task17():
    """
        ```python
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1

key learnings:
Two core lessons:

1. **NaN is toxic and never equal to anything, including itself.
** Any arithmetic with `nan` produces `nan`, and any comparison returns `False`.
 That's why `nan == nan` is `False` and `inf > nan` is `False`. The one exception:
   Python's `set`/`in` uses identity (`is`) before equality, and since `np.nan` is a singleton, 
   `nan in set([nan])` is `True`.

2. **Floating point can't represent 0.1 exactly.** `3 * 0.1` is `0.30000000000000004`, not `0.3`. 
Use `np.isclose()` or `math.isclose()` instead of `==` for float comparison.
```
    """
    exprs = [
        ("0 * np.nan",             0 * np.nan),
        ("np.nan == np.nan",       np.nan == np.nan),
        ("np.inf > np.nan",        np.inf > np.nan),
        ("np.nan - np.nan",        np.nan - np.nan),
        ("np.nan in set([np.nan])", np.nan in set([np.nan])),
        ("0.3 == 3 * 0.1",        0.3 == 3 * 0.1),
    ]
    for label, result in exprs:
        print(f"{label:<30} {result}")


@task("Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)")
@task_skipper(skip=False)
def task18():
    A = np.identity(5) 
    print(A)
    A_flat = np.diagflat([1,2,3,4],-1) 
    A_new = A + A_flat
    print(A_new)

    answer = np.diag([1,2,3,4], k=-1)
    print(answer)


@task("Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)")
@task_skipper(skip=False)
def task19():
    checkboard = np.zeros((8,8), dtype=int)
    checkboard[0:8:2, 0:8:2] = 1  # start at 0, till 8, step by 2 for both row,col
    checkboard[1:8:2, 1:8:2] = 1 # start at 1 (odd), till 8, step by 2 (odds) for both row,col
    print(checkboard)


@task("Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)")
@task_skipper(skip=False)
def task20():
    a = np.arange(6*7*8).reshape((6,7,8))
    r = a.ravel() 
    print(r[99])
    print(np.unravel_index(99, a.shape))
    ind = np.unravel_index(99, a.shape)
    print(f"Index of the 100th element: {ind}")
    print(f"Value at that index: {a[ind]}")


@task("Create a checkerboard 8x8 matrix using the tile function (★☆☆)")
@task_skipper(skip=False)
def task21():
    even = np.tile(np.array([1,0]), (1,4)) 
    odd = np.tile(np.array([0,1]), (1,4))
    segment = np.vstack((even, odd))
    checkboard = np.tile(segment, (4,1))
    print(checkboard)

    # simple one 
    ck = np.tile(np.identity(2), (4,4))
    assert np.array_equal(checkboard, ck), "Checkerboard matrices do not match!"


@task("Normalize a 5x5 random matrix (★☆☆)")
@task_skipper(skip=False)
def task22():
    # euclidean norm per row L2 
    m = np.round(np.random.rand(5,5),2) # rounded to two decimal places
    print(m)
    print("euclidean norm per row L2")
    m_norm = m/np.linalg.norm(m, axis=1, keepdims=True) 
    print(m_norm)

    # min-max norm 
    print("min-max norm")
    m_norm = (m-m.min())/(m.max()-m.min()) 
    print(m_norm)

    #z-score norm 
    print("z-score norm")
    m_norm = (m-m.mean())/m.std() 
    print(m_norm)

@task("Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)")
@task_skipper(skip=False)
def task23():
    my_color = np.dtype([
        ('r', np.ubyte),
        ('g', np.ubyte),
        ('b', np.ubyte),
        ('a', np.ubyte)
    ]) 

    colors = np.array([(255, 0, 0, 255), (69, 255, 0, 255), (0, 0, 255, 255)], dtype=my_color)
    print(colors)
    print(colors['r'])  # Access the red channel


@task("Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)")
@task_skipper(skip=False)
def task24():
    A = np.ones((5,3)) 
    M = -1 * np.ones((3,2))

    print(A,"\n", M)
    product = np.matmul(A, M)
    print(product)

    product_shorthand = A @ M 
    assert np.array_equal(product, product_shorthand)  # Should be True

@task("Given a 1D array, negate all elements which are between 3 and 8, in place (★☆☆)")
@task_skipper(skip=False)
def task25():
    n = np.arange(2,18)
    # if n is between 3 and 8, true: negate, else n but where create a new array
    where_n = np.where((n >= 3) & (n <= 8), -n, n)
    # so use inplace index way 
    n[(n >= 3) & (n <= 8)] *= -1
    print(n)
    assert np.array_equal(n,where_n), "In-place negation did not match expected result" 

@task("What is the output of the following script? (★☆☆)")
@task_skipper(skip=False)
def task26():
    """
    print(sum(range(5),-1))
    from numpy import *
    print(sum(range(5),-1))

    prints 9 
    prints 10

    key learnings:
    - Built-in sum(iterable, start): the 2nd arg is the start value → -1 + 10 = 9
    - np.sum(a, axis): the 2nd arg is the axis; axis=-1 = last axis → 10
    - `from numpy import *` silently shadows Python built-ins
      (sum, min, max, abs, round, all, any, ...) and changes their behaviour.
    - Avoid wildcard imports: use `import numpy as np` and call np.sum explicitly.
    """
    sn = sum(range(5), -1) # Python built-in sum: start=-1 → 0+1+2+3+4-1 = 9 
    nn = np.sum(np.arange(5), -1) # NumPy sum: axis=-1 → sum over last axis of 1D array → 0+1+2+3+4 = 10
    print(f"Python built-in sum(range(5), -1) = {sn}")
    print(f"NumPy sum(range(5), -1) = {nn}")


@task("Consider an integer vector Z, which of these expressions are legal? (★☆☆)")
@task_skipper(skip=False)
def task27():
    """
    key learnings:
    - Z**Z: each element to the power of itself (5^5, 6^6, etc.)
    - 2 << Z >> 2: bitwise shift left then right, works on int arrays
    - Z <- Z: python reads this as Z < (-Z), not assignment! all False
    - 1j*Z: complex numbers, 1j is python's imaginary literal
    - Z/1/1: dividing by 1 twice, just converts int to float
    - Z<Z>Z: illegal, python can't chain < > with numpy arrays
    - takeaway: numpy overloads almost every python operator to work element-wise
    """
    Z = np.arange(5,10) 
    exprs = [
        ("Z**Z", Z**Z),
        ("2 << Z >> 2", 2 << Z >> 2), 
        ("Z <- Z", Z <- Z),
        ("1j*Z", 1j*Z),
        ("Z/1/1", Z/1/1),
        ("Z<Z>Z", "Illegal syntax"),
    ]
    for label, result in exprs:
        print(f"{label:<40} {result}")


@task("What are the result of the following expressions? (★☆☆)")
@task_skipper(skip=False)
def task28():
    """
    key learnings:
    - 0/0 gives nan (not an error), numpy warns but doesn't crash
    - 0//0 (floor division) gives 0, also warns
    - nan cast to int gives an undefined garbage value, casting back to float keeps that garbage
    - takeaway: numpy silently handles bad math with nan/0 instead of raising exceptions,
      so you have to check for these yourself
    """
    exprs = [
        ("np.array(0) / np.array(0)", np.array(0) / np.array(0)),
        ("np.array(0) // np.array(0)", np.array(0) // np.array(0)),
        ("np.array([np.nan]).astype(int).astype(float)", np.array([np.nan]).astype(int).astype(float)),
    ]
    for label, result in exprs:
        print(f"{label:<40} {result}")


@task("How to round away from zero a float array? (★☆☆)")
@task_skipper(skip=False)
def task29():
    f = np.random.rand(5) * 10 - 5  # random floats in [-5,5)
    f_dash = np.where(np.sign(f) == 1, np.ceil(f), np.floor(f))
    print(f"Original array: {f}")
    print(f"Rounded away from zero: {f_dash}")

    # copysign approach: abs removes sign, ceil rounds up, copysign puts the sign back
    # np.sign(0) returns 0 not 1, but floor(0)==ceil(0)==0 so it doesn't matter
    f_ = np.copysign(np.ceil(np.abs(f)), f)

    assert np.array_equal(f_dash, f_), "Both rounding methods should produce the same result"

@task("How to find common values between two arrays? (★☆☆)")
@task_skipper(skip=False)
def task30():
    f1 = np.arange(5,10) 
    f2 = np.arange(8,12) 

    f1f2, f1_inds, f2_inds = np.intersect1d(f1, f2, return_indices=True)
    print(f1f2)
    print(f1_inds)
    print(f2_inds)


@task("How to ignore all numpy warnings (not recommended)? (★☆☆)")
@task_skipper(skip=False)
def task31():
    """
    key learnings:
    - np.errstate: context manager, suppresses warnings only inside the block (best option)
      options: 'ignore', 'warn', 'raise', 'call', 'print', 'log'
      categories: divide, over, under, invalid
    - warnings.filterwarnings('ignore'): suppresses ALL python warnings globally (nuclear option)
    - np.seterr(all='ignore'): suppresses all numpy warnings globally until changed back
    - always prefer np.errstate because it's scoped — warnings come back after the block
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.array([1,0,-1]) / 0 # no warnings 
        print(result)


@task("Is the following expressions true? (★☆☆)")
@task_skipper(skip=False)
def task32():
    """
    key learnings:
    - np.sqrt(-1) returns nan and a warning — it only works with real numbers
    - np.emath.sqrt(-1) returns 1j (complex) — it handles negative inputs properly
    - so np.sqrt(-1) == np.emath.sqrt(-1) is False (nan != 1j)
    - the assert passes because nan != anything is always True (even nan != nan)
    - use np.emath (extended math) when you need complex results from sqrt, log, power
    """
    sq1 = np.sqrt(-1)
    sq2 = np.emath.sqrt(-1)
    print(sq1,sq2)
    assert sq1 != sq2, "np.sqrt(-1) and np.emath.sqrt(-1) should not be equal"


@task("How to get the dates of yesterday, today and tomorrow? (★☆☆)")
@task_skipper(skip=False)
def task33():
    one_day = np.timedelta64(1, 'D')
    today = np.datetime64('today','D') 
    tomorrow = today + one_day
    yesterday = today - one_day
    print("yesterday:", yesterday)
    print("today:", today)
    print("tomorrow:", tomorrow)

@task("How to get all the dates corresponding to the month of July 2016? (★★☆)")
@task_skipper(skip=False)
def task34():
    pass


@task("How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)")
@task_skipper(skip=False)
def task35():
    pass


@task("Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)")
@task_skipper(skip=False)
def task36():
    pass


@task("Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)")
@task_skipper(skip=False)
def task37():
    pass


@task("Consider a generator function that generates 10 integers and use it to build an array (★☆☆)")
@task_skipper(skip=False)
def task38():
    pass


@task("Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)")
@task_skipper(skip=False)
def task39():
    pass


@task("Create a random vector of size 10 and sort it (★★☆)")
@task_skipper(skip=False)
def task40():
    pass


@task("How to sum a small array faster than np.sum? (★★☆)")
@task_skipper(skip=False)
def task41():
    pass


@task("Consider two random arrays A and B, check if they are equal (★★☆)")
@task_skipper(skip=False)
def task42():
    pass


@task("Make an array immutable (read-only) (★★☆)")
@task_skipper(skip=False)
def task43():
    pass


@task("Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)")
@task_skipper(skip=False)
def task44():
    pass


@task("Create random vector of size 10 and replace the maximum value by 0 (★★☆)")
@task_skipper(skip=False)
def task45():
    pass


@task("Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)")
@task_skipper(skip=False)
def task46():
    pass


@task("Given two arrays, X and Y, construct the Cauchy matrix C (Cij=1/(xi-yj)) (★★☆)")
@task_skipper(skip=False)
def task47():
    pass


@task("Print the minimum and maximum representable values for each numpy scalar type (★★☆)")
@task_skipper(skip=False)
def task48():
    pass


@task("How to print all the values of an array? (★★☆)")
@task_skipper(skip=False)
def task49():
    pass


@task("How to find the closest value (to a given scalar) in a vector? (★★☆)")
@task_skipper(skip=False)
def task50():
    pass


@task("Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)")
@task_skipper(skip=False)
def task51():
    pass


@task("Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)")
@task_skipper(skip=False)
def task52():
    pass


@task("How to convert a float (32 bits) array into an integer (32 bits) array in place? (★★☆)")
@task_skipper(skip=False)
def task53():
    pass


@task("How to read the following file? (★★☆)")
@task_skipper(skip=False)
def task54():
    pass


@task("What is the equivalent of enumerate for numpy arrays? (★★☆)")
@task_skipper(skip=False)
def task55():
    pass


@task("Generate a generic 2D Gaussian-like array (★★☆)")
@task_skipper(skip=False)
def task56():
    pass


@task("How to randomly place p elements in a 2D array? (★★☆)")
@task_skipper(skip=False)
def task57():
    pass


@task("Subtract the mean of each row of a matrix (★★☆)")
@task_skipper(skip=False)
def task58():
    pass


@task("How to sort an array by the nth column? (★★☆)")
@task_skipper(skip=False)
def task59():
    pass


@task("How to tell if a given 2D array has null columns? (★★☆)")
@task_skipper(skip=False)
def task60():
    pass


@task("Find the nearest value from a given value in an array (★★☆)")
@task_skipper(skip=False)
def task61():
    pass


@task("Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)")
@task_skipper(skip=False)
def task62():
    pass


@task("Create an array class that has a name attribute (★★☆)")
@task_skipper(skip=False)
def task63():
    pass


@task("Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)")
@task_skipper(skip=False)
def task64():
    pass


@task("How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)")
@task_skipper(skip=False)
def task65():
    pass


@task("Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)")
@task_skipper(skip=False)
def task66():
    pass


@task("Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)")
@task_skipper(skip=False)
def task67():
    pass


@task("Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices? (★★★)")
@task_skipper(skip=False)
def task68():
    pass


@task("How to get the diagonal of a dot product? (★★★)")
@task_skipper(skip=False)
def task69():
    pass


@task("Consider the vector [1,2,3,4,5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)")
@task_skipper(skip=False)
def task70():
    pass


@task("Consider an array of dimension (5,5,3), how to multiply it by an array with dimensions (5,5)? (★★★)")
@task_skipper(skip=False)
def task71():
    pass


@task("How to swap two rows of an array? (★★★)")
@task_skipper(skip=False)
def task72():
    pass


@task("Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the triangles (★★★)")
@task_skipper(skip=False)
def task73():
    pass


@task("Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)")
@task_skipper(skip=False)
def task74():
    pass


@task("How to compute averages using a sliding window over an array? (★★★)")
@task_skipper(skip=False)
def task75():
    pass


@task("Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is shifted by 1 (★★★)")
@task_skipper(skip=False)
def task76():
    pass


@task("How to negate a boolean, or to change the sign of a float inplace? (★★★)")
@task_skipper(skip=False)
def task77():
    pass


@task("Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i? (★★★)")
@task_skipper(skip=False)
def task78():
    pass


@task("Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j to each line i? (★★★)")
@task_skipper(skip=False)
def task79():
    pass


@task("Consider an arbitrary array, write a function that extracts a subpart with a fixed shape and centered on a given element (pad with a fill value when necessary) (★★★)")
@task_skipper(skip=False)
def task80():
    pass


@task("Consider an array Z = [1,2,3,...,14], how to generate an array R = [[1,2,3,4], [2,3,4,5], ..., [11,12,13,14]]? (★★★)")
@task_skipper(skip=False)
def task81():
    pass


@task("Compute a matrix rank (★★★)")
@task_skipper(skip=False)
def task82():
    pass


@task("How to find the most frequent value in an array? (★★★)")
@task_skipper(skip=False)
def task83():
    pass


@task("Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)")
@task_skipper(skip=False)
def task84():
    pass


@task("Create a 2D array subclass such that Z[i,j] == Z[j,i] (★★★)")
@task_skipper(skip=False)
def task85():
    pass


@task("Consider a set of p matrices with shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of the p matrix products at once? (★★★)")
@task_skipper(skip=False)
def task86():
    pass


@task("Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)")
@task_skipper(skip=False)
def task87():
    pass


@task("How to implement the Game of Life using numpy arrays? (★★★)")
@task_skipper(skip=False)
def task88():
    pass


@task("How to get the n largest values of an array (★★★)")
@task_skipper(skip=False)
def task89():
    pass


@task("Given an arbitrary number of vectors, build the cartesian product (every combination of every item) (★★★)")
@task_skipper(skip=False)
def task90():
    pass


@task("How to create a record array from a regular array? (★★★)")
@task_skipper(skip=False)
def task91():
    pass


@task("Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)")
@task_skipper(skip=False)
def task92():
    pass


@task("Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain at least one element of each row of B? (★★★)")
@task_skipper(skip=False)
def task93():
    pass


@task("Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★)")
@task_skipper(skip=False)
def task94():
    pass


@task("Convert a vector of ints into a matrix binary representation (★★★)")
@task_skipper(skip=False)
def task95():
    pass


@task("Given a two dimensional array, how to extract unique rows? (★★★)")
@task_skipper(skip=False)
def task96():
    pass


@task("Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)")
@task_skipper(skip=False)
def task97():
    pass


@task("Considering a path described by two vectors (X,Y), how to sample it using equidistant samples? (★★★)")
@task_skipper(skip=False)
def task98():
    pass


@task("Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees (★★★)")
@task_skipper(skip=False)
def task99():
    pass


@task("Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (★★★)")
@task_skipper(skip=False)
def task100():
    pass
