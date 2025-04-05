import re

def format_gemini_response(text: str) -> str:
    """Format Gemini response from markdown-ish to structured HTML."""

    # Escape leading/trailing whitespace
    text = text.strip()

    # Split into lines and organize into paragraphs/lists
    lines = text.splitlines()
    formatted_lines = []
    in_ol = in_ul = False

    for line in lines:
        line = line.strip()

        # Skip empty lines but close lists if needed
        if not line:
            if in_ol:
                formatted_lines.append("</ol>")
                in_ol = False
            elif in_ul:
                formatted_lines.append("</ul>")
                in_ul = False
            continue

        # Ordered list detection (e.g., "1. Something")
        if re.match(r'^\d+\.\s+', line):
            if not in_ol:
                if in_ul:
                    formatted_lines.append("</ul>")
                    in_ul = False
                formatted_lines.append("<ol>")
                in_ol = True
            content = re.sub(r'^\d+\.\s+', '', line)
            formatted_lines.append(f"<li>{markdown_to_html(content)}</li>")
        # Unordered list detection (e.g., "- something" or "* something")
        elif re.match(r'^[-*]\s+', line):
            if not in_ul:
                if in_ol:
                    formatted_lines.append("</ol>")
                    in_ol = False
                formatted_lines.append("<ul>")
                in_ul = True
            content = re.sub(r'^[-*]\s+', '', line)
            formatted_lines.append(f"<li>{markdown_to_html(content)}</li>")
        else:
            # Normal paragraph
            if in_ol:
                formatted_lines.append("</ol>")
                in_ol = False
            if in_ul:
                formatted_lines.append("</ul>")
                in_ul = False
            formatted_lines.append(f"<p>{markdown_to_html(line)}</p>")

    # Close open list tags
    if in_ol:
        formatted_lines.append("</ol>")
    if in_ul:
        formatted_lines.append("</ul>")

    return "\n".join(formatted_lines)


def markdown_to_html(text: str) -> str:
    """Convert markdown-style bold/italic to HTML-safe formatting."""
    # Bold: **text**
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic: *text*
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Inline code or others can be added here
    return text
