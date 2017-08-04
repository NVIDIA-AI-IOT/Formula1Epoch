
(cl:in-package :asdf)

(defsystem "vesc_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "VescState" :depends-on ("_package_VescState"))
    (:file "_package_VescState" :depends-on ("_package"))
    (:file "VescStateStamped" :depends-on ("_package_VescStateStamped"))
    (:file "_package_VescStateStamped" :depends-on ("_package"))
  ))