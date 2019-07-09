import numpy as np
from xml.etree.ElementTree import Element
from napari.layers import Vectors


def test_random_vectors():
    """Test instantiating Vectors layer with random coordinate-like 2D data."""
    shape = (10, 2, 2)
    data = np.random.random(shape)
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    assert np.all(layer.data == data)
    assert layer.data.shape == shape
    assert layer.ndim == shape[2]
    assert layer._data_view.shape[2] == 2


def test_random_vectors_image():
    """Test instantiating Vectors layer with random image-like 2D data."""
    shape = (20, 10, 2)
    data = np.random.random(shape)
    layer = Vectors(data)
    assert layer.data.shape == (20 * 10, 2, 2)
    assert layer.ndim == 2
    assert layer._data_view.shape[2] == 2


def test_empty_vectors():
    """Test instantiating Vectors layer with empty coordinate-like 2D data."""
    shape = (0, 2, 2)
    data = np.empty(shape)
    layer = Vectors(data)
    assert np.all(layer.data == data)
    assert layer.data.shape == shape
    assert layer.ndim == shape[2]
    assert layer._data_view.shape[2] == 2


def test_random_3D_vectors():
    """Test instantiating Vectors layer with random coordinate-like 3D data."""
    shape = (10, 2, 3)
    data = np.random.random(shape)
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    assert np.all(layer.data == data)
    assert layer.data.shape == shape
    assert layer.ndim == shape[2]
    assert layer._data_view.shape[2] == 2


def test_random_3D_vectors_image():
    """Test instantiating Vectors layer with random image-like 3D data."""
    shape = (12, 20, 10, 3)
    data = np.random.random(shape)
    layer = Vectors(data)
    assert layer.data.shape == (12 * 20 * 10, 2, 3)
    assert layer.ndim == 3
    assert layer._data_view.shape[2] == 2


def test_empty_3D_vectors():
    """Test instantiating Vectors layer with empty coordinate-like 3D data."""
    shape = (0, 2, 3)
    data = np.empty(shape)
    layer = Vectors(data)
    assert np.all(layer.data == data)
    assert layer.data.shape == shape
    assert layer.ndim == shape[2]
    assert layer._data_view.shape[2] == 2


def test_changing_data():
    """Test changing Vectors data."""
    shape_a = (10, 2, 2)
    data_a = np.random.random(shape_a)
    data_a[:, 0, :] = 20 * data_a[:, 0, :]
    shape_b = (16, 2, 2)
    data_b = np.random.random(shape_b)
    data_b[:, 0, :] = 20 * data_b[:, 0, :]
    layer = Vectors(data_b)
    layer.data = data_b
    assert np.all(layer.data == data_b)
    assert layer.data.shape == shape_b
    assert layer.ndim == shape_b[2]
    assert layer._data_view.shape[2] == 2


def test_name():
    """Test setting layer name."""
    data = np.random.random((10, 2, 2))
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    assert layer.name == 'Vectors'

    layer = Vectors(data, name='random')
    assert layer.name == 'random'

    layer.name = 'vcts'
    assert layer.name == 'vcts'


def test_edge_width():
    """Test setting edge width."""
    data = np.random.random((10, 2, 2))
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    assert layer.edge_width == 1

    layer.edge_width = 2
    assert layer.edge_width == 2

    layer = Vectors(data, edge_width=3)
    assert layer.edge_width == 3


def test_edge_color():
    """Test setting edge color."""
    data = np.random.random((10, 2, 2))
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    assert layer.edge_color == 'red'

    layer.edge_color = 'blue'
    assert layer.edge_color == 'blue'

    layer = Vectors(data, edge_color='green')
    assert layer.edge_color == 'green'


def test_length():
    """Test setting length."""
    data = np.random.random((10, 2, 2))
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    assert layer.length == 1

    layer.length = 2
    assert layer.length == 2

    layer = Vectors(data, length=3)
    assert layer.length == 3


def test_thumbnail():
    """Test the image thumbnail for square data."""
    data = np.random.random((10, 2, 2))
    data[:, 0, :] = 18 * data[:, 0, :] + 1
    data[0, :, :] = [0, 0]
    data[-1, 0, :] = [20, 20]
    data[-1, 1, :] = [0, 0]
    layer = Vectors(data)
    layer._update_thumbnail()
    assert layer.thumbnail.shape == layer._thumbnail_shape


def test_xml_list():
    """Test the xml generation."""
    data = np.random.random((10, 2, 2))
    data[:, 0, :] = 20 * data[:, 0, :]
    layer = Vectors(data)
    xml = layer.to_xml_list()
    assert type(xml) == list
    assert len(xml) == 10
    assert np.all([type(x) == Element for x in xml])
