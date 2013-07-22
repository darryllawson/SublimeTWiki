# SublimeTWiki

[TWiki](http://twiki.org/) and [Foswiki](http://foswiki.org/) markup editing package for [Sublime Text](http://sublimetext.com/) 2 and 3.

## Why do I want this?

TWiki and Foswiki have you editing wiki pages in a HTML text area or a web based WYSIWYG editor, but to avoid frustration, and to maximise your productivity, wouldn't you rather be using your awesome Sublime Text editor?

## What exactly does this provide?

- Syntax highlighting of the TWiki/Foswiki markup language.
- Heading navigation via Command-R (OS X) and Control-R (Windows and Linux).
- Some basic snippets and auto-completion.

## Installation

To install this package, you have three options:

1. Use [Sublime Package Control](http://wbond.net/sublime_packages/package_control) to install the *TWiki* package. This is your best option.
2. Use git to clone the repository. For example, on OS X: <br> `git clone git://github.com/darryllawson/SublimeTWiki.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/TWiki`
3. Download a zip of the repository from https://github.com/darryllawson/SublimeTWiki/archive/master.zip, and extract that as a directory named TWiki in your Sublime Text Packages directory.

## Syntax highlighting

**Scopes names**

The language definition for TWiki markup relies on the `markup.*` family of scope names. Unfortunately, those scope names are not well supported by the color schemes distributed with Sublime Text, even though they are part of the [TextMate scope naming conventions](http://manual.macromates.com/en/language_grammars#naming_conventions.html). If TWiki syntax highlighting doesn't appear to be working for you, then you may need to modify your color scheme; perhaps consider the _Monokai for Markup_ color theme distributed with this package (see below for details), or the theme distributed with the [MarkdownEditing](https://github.com/ttscoff/MarkdownEditing) package.

**Monokai for Markup color scheme**

A _Monokai for Markup_ color theme is distributed with this package. It is a modified version of the standard _Monokai_ theme, with support for the `markup.*` family of scope names.

## Browser integration tips

**It's All Text! Firefox Add-on**

If you use Firefox, you can use the [It's All Text!](https://addons.mozilla.org/en-US/firefox/addon/its-all-text/) add-on to edit HTML text areas with Sublime Text. To configure it:

1. Right click in a text area in Firefox, and select It's All Text > Preferences.
2. Set the Editor field to the path of your Sublime Text executable.
3. Add `.twiki` to the front of the File Extensions list (which is comma separated).

**QuickCursor (on OS X)**

If you use Safari, Chrome or any other browser on OS X, you can use [QuickCursor](http://www.hogbaysoftware.com/products/quickcursor) to edit HTML text areas (any text actually) with Sublime Text. To configure it, open its Preferences and add a Custom Bundle ID of `com.sublimetext.2`. I also configure an Option-Command-E global short-cut.

**Text Editor Anywhere (on Windows)**

If you use Chrome, Internet Explorer or any other browser on Windows, you can use [Text Editor Anywhere](http://www.listary.com/text-editor-anywhere) to edit HTML text areas (any text actually) with Sublime Text. To configure it:

1. Open Options from the system tray icon.
2. Add a new `twiki` extension and set the associated editor to `C:\Program Files\Sublime Text 2\sublime_text.exe`.
3. Move the new `twiki` extension entry to the top of the list.

## Known issues

- Minor: &lt;verbatim&gt;, &lt;/verbatim&gt;, &lt;/pre&gt; and &lt;/literal&gt; tags can not span multiple lines.
- Minor: only a single attribute in a &lt;verbatim&gt; tag is highlighted.

## Contributing

This project is hosted at https://github.com/darryllawson/SublimeTWiki/.
Please report issues at https://github.com/darryllawson/SublimeTWiki/issues/.

## Acknowledgements

Ideas and code from the [twiki.tmbundle](https://github.com/textmate/twiki.tmbundle) and [gedit-twiki](https://github.com/darryllawson/gedit-twiki) projects were used. Thanks to all involved.

## License

Copyright (C) 2013 Darryl Lawson &lt;darryl.lawson@me.com&gt; <br>
Licensed under the MIT License: http://opensource.org/licenses/mit-license.php
