# Vibescript extension for Zed

Adds [Vibescript](https://github.com/xipkit/vibescript) language support to [Zed](https://zed.dev), including syntax highlighting and LSP integration.

## Features

- Syntax highlighting
- Diagnostics
- Hover information
- Completions

## Prerequisites

Supports the Rust implementation of Vibescript v0.80.0. Install its CLI and
language server with:

```sh
cargo install --git https://github.com/xipkit/vibescript --tag v0.80.0 vibes
```

Add Cargo's bin directory (`~/.cargo/bin` by default) to your editor's `PATH`.
The server command remains `vibes lsp`. Replace any path to the retired Go binary.

## Development

To install as a dev extension, open Zed and run:

```
zed: Install Dev Extension
```

Then select this repo's directory.

The grammar pin tracks tree-sitter-vibescript 0.80.0. Vendored queries cover the
Rust language's static types, aliases, enums and brace blocks, including locals,
indentation, folding and outlines.

Validate a local grammar checkout with `python3 scripts/check-queries.py
/path/to/tree-sitter-vibescript` after running `npm ci` there. Build the extension
with `CARGO_BUILD_JOBS=3 cargo build --target wasm32-wasip1`.
