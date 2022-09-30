// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/live_tune__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

bool
arm_interfaces__msg__LiveTune__init(arm_interfaces__msg__LiveTune * msg)
{
  if (!msg) {
    return false;
  }
  // arm_motor_number
  // command
  if (!rosidl_runtime_c__String__init(&msg->command)) {
    arm_interfaces__msg__LiveTune__fini(msg);
    return false;
  }
  // value
  return true;
}

void
arm_interfaces__msg__LiveTune__fini(arm_interfaces__msg__LiveTune * msg)
{
  if (!msg) {
    return;
  }
  // arm_motor_number
  // command
  rosidl_runtime_c__String__fini(&msg->command);
  // value
}

arm_interfaces__msg__LiveTune *
arm_interfaces__msg__LiveTune__create()
{
  arm_interfaces__msg__LiveTune * msg = (arm_interfaces__msg__LiveTune *)malloc(sizeof(arm_interfaces__msg__LiveTune));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__msg__LiveTune));
  bool success = arm_interfaces__msg__LiveTune__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__msg__LiveTune__destroy(arm_interfaces__msg__LiveTune * msg)
{
  if (msg) {
    arm_interfaces__msg__LiveTune__fini(msg);
  }
  free(msg);
}


bool
arm_interfaces__msg__LiveTune__Sequence__init(arm_interfaces__msg__LiveTune__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  arm_interfaces__msg__LiveTune * data = NULL;
  if (size) {
    data = (arm_interfaces__msg__LiveTune *)calloc(size, sizeof(arm_interfaces__msg__LiveTune));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = arm_interfaces__msg__LiveTune__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        arm_interfaces__msg__LiveTune__fini(&data[i - 1]);
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
arm_interfaces__msg__LiveTune__Sequence__fini(arm_interfaces__msg__LiveTune__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      arm_interfaces__msg__LiveTune__fini(&array->data[i]);
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

arm_interfaces__msg__LiveTune__Sequence *
arm_interfaces__msg__LiveTune__Sequence__create(size_t size)
{
  arm_interfaces__msg__LiveTune__Sequence * array = (arm_interfaces__msg__LiveTune__Sequence *)malloc(sizeof(arm_interfaces__msg__LiveTune__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__msg__LiveTune__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
arm_interfaces__msg__LiveTune__Sequence__destroy(arm_interfaces__msg__LiveTune__Sequence * array)
{
  if (array) {
    arm_interfaces__msg__LiveTune__Sequence__fini(array);
  }
  free(array);
}
