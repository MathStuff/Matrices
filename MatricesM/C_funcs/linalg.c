#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

// /*
//Functions
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
//MEMORY LEAKING FUNCTION
static PyObject* Ctranspose(PyObject* self, PyObject* args)
{ 
  int row,col;
  PyObject* list;
  if (!PyArg_ParseTuple(args, "iiO", &row, &col, &list))
      return NULL;

  Py_ssize_t r = row;
  Py_ssize_t c = col;
  int i;
  int j;
  PyObject *arr = PyList_New(c);

  for (i=0; i < col; i++) {
    PyObject *colPointer = PyList_New(r);
    for(j=0;j < row; j++){
      //Possible errors here ?
      PyList_SET_ITEM(colPointer, j, PyList_GET_ITEM(PyList_GET_ITEM(list,j), i));
    }
    PyList_SET_ITEM(arr, i, colPointer);
  }
  /*
  Py_BuildValue is causing memory leak.
  If arr is returned as a Py_Object* "Segmentation Error" occures
  */
  PyObject* result = Py_BuildValue("O",arr); 
                                                                                     
  return result;

}

//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
//List of all functions
static PyMethodDef allMethods[] = {
  {"Ctranspose", Ctranspose, METH_VARARGS, "Transpose a matrix"},
  {NULL,NULL,0,NULL}
};

//Create the module
static struct PyModuleDef linalg = {
  PyModuleDef_HEAD_INIT,
  "linalg",
  "Linear algebra methods for matrices",
  -1,
  allMethods
};

//Return the module
PyMODINIT_FUNC PyInit_linalg(void)
{
  return PyModule_Create(&linalg);
}
// */
