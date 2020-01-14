#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'tk')


# In[10]:


x = [0, 2, 4, 6]
y = [1, 3, 4, 8]


plt.plot(x,y)


plt.xlabel('x values')
plt.ylabel('y values')
plt.title('plotted x and y values')
plt.legend(['line 1'])


plt.savefig('C:/Users/alina/Documents/Python Scripts/plot.png', dpi=300, bbox_inches='tight')


plt.show()


# In[ ]:




