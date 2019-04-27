#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Python.h>

//Actual method to return values
static PyObject* pyfill(PyObject* self, PyObject* args)
{ 
  int row,col;
  
  if (!PyArg_ParseTuple(args, "ii", &row,&col))
    return NULL;

  srand((unsigned int)time(NULL));

  Py_ssize_t r = row;
  Py_ssize_t c = col;
  int i;
  int j;
  PyObject *arr = PyList_New(r);

  for(i=0;i < row; i++) {
    PyObject *item = PyList_New(c);
    for(j=0;j < col; j++){
      PyList_SET_ITEM(item, j, PyFloat_FromDouble((double)rand()/RAND_MAX));
    }
    PyList_SET_ITEM(arr, i, item);
  }
  
  return arr;

}

//List all functions
static PyMethodDef allMethods[] = {
  {"pyfill", pyfill, METH_VARARGS, "Filled 2D array"},
  {NULL,NULL,0,NULL}
};

//Create a module
static struct PyModuleDef fillModule = {
  PyModuleDef_HEAD_INIT,
  "fillModule",
  "Filling a 2D array randomly",
  -1,
  allMethods
};

//Return the module
PyMODINIT_FUNC PyInit_fillModule(void)
{
  return PyModule_Create(&fillModule);
}
// */
