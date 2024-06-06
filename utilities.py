def add_bar_labels(axis) -> None:
    """
    Add bar labels to the plot for each container

    :param axis: The axis to add the labels to
    :return: None
    """

    for cont in axis.containers:
        if cont.datavalues[0] != 0:
            axis.bar_label(cont)
