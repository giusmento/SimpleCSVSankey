import pandas
import plotly
import plotly.graph_objects as go


def genSankey(df, cat_cols=[], title='Sankey Diagram'):

    # group by all selected columns
    value_cols = 'count'
    df[value_cols] = 1
    df = df.groupby(cat_cols, as_index=False).agg({value_cols: 'count'})
    # maximum of 6 value cols -> 6 colors
    colorPalette = ['#4B8BBE', '#306998', '#FFE873', '#FFD43B', '#646464']
    labelList = []
    labelListWithLevel = []
    colorNumList = []
    level = 0
    for catCol in cat_cols:
        labelListTemp = list(set(df[catCol].values))
        colorNumList.append(len(labelListTemp))
        labelListTempLevel = [f'{level}-' + el for el in labelListTemp]
        labelList = labelList + labelListTemp
        labelListWithLevel = labelListWithLevel + labelListTempLevel
        level = level + 1

    # remove duplicates from labelList
    #labelList = list(dict.fromkeys(labelList))

    # define colors based on number of levels
    colorList = []
    for idx, colorNum in enumerate(colorNumList):
        colorList = colorList + [colorPalette[idx]] * colorNum

    # transform df into a source-target pair
    for i in range(len(cat_cols) - 1):
        if i == 0:
            sourceTargetDf = df[[cat_cols[i], cat_cols[i + 1], value_cols]]
            sourceTargetDf[cat_cols[i]] = sourceTargetDf[cat_cols[i]].apply(lambda x: f"{i}-" + x)
            sourceTargetDf[cat_cols[i + 1]] = sourceTargetDf[cat_cols[i + 1]].apply(lambda x: f"{i + 1}-" + x)
            sourceTargetDf.columns = ['source', 'target', 'count']
        else:
            tempDf = df[[cat_cols[i], cat_cols[i + 1], value_cols]]
            tempDf[cat_cols[i]] = tempDf[cat_cols[i]].apply(lambda x: f"{i}-" + x)
            tempDf[cat_cols[i + 1]] = tempDf[cat_cols[i + 1]].apply(lambda x: f"{i + 1}-" + x)
            tempDf.columns = ['source', 'target', 'count']
            sourceTargetDf = pandas.concat([sourceTargetDf, tempDf])
        sourceTargetDf = sourceTargetDf.groupby(['source', 'target']).agg({'count': 'sum'}).reset_index()

    # add index for source-target pair
    sourceTargetDf['sourceID'] = sourceTargetDf['source'].apply(lambda x: labelListWithLevel.index(str(x)))
    sourceTargetDf['targetID'] = sourceTargetDf['target'].apply(lambda x: labelListWithLevel.index(x))

    # creating the sankey diagram
    data = dict(
        type='sankey',
        node=dict(
            pad=15,
            thickness=20,
            line=dict(
                color="black",
                width=0.5
            ),
            label=labelListWithLevel,
            color=colorList
        ),
        link=dict(
            arrowlen=15,
            source=sourceTargetDf['sourceID'],
            target=sourceTargetDf['targetID'],
            value=sourceTargetDf['count']
        )
    )

    layout = dict(
        title=title,
        font=dict(
            size=10
        )
    )

    fig = dict(data=[data], layout=layout)
    return fig
