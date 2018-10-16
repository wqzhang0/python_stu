/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : rpc

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-10-14 23:06:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add role permission', '7', 'add_rolepermission');
INSERT INTO `auth_permission` VALUES ('26', 'Can change role permission', '7', 'change_rolepermission');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete role permission', '7', 'delete_rolepermission');
INSERT INTO `auth_permission` VALUES ('28', 'Can view role permission', '7', 'view_rolepermission');
INSERT INTO `auth_permission` VALUES ('29', 'Can add rpc api', '8', 'add_rpcapi');
INSERT INTO `auth_permission` VALUES ('30', 'Can change rpc api', '8', 'change_rpcapi');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete rpc api', '8', 'delete_rpcapi');
INSERT INTO `auth_permission` VALUES ('32', 'Can view rpc api', '8', 'view_rpcapi');
INSERT INTO `auth_permission` VALUES ('33', 'Can add rpc module', '9', 'add_rpcmodule');
INSERT INTO `auth_permission` VALUES ('34', 'Can change rpc module', '9', 'change_rpcmodule');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete rpc module', '9', 'delete_rpcmodule');
INSERT INTO `auth_permission` VALUES ('36', 'Can view rpc module', '9', 'view_rpcmodule');
INSERT INTO `auth_permission` VALUES ('37', 'Can add rpc role', '10', 'add_rpcrole');
INSERT INTO `auth_permission` VALUES ('38', 'Can change rpc role', '10', 'change_rpcrole');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete rpc role', '10', 'delete_rpcrole');
INSERT INTO `auth_permission` VALUES ('40', 'Can view rpc role', '10', 'view_rpcrole');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$120000$uDP1Ta9z4W0W$SwfkWNK/Dd11I4lXptx4A3DTZnl00UtxqlpxdzEopnM=', '2018-10-14 07:38:12.198710', '1', 'wqzhang', '', '', 'bate1217@163.com', '1', '1', '2018-10-14 07:38:08.338561');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-10-14 07:38:30.264626', '1', '人大', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-10-14 07:38:49.031579', '2', '文件管理', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-10-14 07:39:23.971074', '1', '获取文件列表', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-10-14 07:45:03.366404', '7cef9808-13fa-4b58-b80a-47cc58e85058', '人大管理员', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2018-10-14 07:46:32.313029', '1', '人大管理员获取文件列表', '1', '[{\"added\": {}}]', '7', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('7', 'app', 'rolepermission');
INSERT INTO `django_content_type` VALUES ('8', 'app', 'rpcapi');
INSERT INTO `django_content_type` VALUES ('9', 'app', 'rpcmodule');
INSERT INTO `django_content_type` VALUES ('10', 'app', 'rpcrole');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-10-14 07:37:17.885409');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-10-14 07:37:19.980386');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-10-14 07:37:20.516386');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-10-14 07:37:20.539388');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2018-10-14 07:37:20.556385');
INSERT INTO `django_migrations` VALUES ('6', 'app', '0001_initial', '2018-10-14 07:37:22.293407');
INSERT INTO `django_migrations` VALUES ('7', 'contenttypes', '0002_remove_content_type_name', '2018-10-14 07:37:22.629387');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0002_alter_permission_name_max_length', '2018-10-14 07:37:22.871386');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0003_alter_user_email_max_length', '2018-10-14 07:37:22.922387');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0004_alter_user_username_opts', '2018-10-14 07:37:22.940387');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0005_alter_user_last_login_null', '2018-10-14 07:37:23.119407');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0006_require_contenttypes_0002', '2018-10-14 07:37:23.127402');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0007_alter_validators_add_error_messages', '2018-10-14 07:37:23.144402');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0008_alter_user_username_max_length', '2018-10-14 07:37:23.332390');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0009_alter_user_last_name_max_length', '2018-10-14 07:37:23.518386');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2018-10-14 07:37:23.677388');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('t1ns2dlx5lrbaayo99to15ld7zbtbk66', 'YmI5NTE4M2FmN2ExNTYxNmFkMDU2NDYyMWFlNWM5NjQ2YTE2N2IyOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmOTJlZmZjZWJlZTEzZmRiYzdiNTA4NmUxNTE1MGE2ZTIxMzcyZmQ3In0=', '2018-10-28 07:38:12.213707');

-- ----------------------------
-- Table structure for rpc_api
-- ----------------------------
DROP TABLE IF EXISTS `rpc_api`;
CREATE TABLE `rpc_api` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `last_update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(100) NOT NULL,
  `url` varchar(100) NOT NULL,
  `desc` varchar(500) NOT NULL,
  `module_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rpc_api_module_id_9849bfa5_fk_rpc_module_id` (`module_id`),
  CONSTRAINT `rpc_api_module_id_9849bfa5_fk_rpc_module_id` FOREIGN KEY (`module_id`) REFERENCES `rpc_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of rpc_api
-- ----------------------------
INSERT INTO `rpc_api` VALUES ('1', '2018-10-14 07:39:23.964073', '2018-10-14 07:39:23.964073', '0', '获取文件列表', 'getFileList', '获取文件列表 描述', '2');

-- ----------------------------
-- Table structure for rpc_module
-- ----------------------------
DROP TABLE IF EXISTS `rpc_module`;
CREATE TABLE `rpc_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `last_update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` varchar(500) NOT NULL,
  `super_module_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rpc_module_super_module_id_6935c379_fk_rpc_module_id` (`super_module_id`),
  CONSTRAINT `rpc_module_super_module_id_6935c379_fk_rpc_module_id` FOREIGN KEY (`super_module_id`) REFERENCES `rpc_module` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of rpc_module
-- ----------------------------
INSERT INTO `rpc_module` VALUES ('1', '2018-10-14 07:38:30.258626', '2018-10-14 07:38:30.259626', '0', '人大', '项目模块', null);
INSERT INTO `rpc_module` VALUES ('2', '2018-10-14 07:38:49.026578', '2018-10-14 07:38:49.026578', '0', '文件管理', '文件管理', '1');

-- ----------------------------
-- Table structure for rpc_role
-- ----------------------------
DROP TABLE IF EXISTS `rpc_role`;
CREATE TABLE `rpc_role` (
  `create_time` datetime(6) NOT NULL,
  `last_update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `uuid` char(32) NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` varchar(500) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of rpc_role
-- ----------------------------
INSERT INTO `rpc_role` VALUES ('2018-10-14 07:45:03.355402', '2018-10-14 07:45:03.355402', '0', '7cef980813fa4b58b80a47cc58e85058', '人大管理员', '人大管理员');

-- ----------------------------
-- Table structure for rpc_role_permission
-- ----------------------------
DROP TABLE IF EXISTS `rpc_role_permission`;
CREATE TABLE `rpc_role_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `last_update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `RpcApi_id` int(11) NOT NULL,
  `RpcRole_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rpc_Role_Permission_RpcRole_id_RpcApi_id_9a853e20_uniq` (`RpcRole_id`,`RpcApi_id`),
  KEY `rpc_Role_Permission_RpcApi_id_4759a113_fk_rpc_api_id` (`RpcApi_id`),
  CONSTRAINT `rpc_Role_Permission_RpcApi_id_4759a113_fk_rpc_api_id` FOREIGN KEY (`RpcApi_id`) REFERENCES `rpc_api` (`id`),
  CONSTRAINT `rpc_Role_Permission_RpcRole_id_3f451293_fk_rpc_Role_uuid` FOREIGN KEY (`RpcRole_id`) REFERENCES `rpc_role` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of rpc_role_permission
-- ----------------------------
INSERT INTO `rpc_role_permission` VALUES ('1', '2018-10-14 07:46:32.304047', '2018-10-14 07:46:32.304047', '0', '1', '7cef980813fa4b58b80a47cc58e85058');
SET FOREIGN_KEY_CHECKS=1;
