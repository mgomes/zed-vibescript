use zed_extension_api::{self as zed, Result};

struct VibescriptExtension;

impl zed::Extension for VibescriptExtension {
    fn new() -> Self {
        Self
    }

    fn language_server_command(
        &mut self,
        _language_server_id: &zed::LanguageServerId,
        worktree: &zed::Worktree,
    ) -> Result<zed::Command> {
        let vibes_path = worktree
            .which("vibes")
            .ok_or("Rust vibes binary not found in PATH; install with cargo install --git https://github.com/xipkit/vibescript --tag v0.80.0 vibes")?;
        Ok(zed::Command {
            command: vibes_path,
            args: vec!["lsp".into()],
            env: Default::default(),
        })
    }
}

zed::register_extension!(VibescriptExtension);
