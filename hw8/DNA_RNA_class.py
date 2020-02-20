class RNA:
    def __init__(self, rna_sequence):
        self.rna_sequence = rna_sequence.upper()
        for i in self.rna_sequence:
            if i == 'T':
                print('It is not RNA')
                self.rna_sequence = ''
                break


class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def gc_content(self):
        count = 0
        for i in self.sequence:
            if i == 'G' or i == 'C':
                count = count + 1
        print('GC content:', count * 100 / len(self.sequence), '%')

    def reverse_complement(self):
        rev_seq = ''
        for i in self.sequence:
            if i == 'G':
                rev_seq = rev_seq + 'C'
            elif i == 'C':
                rev_seq = rev_seq + 'G'
            elif i == 'A':
                rev_seq = rev_seq + 'T'
            elif i == 'T':
                rev_seq = rev_seq + 'A'
            else:
                print('It is not DNA sequence')
                rev_seq = ''
                break
        # print('Reverse complement:', rev_seq)
        return DNA(rev_seq)

    def trascribe(self):
        tr_seq = ''
        for i in self.sequence:
            if i == 'T':
                tr_seq = tr_seq + 'U'
            elif i == 'A' or i == 'C' or i == 'G':
                tr_seq = tr_seq + i
            else:
                print('It can not be transcribed')
                rev_seq = ''
                break
        return RNA(tr_seq)


# return rev_seq
dna_seq = DNA('ATGC')
dna_seq.gc_content()
print('Reverse complement:', dna_seq.reverse_complement().sequence)
print('Transcription', dna_seq.trascribe().rna_sequence)
