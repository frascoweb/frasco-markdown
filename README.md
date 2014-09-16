# Frasco-Markdown

Provides markdown support to your application using [markdown](https://pypi.python.org/pypi/Markdown).
Adds a `markdown_to_html` action and support for *.md* files as views.

Feature name: *markdown*

## Markdown views

Files with the ".md" extension and a YAML front-matter in the views folder will be
considered as view. They will be rendered to html. A *layout* option can be added
in the front-matter. It must be a filename to a jinja layout with a *content*
block. The block name can be changed using *layout_block* in the front-matter.

    ---
    url: /about
    layout: layout.html
    ---
    # About the team

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada sollicitudin
    quam, sed laoreet ipsum eleifend vitae. Nulla lobortis neque ac imperdiet blandit.
    Curabitur euismod placerat mi. Ut ut scelerisque enim, at aliquet ligula. Integer
    egestas turpis sed ullamcorper venenatis. In tincidunt luctus libero quis blandit.
    Donec non venenatis justo. Aliquam non augue ut dui volutpat feugiat.

## The *markdown_to_html* action

You can convert any markdown text to html using the *markdown_to_html* action.

Options, either:

 - *var*: a variable name containing markdown text which will be converted to html (default)

or:

 - *md*: markdown text to be converted

When using *md*, the action returns the html content.  
Any other options will be forwarded to the `markdown.markdown()` function.

## Jinja helpers

This features introduces a `{{ markdown }}{{ endmarkdown }}` block and a `markdown` filter
to convert markdown to html in your templates. All keyword arguments will be forwarded to
the `markdown.markdown()` function.

    {% markdown safe_mode="replace" %}
        my markdown
    {% endmarkdown %}

    {{ my_markdown_var|markdown(safe_mode="replace") }}

## Conversion options

These feature options control the way html is generated:

 - *extensions*: a dict where key names are extension names and values there config (as defined by *extension_config* in the markdown package)
 - *output_format*: the output html format (default html5) (see *output_format* in the markdown package)
 - *safe_mode*: how to handle embedded html (default False) (see *safe_mode* in the markdown package)
 - *html_replacement_text*: the text to use when *safe_mode* is *replace* (see *html_replacement_text* in the python package)