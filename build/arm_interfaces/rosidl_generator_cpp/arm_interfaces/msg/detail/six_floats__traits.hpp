// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from arm_interfaces:msg/SixFloats.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__TRAITS_HPP_
#define ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "arm_interfaces/msg/detail/six_floats__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace arm_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const SixFloats & msg,
  std::ostream & out)
{
  out << "{";
  // member: m0
  {
    out << "m0: ";
    rosidl_generator_traits::value_to_yaml(msg.m0, out);
    out << ", ";
  }

  // member: m1
  {
    out << "m1: ";
    rosidl_generator_traits::value_to_yaml(msg.m1, out);
    out << ", ";
  }

  // member: m2
  {
    out << "m2: ";
    rosidl_generator_traits::value_to_yaml(msg.m2, out);
    out << ", ";
  }

  // member: m3
  {
    out << "m3: ";
    rosidl_generator_traits::value_to_yaml(msg.m3, out);
    out << ", ";
  }

  // member: m4
  {
    out << "m4: ";
    rosidl_generator_traits::value_to_yaml(msg.m4, out);
    out << ", ";
  }

  // member: m5
  {
    out << "m5: ";
    rosidl_generator_traits::value_to_yaml(msg.m5, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SixFloats & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: m0
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m0: ";
    rosidl_generator_traits::value_to_yaml(msg.m0, out);
    out << "\n";
  }

  // member: m1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m1: ";
    rosidl_generator_traits::value_to_yaml(msg.m1, out);
    out << "\n";
  }

  // member: m2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m2: ";
    rosidl_generator_traits::value_to_yaml(msg.m2, out);
    out << "\n";
  }

  // member: m3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m3: ";
    rosidl_generator_traits::value_to_yaml(msg.m3, out);
    out << "\n";
  }

  // member: m4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m4: ";
    rosidl_generator_traits::value_to_yaml(msg.m4, out);
    out << "\n";
  }

  // member: m5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "m5: ";
    rosidl_generator_traits::value_to_yaml(msg.m5, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SixFloats & msg, bool use_flow_style = false)
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
  const arm_interfaces::msg::SixFloats & msg,
  std::ostream & out, size_t indentation = 0)
{
  arm_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use arm_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const arm_interfaces::msg::SixFloats & msg)
{
  return arm_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<arm_interfaces::msg::SixFloats>()
{
  return "arm_interfaces::msg::SixFloats";
}

template<>
inline const char * name<arm_interfaces::msg::SixFloats>()
{
  return "arm_interfaces/msg/SixFloats";
}

template<>
struct has_fixed_size<arm_interfaces::msg::SixFloats>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<arm_interfaces::msg::SixFloats>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<arm_interfaces::msg::SixFloats>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__TRAITS_HPP_
