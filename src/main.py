#This is the main code you have to run.
#Don't forget to create an enmpty text file and to update all the paths !

import get_caracters as gc
import create_Huffman_tree as ht
import text_decoding as td
import get_compression_rate as cr
import paths as p



def create_huffman_tree (alphabet_file_path, compressed_file_path) :
    alphabet_file = open(p.alphabet_file_path, 'r')
    lines_of_file = alphabet_file.readlines()

    alphabet_dictionnary = gc.create_alphabet_dictionary(lines_of_file)[0]
    huffman_tree = ht.create_Huffman_tree(ht.create_all_trees(alphabet_dictionnary))

    return(huffman_tree)


def get_final_text (alphabet_file_path, compressed_file_path) :
    tree = create_huffman_tree(p.alphabet_file_path, p.compressed_file_path)

    binary_code = td.get_binary_code(p.compressed_file_path)
    texte_final = td.translate_binary_code(binary_code, tree)
    return(tree, binary_code, texte_final)


def get_efficiency (alphabet_file_path, compressed_file_path, path) :
    tree, binary_code, texte_final = get_final_text(p.alphabet_file_path, p.compressed_file_path)
    message = td.translate_binary_code(binary_code, tree)
    size = cr.get_file_size(p.compressed_file_path)
    nb_caracters = len(message) - 2
    print("The compressed file contains " + str(nb_caracters/size) + " caracters/bytes.")
    print("The compression rate is " + str(round(size/nb_caracters*100, 2)), '%.')
    return size/nb_caracters


def get_decompressed_file (alphabet_file_path, compressed_file_path, path) :
    tree, binary_code, texte_final = get_final_text(p.alphabet_file_path, p.compressed_file_path)
    message = td.translate_binary_code(binary_code, tree)
    new_file = open(path, "w")
    new_file.write(message)
    new_file.close()

def run_the_whole_programm () :
    print(" ")
    get_efficiency(p.alphabet_file_path, p.compressed_file_path, p.decompressed_file_path)
    print(" ")
    get_decompressed_file(p.alphabet_file_path, p.compressed_file_path, p.decompressed_file_path)

run_the_whole_programm()

