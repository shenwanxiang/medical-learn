#https://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.Probit.html




from statsmodels.discrete.discrete_model import Probit
p = Probit(df.child.map({'yes':1, 'no':0}), df[['age']])
a = p.fit()
a.summary2()