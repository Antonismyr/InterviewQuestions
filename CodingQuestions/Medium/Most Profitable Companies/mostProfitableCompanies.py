# Import your libraries
import pandas as pd

# Start writing code
biggestProfits = forbes_global_2010_2014[['company', 'profits']].sort_values(by='profits', ascending=False).head(3)