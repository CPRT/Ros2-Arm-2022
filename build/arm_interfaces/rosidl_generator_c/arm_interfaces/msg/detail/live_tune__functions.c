// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/live_tune__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


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

bool
arm_interfaces__msg__LiveTune__are_equal(const arm_interfaces__msg__LiveTune * lhs, const arm_interfaces__msg__LiveTune * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // arm_motor_number
  if (lhs->arm_motor_number != rhs->arm_motor_number) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->command), &(rhs->command)))
  {
    return false;
  }
  // value
  if (lhs->value != rhs->value) {
    return false;
  }
  return true;
}

bool
arm_interfaces__msg__LiveTune__copy(
  const arm_interfaces__msg__LiveTune * input,
  arm_interfaces__msg__LiveTune * output)
{
  if (!input || !output) {
    return false;
  }
  // arm_motor_number
  output->arm_motor_number = input->arm_motor_number;
  // command
  if (!rosidl_runtime_c__String__copy(
      &(input->command), &(output->command)))
  {
    return false;
  }
  // value
  output->value = input->value;
  return true;
}

arm_interfaces__msg__LiveTune *
arm_interfaces__msg__LiveTune__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__LiveTune * msg = (arm_interfaces__msg__LiveTune *)allocator.allocate(sizeof(arm_interfaces__msg__LiveTune), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(arm_interfaces__msg__LiveTune));
  bool success = arm_interfaces__msg__LiveTune__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
arm_interfaces__msg__LiveTune__destroy(arm_interfaces__msg__LiveTune * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    arm_interfaces__msg__LiveTune__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
arm_interfaces__msg__LiveTune__Sequence__init(arm_interfaces__msg__LiveTune__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__LiveTune * data = NULL;

  if (size) {
    data = (arm_interfaces__msg__LiveTune *)allocator.zero_allocate(size, sizeof(arm_interfaces__msg__LiveTune), allocator.state);
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
      allocator.deallocate(data, allocator.state);
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
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      arm_interfaces__msg__LiveTune__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
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
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  arm_interfaces__msg__LiveTune__Sequence * array = (arm_interfaces__msg__LiveTune__Sequence *)allocator.allocate(sizeof(arm_interfaces__msg__LiveTune__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = arm_interfaces__msg__LiveTune__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
arm_interfaces__msg__LiveTune__Sequence__destroy(arm_interfaces__msg__LiveTune__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    arm_interfaces__msg__LiveTune__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
arm_interfaces__msg__LiveTune__Sequence__are_equal(const arm_interfaces__msg__LiveTune__Sequence * lhs, const arm_interfaces__msg__LiveTune__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!arm_interfaces__msg__LiveTune__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
arm_interfaces__msg__LiveTune__Sequence__copy(
  const arm_interfaces__msg__LiveTune__Sequence * input,
  arm_interfaces__msg__LiveTune__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(arm_interfaces__msg__LiveTune);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    arm_interfaces__msg__LiveTune * data =
      (arm_interfaces__msg__LiveTune *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!arm_interfaces__msg__LiveTune__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          arm_interfaces__msg__LiveTune__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!arm_interfaces__msg__LiveTune__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
