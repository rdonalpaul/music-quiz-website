CREATE TABLE user_comments 
(
    comment_id INT AUTO_INCREMENT,
    username VARCHAR(255),
    url VARCHAR(255) NOT NULL,
    comment TEXT,
    PRIMARY KEY (comment_id)
);
