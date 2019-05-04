#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Python.h>

//Actual method to return values
static PyObject* pyfill(PyObject* self, PyObject* args)
{ 
  int row,col,seed;
  
  if (!PyArg_ParseTuple(args, "iii", &row,&col,&seed))
    return NULL;

  srand(seed);

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
static struct PyModuleDef zerone = {
  PyModuleDef_HEAD_INIT,
  "zerone",
  "Fill a 2D list with float numbers ranged from 0 to 1",
  -1,
  allMethods
};

//Return the module
PyMODINIT_FUNC PyInit_zerone(void)
{
  return PyModule_Create(&zerone);
}
// */
