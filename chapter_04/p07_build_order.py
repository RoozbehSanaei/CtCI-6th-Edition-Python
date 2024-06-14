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

import pytest




'''
The determine_build_order function computes a build order for projects with dependencies:
    
    Initialize Dependency Mapping: 
        Creates a mapping for each project to track its dependencies.

    Setup for Build Sequence: 
        Establishes a list to hold the build sequence and a set of all projects yet to be built.

    Process Dependencies: 
        Fills in the dependency mapping with the provided project-dependency pairs.

    Build Order Logic:
        Repeatedly iterates over the projects yet to be built.
        In each iteration, it checks for projects whose dependencies are already built.
        Projects with all dependencies built are added to the build sequence and removed from the set of projects yet to be built.

    Handle Impossible Build Order: If in any iteration no project can be built (indicating a deadlock like a circular dependency), an error indicating no valid build order is raised.

    Finalize Build Order: Returns the complete build sequence once all projects are successfully added.
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
