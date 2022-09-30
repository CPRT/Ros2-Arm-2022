// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from arm_interfaces:msg/SixFloats.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__TRAITS_HPP_
#define ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__TRAITS_HPP_

#include "arm_interfaces/msg/detail/six_floats__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

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
