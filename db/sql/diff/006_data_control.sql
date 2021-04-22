
-- DATA CONTROL

CREATE TABLE DataControl (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	category VARCHAR(255),
	value VARCHAR(255) NOT NULL
);

-- REQUEST MODIFICATION

ALTER TABLE `UserRequest` ADD COLUMN type enum(
    'COMPANY ADD', 'COMPANY CHANGE',
    'COMPANY ADDRESS CHANGE', 'COMPANY ADDRESS ADD',
    'COMPANY TAXONOMY CHANGE',
    'COMPANY LOGO CHANGE'
) DEFAULT NULL;
ALTER TABLE `UserRequest` ADD COLUMN data JSON DEFAULT NULL AFTER request;
ALTER TABLE `UserRequest` CHANGE `status` enum('NEW', 'IN PROCESS','PROCESSED', 'REJECTED') NOT NULL DEFAULT 'NEW';