"""Personal configuration files for zsh, tmux, neovim and git."""

from __future__ import annotations

__all__ = ["dotfiles"]


def dotfiles(value):
    """Personal configuration files for zsh, tmux, neovim and git."""
    if value is None:
        raise ValueError("value must not be None")
    return value
