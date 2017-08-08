# TWiki and Foswiki Support for Sublime Text

A [Sublime Text](http://sublimetext.com/) package for the [TWiki](http://twiki.org/) and [Foswiki](http://foswiki.org/) markup language.

Use this extension in conjunction with a tool such as [Text Editor Anywhere](http://www.listary.com/text-editor-anywhere) (on Windows) or [QuickCursor](https://github.com/jessegrosjean/quickcursor) (on macOS) for wiki page editing bliss.

Files with a `.twiki` or `.foswiki` extension are automatically opened into TWiki/Foswiki language mode.

## What exactly does this package provide?

- Syntax highlighting of the TWiki and Foswiki markup languages.
- Heading navigation via Command-R (OS X) and Control-R (Windows and Linux).
- Some basic snippets and auto-completion.

## Known issues

- `<verbatim>`, `</verbatim>`, `<pre>`, `</pre>`, `<literal>`, and `</literal>` tags that span multiple lines, are not highlighted correctly.
- Only a single attribute in a `<verbatim>` tag is highlighted.
