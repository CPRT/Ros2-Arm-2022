// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from arm_interfaces:msg/LiveTune.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__TRAITS_HPP_
#define ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "arm_interfaces/msg/detail/live_tune__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace arm_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const LiveTune & msg,
  std::ostream & out)
{
  out << "{";
  // member: arm_motor_number
  {
    out << "arm_motor_number: ";
    rosidl_generator_traits::value_to_yaml(msg.arm_motor_number, out);
    out << ", ";
  }

  // member: command
  {
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << ", ";
  }

  // member: value
  {
    out << "value: ";
    rosidl_generator_traits::value_to_yaml(msg.value, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LiveTune & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: arm_motor_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "arm_motor_number: ";
    rosidl_generator_traits::value_to_yaml(msg.arm_motor_number, out);
    out << "\n";
  }

  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << "\n";
  }

  // member: value
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "value: ";
    rosidl_generator_traits::value_to_yaml(msg.value, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LiveTune & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace arm_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use arm_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const arm_interfaces::msg::LiveTune & msg,
  std::ostream & out, size_t indentation = 0)
{
  arm_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use arm_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const arm_interfaces::msg::LiveTune & msg)
{
  return arm_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<arm_interfaces::msg::LiveTune>()
{
  return "arm_interfaces::msg::LiveTune";
}

template<>
inline const char * name<arm_interfaces::msg::LiveTune>()
{
  return "arm_interfaces/msg/LiveTune";
}

template<>
struct has_fixed_size<arm_interfaces::msg::LiveTune>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<arm_interfaces::msg::LiveTune>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<arm_interfaces::msg::LiveTune>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ARM_INTERFACES__MSG__DETAIL__LIVE_TUNE__TRAITS_HPP_
