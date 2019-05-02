#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <Python.h>

//Symmetrical matrix
static PyObject* symzerone(PyObject* self, PyObject* args)
{ 
  int dim;
  
  if (!PyArg_ParseTuple(args, "i", &dim))
    return NULL;

  srand((unsigned int)time(NULL));

  Py_ssize_t d = dim;
  int i,j;
  PyObject *arr = PyList_New(d);

  for(i=0;i < dim; i++) {
    PyList_SET_ITEM(arr, i, PyList_New(d));
  }
  for(i=0;i < dim; i++) {
    //Unique diagonal
    PyList_SET_ITEM(PyList_GET_ITEM(arr,i), i, PyFloat_FromDouble((double)rand()/RAND_MAX));
    for(j=i+1;j < dim; j++){
      double num = (double)rand()/RAND_MAX;
      //Repeat the same number for arr[i,j] and arr[j,i]
      PyList_SET_ITEM(PyList_GET_ITEM(arr,i), j, PyFloat_FromDouble(num));
      PyList_SET_ITEM(PyList_GET_ITEM(arr,j), i, PyFloat_FromDouble(num));
    }
  }
  
  return arr;

}

//List all functions
static PyMethodDef allMethods[] = {
  {"symzerone", symzerone, METH_VARARGS, "Symmetrically filled 2D array"},
  {NULL,NULL,0,NULL}
};

//Create a module
static struct PyModuleDef constructors = {
  PyModuleDef_HEAD_INIT,
  "constructors",
  "Symmetrically fill a 2D list with float numbers ranged from 0 to 1",
  -1,
  allMethods
};

//Return the module
PyMODINIT_FUNC PyInit_constructors(void)
{
  return PyModule_Create(&constructors);
}
// */
