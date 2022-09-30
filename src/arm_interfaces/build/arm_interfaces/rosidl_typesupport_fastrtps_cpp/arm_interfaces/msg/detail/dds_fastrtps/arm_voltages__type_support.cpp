// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from arm_interfaces:msg/ArmVoltages.idl
// generated code does not contain a copyright notice
#include "arm_interfaces/msg/detail/arm_voltages__rosidl_typesupport_fastrtps_cpp.hpp"
#include "arm_interfaces/msg/detail/arm_voltages__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace arm_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_arm_interfaces
cdr_serialize(
  const arm_interfaces::msg::ArmVoltages & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: m0
  cdr << ros_message.m0;
  // Member: m1
  cdr << ros_message.m1;
  // Member: m2
  cdr << ros_message.m2;
  // Member: m3
  cdr << ros_message.m3;
  // Member: m4
  cdr << ros_message.m4;
  // Member: m5
  cdr << ros_message.m5;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_arm_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  arm_interfaces::msg::ArmVoltages & ros_message)
{
  // Member: m0
  cdr >> ros_message.m0;

  // Member: m1
  cdr >> ros_message.m1;

  // Member: m2
  cdr >> ros_message.m2;

  // Member: m3
  cdr >> ros_message.m3;

  // Member: m4
  cdr >> ros_message.m4;

  // Member: m5
  cdr >> ros_message.m5;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_arm_interfaces
get_serialized_size(
  const arm_interfaces::msg::ArmVoltages & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: m0
  {
    size_t item_size = sizeof(ros_message.m0);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: m1
  {
    size_t item_size = sizeof(ros_message.m1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: m2
  {
    size_t item_size = sizeof(ros_message.m2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: m3
  {
    size_t item_size = sizeof(ros_message.m3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: m4
  {
    size_t item_size = sizeof(ros_message.m4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: m5
  {
    size_t item_size = sizeof(ros_message.m5);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_arm_interfaces
max_serialized_size_ArmVoltages(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: m0
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: m1
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: m2
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: m3
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: m4
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: m5
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _ArmVoltages__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const arm_interfaces::msg::ArmVoltages *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ArmVoltages__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<arm_interfaces::msg::ArmVoltages *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ArmVoltages__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const arm_interfaces::msg::ArmVoltages *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ArmVoltages__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ArmVoltages(full_bounded, 0);
}

static message_type_support_callbacks_t _ArmVoltages__callbacks = {
  "arm_interfaces::msg",
  "ArmVoltages",
  _ArmVoltages__cdr_serialize,
  _ArmVoltages__cdr_deserialize,
  _ArmVoltages__get_serialized_size,
  _ArmVoltages__max_serialized_size
};

static rosidl_message_type_support_t _ArmVoltages__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ArmVoltages__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace arm_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_arm_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<arm_interfaces::msg::ArmVoltages>()
{
  return &arm_interfaces::msg::typesupport_fastrtps_cpp::_ArmVoltages__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, arm_interfaces, msg, ArmVoltages)() {
  return &arm_interfaces::msg::typesupport_fastrtps_cpp::_ArmVoltages__handle;
}

#ifdef __cplusplus
}
#endif
