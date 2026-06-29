class PsilocybinError(Exception):
    """Base package error."""


class WorkspaceError(PsilocybinError):
    """Raised when workspace discovery or creation fails."""


class ValidationFailure(PsilocybinError):
    """Raised when validation blocks an operation."""


class LLMError(PsilocybinError):
    """Raised when optional LLM assistance fails."""
