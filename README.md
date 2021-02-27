## What is this? 🤔

This script will get all the glyphs from the **Fira Code** font and put them into the specified font, they won't overwrite
existing glyphs, only the ones your font are missing.

## How to use 🤷‍♀️

`./fira-attach.py` to attach FiraCode glyphs to all fonts on the same directory as the script (`*.ttf` and `*.otf` only)

`./fira-attach.py <folder>` to attach FiraCode glyphs to all fonts on `<folder>` (`*.ttf` and `*.otf` only)

`./fira-attach.py <font>` to attach FiraCode glyphs to specified `<font>` path (`*.ttf` and `*.otf` only)

## Ideal use 💡

You have your font patched with the [NerdFont](https://github.com/ryanoasis/nerd-fonts) patcher but you are missing some nice
glyphs like the round corners, etc...

## Dependencies 🏁

- Fontforge (see [install instructions](http://designwithfontforge.com/en-US/Installing_Fontforge.html))

## Output 👉

Output font will have the same name as the original with an `- FiraAttached` appended to the file name and will appear
on the `./output` folder relative to the script, real font name is left intact.

Ex: `SourceCodePro.ttf` -> `SourceCodePro - FiraAttached.ttf`

## Key Notes: 🧷

- I didn't test this against an original font that hasn't been patched, I have always tested this against NerdFont patched fonts,
  so it gives me nice results 🙃.

- I think if you patch it to an unpatched font it will inject the NerdFonts glyphs as well but I wouldn't recommend that.
