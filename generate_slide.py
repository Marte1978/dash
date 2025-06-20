import io, sys

content_stream = """BT
/F1 24 Tf
50 750 Td
(\xc2\xbfQuienes somos?) Tj
0 -30 Td
(Somos un movimiento empresarial cuyo objetivo es que sus miembros logren la libertad financiera. Socio comercial: HGW.) Tj
ET"""

pdf_parts = []

pdf_parts.append('%PDF-1.4\n')

offsets = []

# object 1
offsets.append(sum(len(p) for p in pdf_parts))
pdf_parts.append('1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n')

# object 2
offsets.append(sum(len(p) for p in pdf_parts))
pdf_parts.append('2 0 obj\n<< /Type /Pages /Count 1 /Kids [3 0 R] >>\nendobj\n')

# object 3
offsets.append(sum(len(p) for p in pdf_parts))
pdf_parts.append('3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n')

# object 4
offsets.append(sum(len(p) for p in pdf_parts))
pdf_parts.append('4 0 obj\n<< /Length {} >>\nstream\n{}\nendstream\nendobj\n'.format(len(content_stream), content_stream))

# object 5
offsets.append(sum(len(p) for p in pdf_parts))
pdf_parts.append('5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n')

xref_offset = sum(len(p) for p in pdf_parts)

pdf_parts.append('xref\n')
pdf_parts.append('0 6\n')
pdf_parts.append('0000000000 65535 f \n')
for off in offsets:
    pdf_parts.append('{:010d} 00000 n \n'.format(off))

pdf_parts.append('trailer\n')
pdf_parts.append('<< /Root 1 0 R /Size 6 >>\n')
pdf_parts.append('startxref\n')
pdf_parts.append(str(xref_offset) + '\n')
pdf_parts.append('%%EOF\n')

with open('presentation.pdf', 'wb') as f:
    f.write(''.join(pdf_parts).encode('latin1'))

