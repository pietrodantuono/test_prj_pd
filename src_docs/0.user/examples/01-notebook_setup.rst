.. _1. Py-fatigue notebook setup:

1. Set up a notebook running *test_prj_pd*
=========================================

.. important::

    If we are in a development environment, we must set up a notebook that is
    able to recognize the development path as a project.

    To do so, we have to create a new notebook in the `test_prj_pd/notebooks`
    folder and add the following code block in the first cell.

Therefore, if you are working in a package template development enviromment, each of the
following examples in 

`Jupyter Notebooks <https://docs.jupyter.org/en/latest/>`_ and use the
following as cell #1:

.. code-block:: python
    :linenos:

    # Standard imports
    import sys
    import os

    PROJECT_PATH = os.path.dirname(os.getcwd())
    print(f'PROJECT_PATH = {PROJECT_PATH}')

    if not PROJECT_PATH in sys.path:
        sys.path.append(PROJECT_PATH)

    # Use the package
    from test_prj_pd.version import parse_version, __version__
    v = parse_version(__version__)

Optionally, we can add some matplotlib tweaking:

.. code-block:: python
    :linenos:

    plt.rcParams['figure.figsize'] = (7, 3.5)
    plt.rcParams["font.family"] = "Serif"
    plt.rcParams["font.size"] = 10.5
    plt.rcParams["axes.grid"] = True
    plt.rcParams['grid.color'] = "#DDDDDD"
    plt.rcParams['grid.linestyle'] = "-"
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['lines.markersize'] = 3
    plt.rcParams['xtick.bottom'] = False
    plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['ytick.left'] = False
    plt.rcParams['ytick.labelleft'] = True
