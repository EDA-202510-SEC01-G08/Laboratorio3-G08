"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 """

import csv
import os

from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as lt
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_logic():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {
        'books': None,
        'authors': None,
        'tags': None,
        'book_tags': None
    }

    catalog['books'] = lt.new_list()
    catalog['authors'] = lt.new_list()
    catalog['tags'] = lt.new_list()
    catalog['book_tags'] = lt.new_list
    return catalog


# Funciones para la carga de datos


def load_data(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    books, authors = load_books(catalog)
    load_books(catalog)
    load_tags(catalog)
    load_books_tags(catalog)
    return books, authors



def load_books(catalog):
    """
    Carga los libros del archivo. Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = data_dir + 'GoodReads/books-medium.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for book in input_file:
        add_book(catalog, book)
    return book_size(catalog), author_size(catalog)


def load_tags(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags

    :param catalog: El catalogo de estructuras del laboratorio

    :return: El número de tags cargados
    """
    tagsfile = data_dir + 'GoodReads/tags.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        add_tag(catalog, tag)
    return tag_size(catalog)  
    


def load_books_tags(catalog):
    """
    Carga la información que asocia tags con libros.

    :param catalog: El catalogo de estructuras del laboratorio

    :return: El número de book_tags cargados
    """
    book_tagsfile = data_dir + 'GoodReads/book_tags.csv'
    input_file = csv.DictReader(open(book_tagsfile, encoding='utf-8'))
    for book_tag in input_file:
        add_book_tag(catalog, book_tag)
    return book_tag_size(catalog)

# Funciones de consulta sobre el catálogo

def get_books_by_author(catalog, author_name):
    """
    Retrona los libros de un autor
    """
    pos_author = lt.is_present(
        catalog['authors'], author_name, compare_authors)
    if pos_author > 0:
        author = lt.get_element(catalog['authors'], pos_author)
        return author
    return None


def get_best_book(catalog):
    
    mejor = lt.first_element(catalog['books'])
    current = lt.first_node(catalog['books'])
    while current is not None:
        book = lt.get_element(catalog['books'], current)
        if compare_ratings(book, mejor):
            mejor = book
        current = lt.next_node(catalog['books'], current)
    return mejor


def count_books_by_tag(catalog, tag):
    
    tag_id = lt.first_node(catalog['tags'])
    count = 0
    while tag_id is not None:
        tag = lt.get_element(catalog['tags'], tag_id)
        tag_id = lt.next_node(catalog['tags'], tag_id)
        count += 1
    return count


# Funciones para agregar informacion al catalogo

def add_book(catalog, book):
    # Se adiciona el libro a la lista de libros
    lt.add_last(catalog['books'], book)
    # Se obtienen los autores del libro
    authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        add_book_author(catalog, author.strip(), book)
    return catalog


def add_book_author(catalog, author_name, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    pos_author = lt.is_present(authors, author_name, compare_authors)
    if pos_author > 0:
        author = lt.get_element(authors, pos_author)
    else:
        author = new_author(author_name)
        lt.add_last(authors, author)
    lt.add_last(author['books'], book)
    return catalog


def add_tag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = new_tag(tag['tag_name'], tag['tag_id'])
    lt.add_last(catalog['tags'], t)
    return catalog


def add_book_tag(catalog, book_tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = new_book_tag(book_tag['tag_id'], book_tag['goodreads_book_id'])
    lt.add_last(catalog['book_tags'], t)
    return catalog


# Funciones para creacion de datos

def new_author(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.new_list()
    return author


def new_tag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def new_book_tag(tag_id, book_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    book_tag = {'tag_id': tag_id, 'book_id': book_id}
    return book_tag


def book_size(catalog):
    return lt.size(catalog['books'])


def author_size(catalog):
    
    return lt.size(catalog['authors'])


def tag_size(catalog):
    
    return lt.size(catalog['tags'])



def book_tag_size(catalog):
    
    return lt.size(catalog['book_tags'])


# Funciones utilizadas para comparar elementos dentro de una lista


def compare_authors(author_name1, author):
    if author_name1.lower() == author['name'].lower():
        return 0
    elif author_name1.lower() > author['name'].lower():
        return 1
    return -1


def compare_tag_names(name, tag):
    if (name == tag['name']):
        return 0
    elif (name > tag['name']):
        return 1
    return -1


# funciones para comparar elementos dentro de algoritmos de ordenamientos

def compare_ratings(book1, book2):
    return (float(book1['average_rating']) > float(book2['average_rating']))
