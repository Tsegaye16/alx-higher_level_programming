#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
/**
 * print_python_list_info- function that Prints some basic info about Python lists.
 * @p_o: PyObject
 */

void print_python_list_info(__attribute__((unused)) PyObject *p_o)
{
	int n;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p_o));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p_o)->allocated);

	for (n = 0; n < Py_SIZE(p_o); n++)
	{
		printf("Element %d: %s\n", n, Py_TYPE(PyList_GetItem(p_o, n))->tp_name);
	}
}
