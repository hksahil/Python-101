#!/usr/bin/env python
# coding: utf-8

# ## Basic Probability

# ### Random Variables

# - In probability,we calculate the probablity(chances of outcomes)
# - We need to assign a number to each outcome
# - Function which does this is called random variable
# - For example,in below example :
#     - I clicked on any hexagon (click means outcome) and then gave it a number
#     - Repeated it for all the outcomes
#         - We now have random variable

# 
# ![random%20function.PNG](attachment:random%20function.PNG)

# ## Types of Random Variable

# - Discrete Random Variable
#     - A discrete random variable has a finite/countable number of possible values.
#     
#     
# - Continuous Random Variable
#     - A continuous random variable has a infinite/non-countable number of possible values.
# 

# ### Expectation 

# - measure of centrality of variable

# In[ ]:





# ### Variance

# - measure of distribution of random variable
# - The average value of the squared difference between the random variable and its expectation
#     - Var(X)=E[(X−E[X])2]

# ## Compound Probability

# ### Set Theory

# - To specify compound events. 
#     - For example, we can represent the event "roll an even number" by the set {2, 4, 6}
# - Talks about union and intersetion venn diagrams
# - ![sets.PNG](attachment:sets.PNG)

# ### Conditional Probability

# - Probability - Find the probability that it will rain tomorrow
# - Conditional Probability- Find the probability that it will rain tomorrow given that it is a cloudy day
#     - Instead of looking at how often it rains on any day in general, we "pretend" that our sample space consists of only those days for which the previous day was cloudy
#         - Lesser sample space
#     - Conditional probability uses the information we allready have about our system of interest.
#     - Bookish Defination : A conditional probability is the probability of an event, given some other event has already occurred
#     - Formulae : P(A|B)=P(A intersection B)/P(B)
#     - More : https://setosa.io/conditional/
# 
