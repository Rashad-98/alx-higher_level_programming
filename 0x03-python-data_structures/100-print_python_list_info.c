#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to PyObject 'structure'
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list;
	long int size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		list = (PyListObject *)PyList_GetItem(p, i);
	printf("Element %d: %s\n", i, list->ob_base.ob_base.ob_type->tp_name);
	}
}
