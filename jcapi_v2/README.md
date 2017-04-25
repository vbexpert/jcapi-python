# jcapiv2
Allow cusotmers to manage the JumpCloud Directory objects, groupings and mappings.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 2.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import jcapiv2 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import jcapiv2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = jcapiv2.DirectoriesApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try:
    # List All Directories, which consist of G Suites, LDAP Servers and Office 365s. 
    api_response = api_instance.list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:3004/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DirectoriesApi* | [**list**](docs/DirectoriesApi.md#list) | **GET** /directories | List All Directories, which consist of G Suites, LDAP Servers and Office 365s. 
*GraphApi* | [**application_associations_list**](docs/GraphApi.md#application_associations_list) | **GET** /applications/{application_id}/associations | List associations of a application
*GraphApi* | [**application_associations_post**](docs/GraphApi.md#application_associations_post) | **POST** /applications/{application_id}/associations | Manage associations of an Application
*GraphApi* | [**application_server_traverse_user**](docs/GraphApi.md#application_server_traverse_user) | **GET** /applications/{application_id}/users | Get the Users an Application is associated with.
*GraphApi* | [**application_traverse_user_groups**](docs/GraphApi.md#application_traverse_user_groups) | **GET** /applications/{application_id}/usergroups | Get the User Groups an Application is associated with.
*GraphApi* | [**command_associations_list**](docs/GraphApi.md#command_associations_list) | **GET** /commands/{command_id}/associations | List associations of a command
*GraphApi* | [**command_associations_post**](docs/GraphApi.md#command_associations_post) | **POST** /commands/{command_id}/associations | Manage associations of a Command
*GraphApi* | [**command_traverse_system**](docs/GraphApi.md#command_traverse_system) | **GET** /commands/{command_id}/systems | Get the Systems an Command is associated with.
*GraphApi* | [**command_traverse_system_group**](docs/GraphApi.md#command_traverse_system_group) | **GET** /commands/{command_id}/systemgroups | Get the System Groups an Command is associated with.
*GraphApi* | [**g_suite_associations_list**](docs/GraphApi.md#g_suite_associations_list) | **GET** /gsuites/{gsuite_id}/associations | List associations of a G Suite instance.
*GraphApi* | [**g_suite_associations_post**](docs/GraphApi.md#g_suite_associations_post) | **POST** /gsuites/{gsuite_id}/associations | Manage associations of a G Suite instance.
*GraphApi* | [**g_suite_traverse_user**](docs/GraphApi.md#g_suite_traverse_user) | **GET** /gsuites/{gsuite_id}/users | Get the Users a G Suite instance is associated with.
*GraphApi* | [**g_suite_traverse_user_group**](docs/GraphApi.md#g_suite_traverse_user_group) | **GET** /gsuites/{gsuite_id}/usergroups | Get the User Groups a G Suite instance is associated with.
*GraphApi* | [**ldap_server_associations_list**](docs/GraphApi.md#ldap_server_associations_list) | **GET** /ldapservers/{ldapserver_id}/associations | List associations of a LDAP Server
*GraphApi* | [**ldap_server_associations_post**](docs/GraphApi.md#ldap_server_associations_post) | **POST** /ldapservers/{ldapserver_id}/associations | Manage associations of a LDAP Server
*GraphApi* | [**ldap_server_traverse_user**](docs/GraphApi.md#ldap_server_traverse_user) | **GET** /ldapservers/{ldapserver_id}/users | Get the Users a LDAP Server is associated with.
*GraphApi* | [**ldap_server_traverse_user_group**](docs/GraphApi.md#ldap_server_traverse_user_group) | **GET** /ldapservers/{ldapserver_id}/usergroups | Get the User Groups a LDAP Server is associated with.
*GraphApi* | [**office365_associations_list**](docs/GraphApi.md#office365_associations_list) | **GET** /office365s/{office365_id}/associations | List associations of a Office 365 instance.
*GraphApi* | [**office365_associations_post**](docs/GraphApi.md#office365_associations_post) | **POST** /office365s/{office365_id}/associations | Manage associations of a Office 365 suite.
*GraphApi* | [**office365_traverse_user**](docs/GraphApi.md#office365_traverse_user) | **GET** /office365s/{office365_id}/users | Get the Users a Office 365 instance is associated with.
*GraphApi* | [**office365_traverse_user_group**](docs/GraphApi.md#office365_traverse_user_group) | **GET** /office365s/{office365_id}/usergroups | Get the User Groups a Office 365 instance is associated with.
*GraphApi* | [**radius_server_associations_list**](docs/GraphApi.md#radius_server_associations_list) | **GET** /radiusservers/{radiusserver_id}/associations | List associations of a Radius Server
*GraphApi* | [**radius_server_associations_post**](docs/GraphApi.md#radius_server_associations_post) | **POST** /radiusservers/{radiusserver_id}/associations | Manage associations of a Radius Server
*GraphApi* | [**radius_server_traverse_user**](docs/GraphApi.md#radius_server_traverse_user) | **GET** /radiusservers/{radiusserver_id}/users | Get the Users a Radius Server is associated with.
*GraphApi* | [**radius_server_traverse_user_group**](docs/GraphApi.md#radius_server_traverse_user_group) | **GET** /radiusservers/{radiusserver_id}/usergroups | Get the User Groups a Radius Server is associated with.
*GraphApi* | [**system_associations_list**](docs/GraphApi.md#system_associations_list) | **GET** /systems/{system_id}/associations | List associations of a System
*GraphApi* | [**system_associations_post**](docs/GraphApi.md#system_associations_post) | **POST** /systems/{system_id}/associations | Manage associations of a System
*GraphApi* | [**system_group_associations_list**](docs/GraphApi.md#system_group_associations_list) | **GET** /systemgroups/{group_id}/associations | List associations of a System Group.
*GraphApi* | [**system_group_associations_post**](docs/GraphApi.md#system_group_associations_post) | **POST** /systemgroups/{group_id}/associations | Manage associations of a System Group
*GraphApi* | [**system_group_member_of**](docs/GraphApi.md#system_group_member_of) | **GET** /systemgroups/{group_id}/memberof | Get System Group&#39;s groups it is a member of.
*GraphApi* | [**system_group_members_list**](docs/GraphApi.md#system_group_members_list) | **GET** /systemgroups/{group_id}/members | List members of a System Group
*GraphApi* | [**system_group_membership**](docs/GraphApi.md#system_group_membership) | **GET** /systemgroups/{group_id}/membership | Get System and System Group&#39;s who are members of this group.
*GraphApi* | [**system_group_traverse_user**](docs/GraphApi.md#system_group_traverse_user) | **GET** /systemgroups/{group_id}/users | Get the Users a System Group is associated with.
*GraphApi* | [**system_group_traverse_user_group**](docs/GraphApi.md#system_group_traverse_user_group) | **GET** /systemgroups/{group_id}/usergroups | Get the User Groups a System Group is associated with.
*GraphApi* | [**system_member_of**](docs/GraphApi.md#system_member_of) | **GET** /systems/{system_id}/memberof | Get System&#39;s groups it is a member of.
*GraphApi* | [**system_traverse_user**](docs/GraphApi.md#system_traverse_user) | **GET** /systems/{system_id}/users | Get the Users a System is associated with.
*GraphApi* | [**user_associations_list**](docs/GraphApi.md#user_associations_list) | **GET** /users/{user_id}/associations | List associations of a User.
*GraphApi* | [**user_associations_post**](docs/GraphApi.md#user_associations_post) | **POST** /users/{user_id}/associations | Manage associations of a User
*GraphApi* | [**user_group_associations_list**](docs/GraphApi.md#user_group_associations_list) | **GET** /usergroups/{group_id}/associations | List associations of a User Group.
*GraphApi* | [**user_group_associations_post**](docs/GraphApi.md#user_group_associations_post) | **POST** /usergroups/{group_id}/associations | Manage associations of a User Group
*GraphApi* | [**user_group_member_of**](docs/GraphApi.md#user_group_member_of) | **GET** /usergroups/{group_id}/memberof | Get User Group&#39;s groups it is a member of.
*GraphApi* | [**user_group_members_list**](docs/GraphApi.md#user_group_members_list) | **GET** /usergroups/{group_id}/members | List members of a User Group
*GraphApi* | [**user_group_members_post**](docs/GraphApi.md#user_group_members_post) | **POST** /usergroups/{group_id}/members | Manage members of a User Group
*GraphApi* | [**user_group_membership**](docs/GraphApi.md#user_group_membership) | **GET** /usergroups/{group_id}/membership | Get User and User Group&#39;s who are members of this group.
*GraphApi* | [**user_group_traverse_application**](docs/GraphApi.md#user_group_traverse_application) | **GET** /usergroups/{group_id}/applications | Get the Applications a User Group is associated with.
*GraphApi* | [**user_group_traverse_directory**](docs/GraphApi.md#user_group_traverse_directory) | **GET** /usergroups/{group_id}/directories | Get the Directories a User Group is associated with.
*GraphApi* | [**user_group_traverse_g_suite**](docs/GraphApi.md#user_group_traverse_g_suite) | **GET** /usergroups/{group_id}/gsuites | Get the G Suite instance a User Group is associated with.
*GraphApi* | [**user_group_traverse_ldap_server**](docs/GraphApi.md#user_group_traverse_ldap_server) | **GET** /usergroups/{group_id}/ldapservers | Get the LDAP Servers a User Group is associated with.
*GraphApi* | [**user_group_traverse_office365**](docs/GraphApi.md#user_group_traverse_office365) | **GET** /usergroups/{group_id}/office365s | Get the Office 365 instance a User Group is associated with.
*GraphApi* | [**user_group_traverse_radius_server**](docs/GraphApi.md#user_group_traverse_radius_server) | **GET** /usergroups/{group_id}/radiusservers | Get the Radius Servers a User Group is associated with.
*GraphApi* | [**user_group_traverse_system**](docs/GraphApi.md#user_group_traverse_system) | **GET** /usergroups/{group_id}/systems | Get the Systems a User Group is associated with.
*GraphApi* | [**user_group_traverse_system_group**](docs/GraphApi.md#user_group_traverse_system_group) | **GET** /usergroups/{group_id}/systemgroups | Get the System Groups a User Group is associatedwith.
*GraphApi* | [**user_member_of**](docs/GraphApi.md#user_member_of) | **GET** /users/{user_id}/memberof | Get Users&#39;s groups it is a member of.
*GraphApi* | [**user_traverse_application**](docs/GraphApi.md#user_traverse_application) | **GET** /users/{user_id}/applications | Get the Applications a User is associated with.
*GraphApi* | [**user_traverse_directory**](docs/GraphApi.md#user_traverse_directory) | **GET** /users/{user_id}/directories | Get the Directories a User is associated with.
*GraphApi* | [**user_traverse_g_suite**](docs/GraphApi.md#user_traverse_g_suite) | **GET** /users/{user_id}/gsuites | Get the G Suite instance a User is associated with.
*GraphApi* | [**user_traverse_ldap_server**](docs/GraphApi.md#user_traverse_ldap_server) | **GET** /users/{user_id}/ldapservers | Get the LDAP Servers a User is associated with.
*GraphApi* | [**user_traverse_office365**](docs/GraphApi.md#user_traverse_office365) | **GET** /users/{user_id}/office365s | Get the Office 365 instance a User is associated with.
*GraphApi* | [**user_traverse_radius_server**](docs/GraphApi.md#user_traverse_radius_server) | **GET** /users/{user_id}/radiusservers | Get the Radius Servers a User is associated with.
*GraphApi* | [**user_traverse_system**](docs/GraphApi.md#user_traverse_system) | **GET** /users/{user_id}/systems | Get the Systems a User is associated with.
*GroupsApi* | [**list**](docs/GroupsApi.md#list) | **GET** /groups | List All Groups
*PoliciesApi* | [**delete**](docs/PoliciesApi.md#delete) | **DELETE** /policies/{id} | Deletes a Policy.
*PoliciesApi* | [**policies_get**](docs/PoliciesApi.md#policies_get) | **GET** /policies/{id} | Gets a specific Policy.
*PoliciesApi* | [**policies_list**](docs/PoliciesApi.md#policies_list) | **GET** /policies | Lists all the policies.
*PoliciesApi* | [**policies_post**](docs/PoliciesApi.md#policies_post) | **POST** /policies | Create a new Policy.
*PoliciesApi* | [**policytemplates_id_get**](docs/PoliciesApi.md#policytemplates_id_get) | **GET** /policytemplates/{id} | Get a specific Policy Template.
*PoliciesApi* | [**policytemplates_list**](docs/PoliciesApi.md#policytemplates_list) | **GET** /policytemplates | Lists all of the policy templates.
*PoliciesApi* | [**update**](docs/PoliciesApi.md#update) | **PATCH** /policies/{id} | Update an existing Policy.
*SystemGroupsApi* | [**system_delete**](docs/SystemGroupsApi.md#system_delete) | **DELETE** /systemgroups/{id} | Delete a System Group
*SystemGroupsApi* | [**system_get**](docs/SystemGroupsApi.md#system_get) | **GET** /systemgroups/{id} | View a System Group Detail
*SystemGroupsApi* | [**system_group_members_post**](docs/SystemGroupsApi.md#system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage members of a System Group
*SystemGroupsApi* | [**system_list**](docs/SystemGroupsApi.md#system_list) | **GET** /systemgroups | List All Systems Groups
*SystemGroupsApi* | [**system_patch**](docs/SystemGroupsApi.md#system_patch) | **PATCH** /systemgroups/{id} | Partial Update a System Group
*SystemGroupsApi* | [**system_post**](docs/SystemGroupsApi.md#system_post) | **POST** /systemgroups | Create a New System Group
*UserGroupsApi* | [**user_delete**](docs/UserGroupsApi.md#user_delete) | **DELETE** /usergroups/{id} | Delete a User Group
*UserGroupsApi* | [**user_get**](docs/UserGroupsApi.md#user_get) | **GET** /usergroups/{id} | View a User Group Detail
*UserGroupsApi* | [**user_list**](docs/UserGroupsApi.md#user_list) | **GET** /usergroups | List All Users Groups
*UserGroupsApi* | [**user_patch**](docs/UserGroupsApi.md#user_patch) | **PATCH** /usergroups/{id} | Partial Update a User Group
*UserGroupsApi* | [**user_post**](docs/UserGroupsApi.md#user_post) | **POST** /usergroups | Create a New User Group


## Documentation For Models

 - [Directory](docs/Directory.md)
 - [Error](docs/Error.md)
 - [GraphConnection](docs/GraphConnection.md)
 - [GraphManagementReq](docs/GraphManagementReq.md)
 - [GraphObject](docs/GraphObject.md)
 - [GraphObjectWithPaths](docs/GraphObjectWithPaths.md)
 - [GraphType](docs/GraphType.md)
 - [Group](docs/Group.md)
 - [GroupType](docs/GroupType.md)
 - [Policy](docs/Policy.md)
 - [PolicyTemplate](docs/PolicyTemplate.md)
 - [PolicyTemplateValid](docs/PolicyTemplateValid.md)
 - [SystemGroup](docs/SystemGroup.md)
 - [SystemGroupData](docs/SystemGroupData.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserGroupData](docs/UserGroupData.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


