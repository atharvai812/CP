def fmt_text(text):
    lines = text.split('\n')
    formatted_lines = []
    current_line = ""
    for line in lines:
        words = line.split()
        for word in words:
            if len(current_line) + len(word) <= 72:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
            else:
                formatted_lines.append(current_line)
                current_line = word
        if current_line:
            formatted_lines.append(current_line)
            current_line = ""
    return "\n".join(formatted_lines)

# Sample Input
input_text = """Unix fmt
The unix fmt program reads lines of text, combining
and breaking lines so as to create an
output file with lines as close to without exceeding
72 characters long as possible. The rules for combining and breaking
lines are as follows.
1. A new line may be started anywhere there is a space in the input.
If a new line is started, there will be no trailing blanks at the
end of the previous line or at the beginning of the new line.
2. A line break in the input may be eliminated in the output, provided
it is not followed by a space or another line break. If a line
break is eliminated, it is replaced by a space."""

# Output
output_text = fmt_text(input_text)
print(output_text)
