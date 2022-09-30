// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from arm_interfaces:msg/SixFloats.idl
// generated code does not contain a copyright notice

#ifndef ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__BUILDER_HPP_
#define ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__BUILDER_HPP_

#include "arm_interfaces/msg/detail/six_floats__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace arm_interfaces
{

namespace msg
{

namespace builder
{

class Init_SixFloats_m5
{
public:
  explicit Init_SixFloats_m5(::arm_interfaces::msg::SixFloats & msg)
  : msg_(msg)
  {}
  ::arm_interfaces::msg::SixFloats m5(::arm_interfaces::msg::SixFloats::_m5_type arg)
  {
    msg_.m5 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::arm_interfaces::msg::SixFloats msg_;
};

class Init_SixFloats_m4
{
public:
  explicit Init_SixFloats_m4(::arm_interfaces::msg::SixFloats & msg)
  : msg_(msg)
  {}
  Init_SixFloats_m5 m4(::arm_interfaces::msg::SixFloats::_m4_type arg)
  {
    msg_.m4 = std::move(arg);
    return Init_SixFloats_m5(msg_);
  }

private:
  ::arm_interfaces::msg::SixFloats msg_;
};

class Init_SixFloats_m3
{
public:
  explicit Init_SixFloats_m3(::arm_interfaces::msg::SixFloats & msg)
  : msg_(msg)
  {}
  Init_SixFloats_m4 m3(::arm_interfaces::msg::SixFloats::_m3_type arg)
  {
    msg_.m3 = std::move(arg);
    return Init_SixFloats_m4(msg_);
  }

private:
  ::arm_interfaces::msg::SixFloats msg_;
};

class Init_SixFloats_m2
{
public:
  explicit Init_SixFloats_m2(::arm_interfaces::msg::SixFloats & msg)
  : msg_(msg)
  {}
  Init_SixFloats_m3 m2(::arm_interfaces::msg::SixFloats::_m2_type arg)
  {
    msg_.m2 = std::move(arg);
    return Init_SixFloats_m3(msg_);
  }

private:
  ::arm_interfaces::msg::SixFloats msg_;
};

class Init_SixFloats_m1
{
public:
  explicit Init_SixFloats_m1(::arm_interfaces::msg::SixFloats & msg)
  : msg_(msg)
  {}
  Init_SixFloats_m2 m1(::arm_interfaces::msg::SixFloats::_m1_type arg)
  {
    msg_.m1 = std::move(arg);
    return Init_SixFloats_m2(msg_);
  }

private:
  ::arm_interfaces::msg::SixFloats msg_;
};

class Init_SixFloats_m0
{
public:
  Init_SixFloats_m0()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SixFloats_m1 m0(::arm_interfaces::msg::SixFloats::_m0_type arg)
  {
    msg_.m0 = std::move(arg);
    return Init_SixFloats_m1(msg_);
  }

private:
  ::arm_interfaces::msg::SixFloats msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::arm_interfaces::msg::SixFloats>()
{
  return arm_interfaces::msg::builder::Init_SixFloats_m0();
}

}  // namespace arm_interfaces

#endif  // ARM_INTERFACES__MSG__DETAIL__SIX_FLOATS__BUILDER_HPP_
