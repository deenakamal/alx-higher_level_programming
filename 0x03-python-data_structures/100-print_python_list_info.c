#include <Python.h>
/**
 * print_python_list_info - a C function that prints some basic
 * info about Python lists.
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int _s;
	int iterat;
	PyListObject *obj;

	_s = PyList_Size(p);
	obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", _s);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (iterat = 0; iterat < _s; iterat++)
	{
		printf("Element %d: ", iterat);
		printf("%s\n", Py_TYPE(obj->ob_item[iterat])->tp_name);
	}
}
