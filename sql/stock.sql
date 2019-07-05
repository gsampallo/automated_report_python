/*
Navicat MySQL Data Transfer

Source Server         : Localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : stock

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-07-04 21:20:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `movimientos`
-- ----------------------------
DROP TABLE IF EXISTS `movimientos`;
CREATE TABLE `movimientos` (
  `mov_id` int(4) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `producto_id` int(3) NOT NULL,
  `tipo_movimiento` varchar(1) NOT NULL,
  `cantidad` int(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`mov_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of movimientos
-- ----------------------------
INSERT INTO `movimientos` VALUES ('1', '2019-06-24', '1', 'A', '3');

-- ----------------------------
-- Table structure for `productos`
-- ----------------------------
DROP TABLE IF EXISTS `productos`;
CREATE TABLE `productos` (
  `producto_id` int(3) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(20) NOT NULL,
  `stock` int(3) NOT NULL,
  PRIMARY KEY (`producto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of productos
-- ----------------------------
INSERT INTO `productos` VALUES ('1', 'Producto A', '1');
INSERT INTO `productos` VALUES ('2', 'Producto B', '4');
INSERT INTO `productos` VALUES ('3', 'Producto C', '5');
INSERT INTO `productos` VALUES ('4', 'Producto D', '0');
