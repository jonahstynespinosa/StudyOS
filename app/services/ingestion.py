from markdownify import markdownify 

def split_into_sections(text: str) -> list[str]:
    sections = text.split("\n\n")
    re.complie(r'')
    return [markdownify(section) for section in sections if section.strip()]