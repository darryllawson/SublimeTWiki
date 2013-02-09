# SublimeTWiki developer guide

## Design principles

Wiki syntax is good; it is an efficient way to write documents for those inclined to learn it. The aim of SublimeTWiki is to assist the writing of wiki markup, not to try and synthesise a WYSIWYG editor. That is, the aim is to highlight the markup, but not simulate the rendered output of TWiki/Foswiki. For example, *bold* should not necessarily be rendered as bold text, although it may.

Highlighting errors is generally avoided for two reasons: 1) There is not really such a thing as an error in wiki markup; it is just plain text. For example, *bold, may seem like an error (that is, *bold is missing a trailing asterisk), but maybe that is what the user wants. 2) The flashing red error highlighting as you type, which is what some language definitions do, can be annoying and distracting.

## Scope naming

- I have attempted to conform to the TextMate scope naming conventions defined [here](http://manual.macromates.com/en/language_grammars).

- I have tried to be consistent with the built-in Markdown and HTML syntax definitions, although, my approach differs in that I make use of the `keyword.other` scope.

- The `markup.` family of scopes names is used where ever appropriate.

- `keyword.other` is used for markup tokens such as `*` for lists, `|` for tables, `[[` for links, and `---+` for headings. This is because I treat markup tokens as the keywords of a markup language. However, the tokens used to delimit formatted text are *not* considered keywords, `punctuation.definition` is used there (yes, the world is grey).

- `variable.other` is used for variable names.

- `constant.other` is used for anchors.

- All scope names end with `.twiki` as per convention.

- The top-level scope name is `text.html.twiki`, not `text.twiki`, so that the HTML package capabilities, such as snippets and commands, apply to TWiki files.

## AAAPackageDev

[AAAPackageDev](http://bitbucket.org/guillermooo/aaapackagedev) is used to convert the `TWiki.JSON-tmLangauge` file into the `TWiki.tmLanguage` file. The `TWiki.tmLanguage` file is the one actually parsed by Sublime Text.

## Similar projects

- [twiki.tmbundle TextMate bundle](https://github.com/textmate/twiki.tmbundle)
- [emacs-twiki-mode](https://github.com/christopherjwhite/emacs-twiki-mode)
- [AsciiDoc Sublime Text package](https://github.com/SublimeText/AsciiDoc])

## References

- [TWiki Text Formatting Rules](http://twiki.org/cgi-bin/view/TWiki/TextFormattingRules)
- [Foswiki Text Formatting Rules](http://foswiki.org/System/TextFormattingRules)
