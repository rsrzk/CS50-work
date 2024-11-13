from project import list_txt_files, select_file, change_directory
import pytest

def test_directory_list():
    # project root folder
    assert list_txt_files() == ['requirements.txt']

    # main folder for storing files
    assert list_txt_files('files').sort() == ['employment_agreement_rais.txt', 'employment_agreement.txt', 'rental_agreement.txt', 'services_agreement.txt'].sort()

    # ignore non txt files
    assert list_txt_files('files3').sort() == ['test.txt', 'test2.txt', 'test3.txt'].sort()

    # sub folder
    assert list_txt_files('files3/files2') == ['test5.txt']

def test_invalid_directory():
    with pytest.raises(FileNotFoundError):
        # folder does not exist
        list_txt_files('project/week0')

def test_not_folder():
    with pytest.raises(NotADirectoryError):
        # folder does not exist
        list_txt_files('files/rental_agreement.txt')

def test_select_valid():
    assert select_file(1, ['file1.txt', 'file2.txt'], 'files') == 'files/file1.txt'
    assert select_file(2, ('file2.txt', 'file3.txt'), 'files4') == 'files4/file3.txt'
    assert select_file(3, ['file1.txt', 'file2.txt', 'file3.txt']) == './file3.txt'

def test_select_invalid_blank():
    with pytest.raises(TypeError):
        select_file()

def test_select_invalid_index():
    with pytest.raises(IndexError):
        select_file(3, ['file1.txt', 'file2.txt'], 'files')

def test_select_invalid_index_text():
    with pytest.raises(TypeError):
        select_file('cat', ['file1.txt', 'file2.txt'], 'files')

def test_change():
    assert change_directory('project/week0') == None
    assert change_directory('files/rental_agreement.txt') == None
    assert change_directory('files') == 'files'
    assert change_directory('files3/files2') == 'files3/files2'

def test_change_invalid():
    with pytest.raises(TypeError):
        change_directory()
