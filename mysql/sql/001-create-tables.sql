---- drop ----
DROP TABLE IF EXISTS views;

---- create ----
create table IF not exists views
(
    'id'               INT(20) AUTO_INCREMENT,
    'lyric_id'         VARCHAR(20) NOT NULL,
    'created_at'       Datetime DEFAULT NULL,
    'updated_at'       Datetime DEFAULT NULL,
    PRIMARY KEY ('id')
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
