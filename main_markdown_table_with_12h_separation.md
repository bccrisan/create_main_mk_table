## 2018/12/12 - 08:00-20:00 pt - In Production 

|	autoland	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ff5e6ef2f756)|Bug 1499655 - Ensure we forceLayerTreeToComposite in tests where we read the compositor APZ test data at the start of the test. r=botond  Differential Revision: https://phabricator.services.mozilla.com/D14206|2018-12-13 12:23:58|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=14a53c3f5f7f)|Bug 1499655 - Move the flushLayout code into forceLayerTreeToCompositor. r=botond  These two bits of code conceptually belong together, since the flushLayout code is intended to work around a case where forceLayerTreeToCompositor wasn't doing anything. So it makes sense to just put them into the same function.  Differential Revision: https://phabricator.services.mozilla.com/D14205|2018-12-13 12:24:08|

|	beta	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=022e5d97749f)|Bug 1512037 - Bail out from prefersReducedMotion() if the target device is Android 4.1 or older. r=snorp a=jcristau  Settings.Global can't be used on such devices.  Differential Revision: https://phabricator.services.mozilla.com/D14226|2018-12-11 23:38:26|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=b0e263db0edf)|Backed out changeset ac3f8e63166b (bug 1512037) for causing Android build bustages|2018-12-12 19:12:55|

|	braindump	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=535d3728de73)|Fix params layout.|2018-12-11 20:45:39|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c4919d73df5a)|Make required-signoffs the default.|2018-12-05 16:32:54|

|	ci-admin	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|2018-10-22 17:52:14|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808)|Bug 1492665 - add support for environments.yml r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6932|2018-10-22 17:52:13|

## 2018/12/11 - 20:00-08:00 pt - In Production

|	autoland	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/autoland.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=ff5e6ef2f756)|Bug 1499655 - Ensure we forceLayerTreeToComposite in tests where we read the compositor APZ test data at the start of the test. r=botond  Differential Revision: https://phabricator.services.mozilla.com/D14206|2018-12-13 12:23:58|
|[Link to commit](https://hg.mozilla.org/integration/autoland/pushloghtml?changeset=14a53c3f5f7f)|Bug 1499655 - Move the flushLayout code into forceLayerTreeToCompositor. r=botond  These two bits of code conceptually belong together, since the flushLayout code is intended to work around a case where forceLayerTreeToCompositor wasn't doing anything. So it makes sense to just put them into the same function.  Differential Revision: https://phabricator.services.mozilla.com/D14205|2018-12-13 12:24:08|

|	beta	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/beta.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=022e5d97749f)|Bug 1512037 - Bail out from prefersReducedMotion() if the target device is Android 4.1 or older. r=snorp a=jcristau  Settings.Global can't be used on such devices.  Differential Revision: https://phabricator.services.mozilla.com/D14226|2018-12-11 23:38:26|
|[Link to commit](https://hg.mozilla.org/releases/mozilla-beta/pushloghtml?changeset=b0e263db0edf)|Backed out changeset ac3f8e63166b (bug 1512037) for causing Android build bustages|2018-12-12 19:12:55|

|	braindump	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/braindump.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=535d3728de73)|Fix params layout.|2018-12-11 20:45:39|
|[Link to commit](https://hg.mozilla.org/build/braindump/pushloghtml?changeset=c4919d73df5a)|Make required-signoffs the default.|2018-12-05 16:32:54|

|	ci-admin	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-admin.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=99d859a7a655)|Bug 1492665 - add modify_resources support r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6933|2018-10-22 17:52:14|
|[Link to commit](https://hg.mozilla.org/build/ci-admin/pushloghtml?changeset=241f75b5d808)|Bug 1492665 - add support for environments.yml r=Callek,bstack  Differential Revision: https://phabricator.services.mozilla.com/D6932|2018-10-22 17:52:13|

|	ci-configuration	|	[MarkDown](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.md)	|	[Json](https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/ci-configuration.json)	| 
|:----------------:|:-------------------------------------:|:---------------------------------:| 
 
 