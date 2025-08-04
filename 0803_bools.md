# What is a Boolean?

**Boolean** (sometimes shortened to bool) is a data type that can only have one of two values: `true` or `false`.
(Sometimes we think of `true` as 1 and `false` as 0.)

# What kind of operations can I do to a Boolean?

### NOT

`not` is like the minus sign in math. 

* `not True` -> `False`
* `not False` -> `True`

When we have two `not` together, they cancel out!

* `not (not True)` -> `True`
* `not (not False)` -> `False`

### OR

"Buy me an apple or a mango!" You're good as long as you bring _either or_. (Or you can go the extra mile and bring both!)

Here is the truth table for `A or B`:

`A` | `B` | `A or B`
--- | --- | --------
True | True | True
True | False | True
False | True | True
False | False | False

### OR

"Buy me an apple and a mango!" You **need** to buy both!

Here is the truth table for `A and B`:

`A` | `B` | `A and B`
--- | --- | --------
True | True | True
True | False | False
False | True | False
False | False | False
