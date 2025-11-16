# Cargo Hyperlink Files

Just a quick lazily written script to read cargo's compiler output and replace any instances of file paths with hyperlinked ones to make it easier to navigate between your terminal and text editor.

Caveats:
- Depends on colour output with the default colours. 
- For now output isn't buffered and compiler output is ingested to completion before being spat back out

I recommend adding an alias for cargo to point to this
`alias cargo=<path/to/>cargo_highlight.py`

commands passed to the script are passed back to cargo, so you call it like
`cargo_highlight.py build`