classDiagram
direction BT
class auth_group {
   varchar(150) name
   int(11) id
}
class auth_group_permissions {
   int(11) group_id
   int(11) permission_id
   bigint(20) id
}
class auth_permission {
   varchar(255) name
   int(11) content_type_id
   varchar(100) codename
   int(11) id
}
class auth_user {
   varchar(128) password
   datetime(6) last_login
   tinyint(1) is_superuser
   varchar(150) username
   varchar(150) first_name
   varchar(150) last_name
   varchar(254) email
   tinyint(1) is_staff
   tinyint(1) is_active
   datetime(6) date_joined
   int(11) id
}
class auth_user_groups {
   int(11) user_id
   int(11) group_id
   bigint(20) id
}
class auth_user_user_permissions {
   int(11) user_id
   int(11) permission_id
   bigint(20) id
}
class django_admin_log {
   datetime(6) action_time
   longtext object_id
   varchar(200) object_repr
   smallint(5) unsigned action_flag
   longtext change_message
   int(11) content_type_id
   int(11) user_id
   int(11) id
}
class django_content_type {
   varchar(100) app_label
   varchar(100) model
   int(11) id
}
class django_migrations {
   varchar(255) app
   varchar(255) name
   datetime(6) applied
   bigint(20) id
}
class django_session {
   longtext session_data
   datetime(6) expire_date
   varchar(40) session_key
}
class game_management_gamefunction {
   varchar(40) game_function
   varchar(255) game_function_description
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_gameinschedule {
   varchar(100) game_type_name
   varchar(255) master_nickname
   time(6) time_begin
   time(6) time_end
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   bigint(20) game_result_id
   bigint(20) game_type_id
   bigint(20) master_id
   bigint(20) schedule_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_gameresult {
   varchar(100) game_result
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   bigint(20) game_type_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_gametype {
   varchar(100) game_name
   varchar(255) game_description
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_location {
   varchar(100) location_name
   varchar(255) location_address
   varchar(255) Location_directions
   varchar(255) location_point
   varchar(100) location_photo
   varchar(100) direction_photo
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_member {
   int(11) tg_id
   varchar(255) tg_name
   date date_birth
   varchar(255) nickname
   tinyint(1) photo
   varchar(100) photo_file
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   bigint(20) game_function_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_memberingame {
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   bigint(20) game_in_schedule_id
   bigint(20) member_id
   bigint(20) member_result_additional_id
   bigint(20) member_result_main_id
   bigint(20) role_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_memberrating {
   date rating_date
   int(11) rating
   bigint(20) game_id
   bigint(20) member_id
   bigint(20) id
}
class game_management_memberresult {
   varchar(100) member_result
   varchar(100) member_result_type
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_memberstatistics {
   date statistic_date
   bigint(20) game_id
   bigint(20) member_id
   bigint(20) result_id
   bigint(20) role_id
   bigint(20) id
}
class game_management_promo {
   varchar(10) par1
   varchar(400) text1
   varchar(10) par2
   varchar(400) text2
   varchar(10) par3
   varchar(400) text3
   varchar(10) par4
   varchar(400) text4
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_registeredtogame {
   varchar(255) comment
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   bigint(20) member_id
   bigint(20) schedule_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_role {
   varchar(40) role
   varchar(255) role_description
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   int(11) update_user_id
   bigint(20) id
}
class game_management_schedule {
   date date
   time(6) schedule_time_begin
   time(6) schedule_time_end
   varchar(255) game_name
   varchar(140) location_name
   tinyint(1) active
   datetime(6) create_time
   datetime(6) update_time
   datetime(6) delete_time
   int(11) create_user_id
   int(11) delete_user_id
   bigint(20) game_id
   bigint(20) location_id
   int(11) update_user_id
   bigint(20) id
}

auth_group_permissions  -->  auth_group : group_id:id
auth_group_permissions  -->  auth_permission : permission_id:id
auth_permission  -->  django_content_type : content_type_id:id
auth_user_groups  -->  auth_group : group_id:id
auth_user_groups  -->  auth_user : user_id:id
auth_user_user_permissions  -->  auth_permission : permission_id:id
auth_user_user_permissions  -->  auth_user : user_id:id
django_admin_log  -->  auth_user : user_id:id
django_admin_log  -->  django_content_type : content_type_id:id
game_management_gamefunction  -->  auth_user : delete_user_id:id
game_management_gamefunction  -->  auth_user : create_user_id:id
game_management_gamefunction  -->  auth_user : update_user_id:id
game_management_gameinschedule  -->  auth_user : delete_user_id:id
game_management_gameinschedule  -->  auth_user : create_user_id:id
game_management_gameinschedule  -->  auth_user : update_user_id:id
game_management_gameinschedule  -->  game_management_gameresult : game_result_id:id
game_management_gameinschedule  -->  game_management_gametype : game_type_id:id
game_management_gameinschedule  -->  game_management_member : master_id:id
game_management_gameinschedule  -->  game_management_schedule : schedule_id:id
game_management_gameresult  -->  auth_user : update_user_id:id
game_management_gameresult  -->  auth_user : create_user_id:id
game_management_gameresult  -->  auth_user : delete_user_id:id
game_management_gameresult  -->  game_management_gametype : game_type_id:id
game_management_gametype  -->  auth_user : delete_user_id:id
game_management_gametype  -->  auth_user : create_user_id:id
game_management_gametype  -->  auth_user : update_user_id:id
game_management_location  -->  auth_user : update_user_id:id
game_management_location  -->  auth_user : create_user_id:id
game_management_location  -->  auth_user : delete_user_id:id
game_management_member  -->  auth_user : delete_user_id:id
game_management_member  -->  auth_user : create_user_id:id
game_management_member  -->  auth_user : update_user_id:id
game_management_member  -->  game_management_gamefunction : game_function_id:id
game_management_memberingame  -->  auth_user : create_user_id:id
game_management_memberingame  -->  auth_user : delete_user_id:id
game_management_memberingame  -->  auth_user : update_user_id:id
game_management_memberingame  -->  game_management_gameinschedule : game_in_schedule_id:id
game_management_memberingame  -->  game_management_member : member_id:id
game_management_memberingame  -->  game_management_memberresult : member_result_additional_id:id
game_management_memberingame  -->  game_management_memberresult : member_result_main_id:id
game_management_memberingame  -->  game_management_role : role_id:id
game_management_memberrating  -->  game_management_gametype : game_id:id
game_management_memberrating  -->  game_management_member : member_id:id
game_management_memberresult  -->  auth_user : delete_user_id:id
game_management_memberresult  -->  auth_user : create_user_id:id
game_management_memberresult  -->  auth_user : update_user_id:id
game_management_memberstatistics  -->  game_management_gametype : game_id:id
game_management_memberstatistics  -->  game_management_member : member_id:id
game_management_memberstatistics  -->  game_management_memberresult : result_id:id
game_management_memberstatistics  -->  game_management_role : role_id:id
game_management_promo  -->  auth_user : create_user_id:id
game_management_promo  -->  auth_user : update_user_id:id
game_management_promo  -->  auth_user : delete_user_id:id
game_management_registeredtogame  -->  auth_user : delete_user_id:id
game_management_registeredtogame  -->  auth_user : update_user_id:id
game_management_registeredtogame  -->  auth_user : create_user_id:id
game_management_registeredtogame  -->  game_management_member : member_id:id
game_management_registeredtogame  -->  game_management_schedule : schedule_id:id
game_management_role  -->  auth_user : update_user_id:id
game_management_role  -->  auth_user : create_user_id:id
game_management_role  -->  auth_user : delete_user_id:id
game_management_schedule  -->  auth_user : create_user_id:id
game_management_schedule  -->  auth_user : update_user_id:id
game_management_schedule  -->  auth_user : delete_user_id:id
game_management_schedule  -->  game_management_gametype : game_id:id
game_management_schedule  -->  game_management_location : location_id:id
