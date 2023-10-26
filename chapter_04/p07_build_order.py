import pytest

'''
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
'''


'''
Initializing a dependency tree and a list to hold the build order.
Populating the dependency tree from the given dependencies.
Iteratively adding to the build list any project whose dependencies are already built, marking it as "built" by removing it from the unbuilt set.
If it ever can't build a new project in an iteration, it raises an error.
'''

def determine_build_order(projects, dependencies):
    dependency_tree = {p: set() for p in projects}
    build_order = []
    unbuilt_projects = set(projects)
    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)

    while unbuilt_projects:
        something_built = False
        for project in list(unbuilt_projects):
            dependencies = dependency_tree[project]
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                unbuilt_projects.remove(project)
                something_built = True
        if not something_built:
            raise NoValidBuildOrderError("No valid build order exists")

    return build_order


class NoValidBuildOrderError(Exception):
    pass


def test_determine_build_order():
    projects = ["a", "b", "c", "d", "e", "f", "g"]
    dependencies = [
        ("d", "g"),
        ("a", "e"),
        ("b", "e"),
        ("c", "a"),
        ("f", "a"),
        ("b", "a"),
        ("f", "c"),
        ("f", "b"),
    ]
    build_order = determine_build_order(projects, dependencies)
    for dependency, project in dependencies:
        assert build_order.index(dependency) < build_order.index(project)


def test_impossible_build_order():
    projects = ["a", "b"]
    dependencies = [("a", "b"), ("b", "a")]
    with pytest.raises(NoValidBuildOrderError):
        determine_build_order(projects, dependencies)
