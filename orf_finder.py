# Don't change the Libraries
import os
import sys

#Your Code Here

class ORFFinder():
    def __init__(self):
        pass

    def read_fasta_file(self, file_path):  # Implement code to read fasta file and return sequences
        sequences = {}
        with open(file_path, 'r') as file:
            sequence_id = ''
            sequence = ''
            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if sequence_id:
                        sequences[sequence_id] = sequence
                        sequence = ''
                    sequence_id = line[1:]
                else:
                    sequence += line
            if sequence_id and sequence:
                sequences[sequence_id] = sequence
        return sequences

    def find_longest_orf(self, sequence):  # Implement code to find the longest DNA ORF in a given sequence
        start_codon = 'ATG'
        stop_codons = ['TAG', 'TGA', 'TAA']
        longest_orf = ''

        for i in range(len(sequence)):
            if sequence[i:i + 3] == start_codon:
                for j in range(i + 3, len(sequence), 3):
                    codon = sequence[j:j + 3]
                    if codon in stop_codons:
                        current_orf = sequence[i:j + 3]
                        if len(current_orf) > len(longest_orf):
                            longest_orf = current_orf
                        break

        return longest_orf

    def process_sequences(self, file_path): #Implement code to process all sequences and find the overall longest DNA ORF
        sequences = self.read_fasta_file(file_path)
        longest_orfs = self.process_sequences(sequences)
        overall_longest_orf = ''
        for seq_id, longest_orf in longest_orfs.items():
            if len(longest_orf) > len(overall_longest_orf):
                overall_longest_orf = longest_orf
        return overall_longest_orf
    
def main(): # initialize to let various arguments pass
    if len(sys.argv) != 2:
        print("Input fasta file")
        sys.exit(1)

    input_file = sys.argv[1]
    orf_finder = ORFFinder()
    overall_longest_orf = orf_finder.process_sequences(input_file)

    print("Overall Longest ORF:")
    print(overall_longest_orf)

if __name__ == "__main__":
    main()
    
