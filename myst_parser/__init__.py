__version__ = "0.8.1"


def setup(app):
    """Initialize Sphinx extension."""
    from myst_parser.sphinx_parser import MystParser
    from myst_parser.nested_refs import NestedReferenceReslover

    app.add_source_suffix(".md", "markdown")
    app.add_source_parser(MystParser)
    app.add_config_value("myst_config", {}, "env")
    app.add_post_transform(NestedReferenceReslover)

    return {"version": __version__, "parallel_read_safe": True}
