// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:msg/SixFloats.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/six_floats__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
arm_interfaces__msg__SixFloats__init(arm_interfaces__msg__SixFloats * msg)
{
  if (!msg) {
    return false;
  }
  // m0
  // m1
  // m2
  // m3
  // m4
  // m5
  return true;
}

void
arm_interfaces__msg__SixFloats__fini(arm_interfaces__msg__SixFloats * msg)
{
  if (!msg) {
    return;
  }
  // m0
  // m1
  // m2
  // m3
  // m4
  // m5
}

arm_interfaces__msg__SixFloats *
arm_interfaces__msg__SixFloats__create()
{
  arm_interfaces__msg__SixFloats * msg = (arm_interfaces__msg__SixFloats *)malloc(sizeof(arm_interfaces__msg__SixFloats));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__msg__SixFloats));
  bool success = arm_interfaces__msg__SixFloats__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__msg__SixFloats__destroy(arm_interfaces__msg__SixFloats * msg)
{
  if (msg) {
    arm_interfaces__msg__SixFloats__fini(msg);
  }
  free(msg);
}


bool
arm_interfaces__msg__SixFloats__Sequence__init(arm_interfaces__msg__SixFloats__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  arm_interfaces__msg__SixFloats * data = NULL;
  if (size) {
    data = (arm_interfaces__msg__SixFloats *)calloc(size, sizeof(arm_interfaces__msg__SixFloats));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__msg__SixFloats__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__msg__SixFloats__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
arm_interfaces__msg__SixFloats__Sequence__fini(arm_interfaces__msg__SixFloats__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      arm_interfaces__msg__SixFloats__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

arm_interfaces__msg__SixFloats__Sequence *
arm_interfaces__msg__SixFloats__Sequence__create(size_t size)
{
  arm_interfaces__msg__SixFloats__Sequence * array = (arm_interfaces__msg__SixFloats__Sequence *)malloc(sizeof(arm_interfaces__msg__SixFloats__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__msg__SixFloats__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
arm_interfaces__msg__SixFloats__Sequence__destroy(arm_interfaces__msg__SixFloats__Sequence * array)
{
  if (array) {
    arm_interfaces__msg__SixFloats__Sequence__fini(array);
  }
  free(array);
}
