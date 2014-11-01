use guitar_schema;
 SET @global.TRIGGER_GUITAR_AFTER_INSERT_DISABLED = 0;
 SET @global.TRIGGER_GUITAR_AFTER_UPDATE_DISABLED = 0;
 SET @global.TRIGGER_GUITAR_BEFORE_DELETE_DISABLED = 0;

DELIMITER $$
USE `guitar_schema`$$
DROP TRIGGER IF EXISTS `Guitar_history_insert`$$
CREATE TRIGGER `Guitar_history_insert` AFTER INSERT ON `Guitar` FOR EACH ROW
IF @global.TRIGGER_GUITAR_AFTER_INSERT_DISABLED = 0 THEN
	INSERT INTO History(trigger_action, guitar_id, action_time) VALUES('insert', NEW.id, NOW());
END IF;
$$

DROP TRIGGER IF EXISTS `Guitar_history_update`$$
CREATE TRIGGER `Guitar_history_update` AFTER UPDATE ON `Guitar` FOR EACH ROW
IF @global.TRIGGER_GUITAR_AFTER_UPDATE_DISABLED = 0 THEN
INSERT INTO History(trigger_action, guitar_id, action_time) VALUES('update', OLD.id, NOW());
END IF;
$$

DROP TRIGGER IF EXISTS `Guitar_history_delete`$$
CREATE TRIGGER `Guitar_history_delete` BEFORE DELETE ON `Guitar` FOR EACH ROW
IF @global.TRIGGER_GUITAR_BEFORE_DELETE_DISABLED = 0 THEN
INSERT INTO History(trigger_action, guitar_id, action_time) VALUES('delete', OLD.id, NOW());
END IF;
$$


DELIMITER ;

SELECT @global.TRIGGER_GUITAR_AFTER_INSERT_DISABLED;