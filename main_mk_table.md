|      Repository      |                   Last commit               |    Deploy time       | 
|:--------------------:|:-------------------------------------------:|:--------------------:| 
|test|quote mr versions to avoid being treated as floats|data|
|test|Bug 1503894 - reenable taskcluster-cron for comm-central repo. r=tomprince

This goes along with a .cron.yml update in comm-central that removes the
periodic-file-update cron configuration. (Bug 1499590 comment 15)

This will get comm-central nightly builds working again.

Differential Revision: https://phabricator.services.mozilla.com/D10959|data|
|test|Bug 1492665 - add modify_resources support r=Callek,bstack

Differential Revision: https://phabricator.services.mozilla.com/D6933|data|
|test|No bug - Pin mozilla-esr60 version for release. a=jorgk|data|
|test|merge default->production; tests passing|data|
|test|Bug 1506212 - Fix more in-content button colors. r=bgrins

Differential Revision: https://phabricator.services.mozilla.com/D11555|data|
|test|no bug - Bumping Firefox l10n changesets r=release a=l10n-bump DONTBUILD

it -> a2c6ba1924c3|data|
|test|Merge inbound to mozilla-central.  a=merge|data|
|test|Bug 1499265 - Intermittent failure in update-verify: Task timeout after 3600 seconds. Force killing container. r=aki a=tomprince

Intermittent failure in update-verify: Task timeout after 3600 seconds. Force killing container

Differential Revision: https://phabricator.services.mozilla.com/D8925|data|
|test|Bug 1506391 - Manually extinguish multi-line use statements.
|data|
|test|Backed out changeset 7e6f51f7fca4 (bug 1470786) for causing bug 1505161; a=backout|data|
|test|Fuzzy query=android web-pl

Pushed via `mach try fuzzy`|data|
|test|Bug 1501406 - Update vswhere to version 2.5.2.|data|
|test|robustcheckout: reference `testedwith` in `supported_hg` assertion r=gps

Now we only need to update the supported Mercurial versions in a
single location.

Differential Revision: https://phabricator.services.mozilla.com/D11197|data|
