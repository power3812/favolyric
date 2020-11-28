

# テーブル定義


## accounts_credentials
TBL物理名|TBL論理名（コメント）
--------|--------
accounts_credentials|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
token|varchar(255)|NO|n/a|n/a|n/a|n/a|
refresh_token|varchar(255)|NO|n/a|n/a|n/a|n/a|
token_uri|varchar(255)|NO|n/a|n/a|n/a|n/a|
client_id|varchar(255)|NO|n/a|n/a|n/a|n/a|
client_secret|varchar(255)|NO|n/a|n/a|n/a|n/a|
scopes|varchar(255)|NO|n/a|n/a|n/a|n/a|
user_id|int(11)|NO|n/a|UNI|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
user_id|user_id|1|NO|YES|


## auth_group
TBL物理名|TBL論理名（コメント）
--------|--------
auth_group|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
name|varchar(150)|NO|n/a|UNI|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
name|name|1|NO|YES|


## auth_group_permissions
TBL物理名|TBL論理名（コメント）
--------|--------
auth_group_permissions|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
group_id|int(11)|NO|n/a|MUL|n/a|n/a|
permission_id|int(11)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
auth_group_permissions_group_id_permission_id_0cd325b0_uniq|group_id|1|NO|YES|
auth_group_permissions_group_id_permission_id_0cd325b0_uniq|permission_id|2|NO|YES|
auth_group_permissio_permission_id_84c5c92e_fk_auth_perm|permission_id|1|NO|NO|


## auth_permission
TBL物理名|TBL論理名（コメント）
--------|--------
auth_permission|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
name|varchar(255)|NO|n/a|n/a|n/a|n/a|
content_type_id|int(11)|NO|n/a|MUL|n/a|n/a|
codename|varchar(100)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
auth_permission_content_type_id_codename_01ab375a_uniq|content_type_id|1|NO|YES|
auth_permission_content_type_id_codename_01ab375a_uniq|codename|2|NO|YES|


## auth_user
TBL物理名|TBL論理名（コメント）
--------|--------
auth_user|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
password|varchar(128)|NO|n/a|n/a|n/a|n/a|
last_login|datetime(6)|YES|n/a|n/a|n/a|n/a|
is_superuser|tinyint(1)|NO|n/a|n/a|n/a|n/a|
username|varchar(150)|NO|n/a|UNI|n/a|n/a|
first_name|varchar(30)|NO|n/a|n/a|n/a|n/a|
last_name|varchar(150)|NO|n/a|n/a|n/a|n/a|
email|varchar(254)|NO|n/a|n/a|n/a|n/a|
is_staff|tinyint(1)|NO|n/a|n/a|n/a|n/a|
is_active|tinyint(1)|NO|n/a|n/a|n/a|n/a|
date_joined|datetime(6)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
username|username|1|NO|YES|


## auth_user_groups
TBL物理名|TBL論理名（コメント）
--------|--------
auth_user_groups|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
user_id|int(11)|NO|n/a|MUL|n/a|n/a|
group_id|int(11)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
auth_user_groups_user_id_group_id_94350c0c_uniq|user_id|1|NO|YES|
auth_user_groups_user_id_group_id_94350c0c_uniq|group_id|2|NO|YES|
auth_user_groups_group_id_97559544_fk_auth_group_id|group_id|1|NO|NO|


## auth_user_user_permissions
TBL物理名|TBL論理名（コメント）
--------|--------
auth_user_user_permissions|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
user_id|int(11)|NO|n/a|MUL|n/a|n/a|
permission_id|int(11)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
auth_user_user_permissions_user_id_permission_id_14a6b632_uniq|user_id|1|NO|YES|
auth_user_user_permissions_user_id_permission_id_14a6b632_uniq|permission_id|2|NO|YES|
auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm|permission_id|1|NO|NO|


## django_admin_log
TBL物理名|TBL論理名（コメント）
--------|--------
django_admin_log|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
action_time|datetime(6)|NO|n/a|n/a|n/a|n/a|
object_id|longtext|YES|n/a|n/a|n/a|n/a|
object_repr|varchar(200)|NO|n/a|n/a|n/a|n/a|
action_flag|smallint(5) unsigned|NO|n/a|n/a|n/a|n/a|
change_message|longtext|NO|n/a|n/a|n/a|n/a|
content_type_id|int(11)|YES|n/a|MUL|n/a|n/a|
user_id|int(11)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
django_admin_log_content_type_id_c4bce8eb_fk_django_co|content_type_id|1|YES|NO|
django_admin_log_user_id_c564eba6_fk_auth_user_id|user_id|1|NO|NO|


## django_content_type
TBL物理名|TBL論理名（コメント）
--------|--------
django_content_type|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
app_label|varchar(100)|NO|n/a|MUL|n/a|n/a|
model|varchar(100)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
django_content_type_app_label_model_76bd3d3b_uniq|app_label|1|NO|YES|
django_content_type_app_label_model_76bd3d3b_uniq|model|2|NO|YES|


## django_evolution
TBL物理名|TBL論理名（コメント）
--------|--------
django_evolution|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
version_id|int(11)|NO|n/a|MUL|n/a|n/a|
app_label|varchar(200)|NO|n/a|n/a|n/a|n/a|
label|varchar(100)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
django_evolution_version_id_e55942c9_fk_django_pr|version_id|1|NO|NO|


## django_migrations
TBL物理名|TBL論理名（コメント）
--------|--------
django_migrations|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
app|varchar(255)|NO|n/a|n/a|n/a|n/a|
name|varchar(255)|NO|n/a|n/a|n/a|n/a|
applied|datetime(6)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|


## django_project_version
TBL物理名|TBL論理名（コメント）
--------|--------
django_project_version|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
signature|longtext|NO|n/a|n/a|n/a|n/a|
when|datetime(6)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|


## django_session
TBL物理名|TBL論理名（コメント）
--------|--------
django_session|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
session_key|varchar(40)|NO|n/a|PRI|n/a|n/a|
session_data|longtext|NO|n/a|n/a|n/a|n/a|
expire_date|datetime(6)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|session_key|1|NO|YES|
django_session_expire_date_a5c62663|expire_date|1|NO|NO|


## favolyric_artists
TBL物理名|TBL論理名（コメント）
--------|--------
favolyric_artists|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
name|varchar(255)|NO|n/a|UNI|n/a|n/a|
created_at|datetime(6)|YES|n/a|n/a|n/a|n/a|
updated_at|datetime(6)|YES|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
name|name|1|NO|YES|


## favolyric_images
TBL物理名|TBL論理名（コメント）
--------|--------
favolyric_images|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
url|varchar(255)|NO|n/a|UNI|n/a|n/a|
created_at|datetime(6)|YES|n/a|n/a|n/a|n/a|
updated_at|datetime(6)|YES|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
url|url|1|NO|YES|


## favolyric_lyrics
TBL物理名|TBL論理名（コメント）
--------|--------
favolyric_lyrics|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
title|varchar(255)|NO|n/a|MUL|n/a|n/a|
artist_id|int(11)|NO|n/a|MUL|n/a|n/a|
image_id|int(11)|NO|n/a|MUL|n/a|n/a|
itunes_link|varchar(255)|NO|n/a|MUL|n/a|n/a|
happy|double|NO|n/a|MUL|n/a|n/a|
sad|double|NO|n/a|MUL|n/a|n/a|
angry|double|NO|n/a|MUL|n/a|n/a|
disgust|double|NO|n/a|MUL|n/a|n/a|
surprise|double|NO|n/a|MUL|n/a|n/a|
fear|double|NO|n/a|MUL|n/a|n/a|
created_at|datetime(6)|YES|n/a|n/a|n/a|n/a|
updated_at|datetime(6)|YES|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
favolyric_lyrics_title_artist_id_e89cc451_uniq|title|1|NO|YES|
favolyric_lyrics_title_artist_id_e89cc451_uniq|artist_id|2|NO|YES|
favolyric_lyrics_title_e50f6505|title|1|NO|NO|
favolyric_lyrics_artist_id_d5eac55f|artist_id|1|NO|NO|
favolyric_lyrics_image_id_d66bb826|image_id|1|NO|NO|
favolyric_lyrics_itunes_link_3af23925|itunes_link|1|NO|NO|
favolyric_lyrics_happy_ac4c8783|happy|1|NO|NO|
favolyric_lyrics_sad_4a3a73ac|sad|1|NO|NO|
favolyric_lyrics_angry_80fa05a2|angry|1|NO|NO|
favolyric_lyrics_disgust_28419263|disgust|1|NO|NO|
favolyric_lyrics_surprise_ab28b7f9|surprise|1|NO|NO|
favolyric_lyrics_fear_e3b1a2aa|fear|1|NO|NO|


## favolyric_views
TBL物理名|TBL論理名（コメント）
--------|--------
favolyric_views|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
lyric_id|int(11)|NO|n/a|MUL|n/a|n/a|
created_at|datetime(6)|NO|n/a|n/a|n/a|n/a|
updated_at|datetime(6)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
favolyric_views_lyric_id_created_at_fe52883f_uniq|lyric_id|1|NO|YES|
favolyric_views_lyric_id_created_at_fe52883f_uniq|created_at|2|NO|YES|
favolyric_views_lyric_id_48f3f023|lyric_id|1|NO|NO|


## social_auth_association
TBL物理名|TBL論理名（コメント）
--------|--------
social_auth_association|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
server_url|varchar(255)|NO|n/a|MUL|n/a|n/a|
handle|varchar(255)|NO|n/a|n/a|n/a|n/a|
secret|varchar(255)|NO|n/a|n/a|n/a|n/a|
issued|int(11)|NO|n/a|n/a|n/a|n/a|
lifetime|int(11)|NO|n/a|n/a|n/a|n/a|
assoc_type|varchar(64)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
social_auth_association_server_url_handle_078befa2_uniq|server_url|1|NO|YES|
social_auth_association_server_url_handle_078befa2_uniq|handle|2|NO|YES|


## social_auth_code
TBL物理名|TBL論理名（コメント）
--------|--------
social_auth_code|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
email|varchar(254)|NO|n/a|MUL|n/a|n/a|
code|varchar(32)|NO|n/a|MUL|n/a|n/a|
verified|tinyint(1)|NO|n/a|n/a|n/a|n/a|
timestamp|datetime(6)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
social_auth_code_email_code_801b2d02_uniq|email|1|NO|YES|
social_auth_code_email_code_801b2d02_uniq|code|2|NO|YES|
social_auth_code_code_a2393167|code|1|NO|NO|
social_auth_code_timestamp_176b341f|timestamp|1|NO|NO|


## social_auth_nonce
TBL物理名|TBL論理名（コメント）
--------|--------
social_auth_nonce|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
server_url|varchar(255)|NO|n/a|MUL|n/a|n/a|
timestamp|int(11)|NO|n/a|n/a|n/a|n/a|
salt|varchar(65)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
social_auth_nonce_server_url_timestamp_salt_f6284463_uniq|server_url|1|NO|YES|
social_auth_nonce_server_url_timestamp_salt_f6284463_uniq|timestamp|2|NO|YES|
social_auth_nonce_server_url_timestamp_salt_f6284463_uniq|salt|3|NO|YES|


## social_auth_partial
TBL物理名|TBL論理名（コメント）
--------|--------
social_auth_partial|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
token|varchar(32)|NO|n/a|MUL|n/a|n/a|
next_step|smallint(5) unsigned|NO|n/a|n/a|n/a|n/a|
backend|varchar(32)|NO|n/a|n/a|n/a|n/a|
data|longtext|NO|n/a|n/a|n/a|n/a|
timestamp|datetime(6)|NO|n/a|MUL|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
social_auth_partial_token_3017fea3|token|1|NO|NO|
social_auth_partial_timestamp_50f2119f|timestamp|1|NO|NO|


## social_auth_usersocialauth
TBL物理名|TBL論理名（コメント）
--------|--------
social_auth_usersocialauth|

#### カラム情報
物理名|データ型|NULL|デフォルト|キー|論理名（コメント）|Extra
----|----|----|----|----|---|---|
id|int(11)|NO|n/a|PRI|n/a|auto_increment|
provider|varchar(32)|NO|n/a|MUL|n/a|n/a|
uid|varchar(255)|NO|n/a|MUL|n/a|n/a|
extra_data|longtext|NO|n/a|n/a|n/a|n/a|
user_id|int(11)|NO|n/a|MUL|n/a|n/a|
created|datetime(6)|NO|n/a|n/a|n/a|n/a|
modified|datetime(6)|NO|n/a|n/a|n/a|n/a|


#### インデックス情報
インデックス名|カラム|複合キー順序|NULL|UNIQ
----|----|----|----|----
PRIMARY|id|1|NO|YES|
social_auth_usersocialauth_provider_uid_e6b5e668_uniq|provider|1|NO|YES|
social_auth_usersocialauth_provider_uid_e6b5e668_uniq|uid|2|NO|YES|
social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id|user_id|1|NO|NO|
social_auth_usersocialauth_uid_796e51dc|uid|1|NO|NO|
