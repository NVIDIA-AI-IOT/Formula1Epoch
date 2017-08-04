// Auto-generated. Do not edit!

// (in-package vesc_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let VescState = require('./VescState.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class VescStateStamped {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.state = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = new VescState();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VescStateStamped
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [state]
    bufferOffset = VescState.serialize(obj.state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VescStateStamped
    let len;
    let data = new VescStateStamped(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [state]
    data.state = VescState.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 100;
  }

  static datatype() {
    // Returns string type for a message object
    return 'vesc_msgs/VescStateStamped';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3a2b3a0e5b5f10ce6bbf973d767cdc4d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Timestamped VESC open source motor controller state (telemetry)
    
    Header  header
    VescState state
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: vesc_msgs/VescState
    # Vedder VESC open source motor controller state (telemetry)
    
    # fault codes
    int32 FAULT_CODE_NONE=0
    int32 FAULT_CODE_OVER_VOLTAGE=1
    int32 FAULT_CODE_UNDER_VOLTAGE=2
    int32 FAULT_CODE_DRV8302=3
    int32 FAULT_CODE_ABS_OVER_CURRENT=4
    int32 FAULT_CODE_OVER_TEMP_FET=5
    int32 FAULT_CODE_OVER_TEMP_MOTOR=6
    
    float64 voltage_input        # input voltage (volt)
    float64 temperature_pcb      # temperature of printed circuit board (degrees Celsius)
    float64 current_motor        # motor current (ampere)
    float64 current_input        # input current (ampere)
    float64 speed                # motor electrical speed (revolutions per minute) 
    float64 duty_cycle           # duty cycle (0 to 1)
    float64 charge_drawn         # electric charge drawn from input (ampere-hour)
    float64 charge_regen         # electric charge regenerated to input (ampere-hour)
    float64 energy_drawn         # energy drawn from input (watt-hour)
    float64 energy_regen         # energy regenerated to input (watt-hour)
    float64 displacement         # net tachometer (counts)
    float64 distance_traveled    # total tachnometer (counts)
    int32   fault_code
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VescStateStamped(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.state !== undefined) {
      resolved.state = VescState.Resolve(msg.state)
    }
    else {
      resolved.state = new VescState()
    }

    return resolved;
    }
};

module.exports = VescStateStamped;
