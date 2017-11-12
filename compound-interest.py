import plotly
import plotly.graph_objs as go


def maths(initial, interestrate, years, compoundsperyear):
    result = initial*((1+((interestrate/100)/compoundsperyear))**(years*compoundsperyear))
    return result


# plotting
def plot():
    xlist = []
    scenario1YList = []
    scenario2YList = []
    scenario3YList = []
    scenario4YList = []
    scenario5YList = []
    scenario6YList = []
    scenario7YList = []
    scenario8YList = []

    for s in range(0, 61):
        xlist.append(s)
        # Scenario 1
        result = maths(initial = 10000, interestrate=7, years=s, compoundsperyear=12)
        scenario1YList.append(result)
        # Scenario 2
        result = maths(initial=10000, interestrate=4, years=s, compoundsperyear=12)
        scenario2YList.append(result)
        # Scenario 3
        result = maths(initial=25000, interestrate=7, years=s, compoundsperyear=12)
        scenario3YList.append(result)
        # Scenario 4
        result = maths(initial=25000, interestrate=4, years=s, compoundsperyear=12)
        scenario4YList.append(result)
        # Scenario 5
        result = maths(initial=10000, interestrate=7, years=s, compoundsperyear=1)
        scenario5YList.append(result)
        # Scenario 6
        result = maths(initial=10000, interestrate=4, years=s, compoundsperyear=1)
        scenario6YList.append(result)
        # Scenario 7
        result = maths(initial=25000, interestrate=7, years=s, compoundsperyear=1)
        scenario7YList.append(result)
        # Scenario 8
        result = maths(initial=25000, interestrate=4, years=s, compoundsperyear=1)
        scenario8YList.append(result)

    trace0 = go.Scatter(
        x=xlist,
        y=scenario1YList,
        name='Scenario 1',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4)
    )
    trace1 = go.Scatter(
        x=xlist,
        y=scenario2YList,
        name='Scenario 2',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4)
    )
    trace2 = go.Scatter(
        x=xlist,
        y=scenario3YList,
        name='Scenario 3',
        line=dict(
            color=('rgb(0, 168, 107)'),
            width=4)
    )
    trace3 = go.Scatter(
        x=xlist,
        y=scenario4YList,
        name='Scenario 4',
        line=dict(
            color=('rgb(255, 165, 0)'),
            width=4)
    )
    trace4 = go.Scatter(
        x=xlist,
        y=scenario5YList,
        name='Scenario 5',
        line=dict(
            color=('rgb(205, 82, 24)'),
            width=4)
    )
    trace5 = go.Scatter(
        x=xlist,
        y=scenario6YList,
        name='Scenario 6',
        line=dict(
            color=('rgb(22, 166, 167)'),
            width=4)
    )
    trace6 = go.Scatter(
        x=xlist,
        y=scenario7YList,
        name='Scenario 7',
        line=dict(
            color=('rgb(0, 238, 107)'),
            width=4)
    )
    trace7 = go.Scatter(
        x=xlist,
        y=scenario8YList,
        name='Scenario 8',
        line=dict(
            color=('rgb(255, 235, 0)'),
            width=4)
    )

    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7]

    # Edit the layout
    layout = dict(title='Compound Interest Modelling',
                  xaxis=dict(title='# years'),
                  yaxis=dict(title='Balance £'),
                  )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='styled-line')


plot()
