// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from arm_interfaces:msg/SixFloats.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__FUNCTIONS_H_
#define ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "arm_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "arm_interfaces/msg/detail/six_floats__struct.h"

/// Initialize msg/SixFloats message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * arm_interfaces__msg__SixFloats
 * )) before or use
 * arm_interfaces__msg__SixFloats__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
bool
arm_interfaces__msg__SixFloats__init(arm_interfaces__msg__SixFloats * msg);

/// Finalize msg/SixFloats message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
void
arm_interfaces__msg__SixFloats__fini(arm_interfaces__msg__SixFloats * msg);

/// Create msg/SixFloats message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * arm_interfaces__msg__SixFloats__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
arm_interfaces__msg__SixFloats *
arm_interfaces__msg__SixFloats__create();

/// Destroy msg/SixFloats message.
/**
 * It calls
 * arm_interfaces__msg__SixFloats__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
void
arm_interfaces__msg__SixFloats__destroy(arm_interfaces__msg__SixFloats * msg);


/// Initialize array of msg/SixFloats messages.
/**
 * It allocates the memory for the number of elements and calls
 * arm_interfaces__msg__SixFloats__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
bool
arm_interfaces__msg__SixFloats__Sequence__init(arm_interfaces__msg__SixFloats__Sequence * array, size_t size);

/// Finalize array of msg/SixFloats messages.
/**
 * It calls
 * arm_interfaces__msg__SixFloats__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
void
arm_interfaces__msg__SixFloats__Sequence__fini(arm_interfaces__msg__SixFloats__Sequence * array);

/// Create array of msg/SixFloats messages.
/**
 * It allocates the memory for the array and calls
 * arm_interfaces__msg__SixFloats__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
arm_interfaces__msg__SixFloats__Sequence *
arm_interfaces__msg__SixFloats__Sequence__create(size_t size);

/// Destroy array of msg/SixFloats messages.
/**
 * It calls
 * arm_interfaces__msg__SixFloats__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_arm_interfaces
void
arm_interfaces__msg__SixFloats__Sequence__destroy(arm_interfaces__msg__SixFloats__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__FUNCTIONS_H_
