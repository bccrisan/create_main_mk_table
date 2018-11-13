## RELEASE SERVICES MARKDOWN TABLE

| Commit Number | Commiter | Commit Message | Commit Url | Date | 
|:---:|:----:|:----------------------------------:|:------:|:----:| 
|30|Kevin Luvian|please-cli: refactor mkProject to only pass project_name (#1678)|[URL](https://github.com/mozilla/release-services/commit/0efec3094069275c8c9155bfc4d70ffd9cace3bb)|2018-11-13 00:48:39 
|29|Kevin Luvian|please-cli: display in which project shell you are (#1676)|[URL](https://github.com/mozilla/release-services/commit/55795964c7b8af1f658ae4cf0437f90ac284f86f)|2018-11-13 00:16:42 
|28|Rok Garbas|setup: update dependencies (#1670)|[URL](https://github.com/mozilla/release-services/commit/591e05867afb6a7dd5fb3917aac0511d323f9110)|2018-11-12 23:36:45 
|27|Marco|staticanalysis/bot: Update parsepatch to latest version and add a regression test for checking if an issue is in a revision (#1679)    staticanalysis/bot: Add tests for Revision.analyze_patch      staticanalysis/bot: Update parsepatch to 0.1.3|[URL](https://github.com/mozilla/release-services/commit/77b4e9d1b463b01ab4fdc56cbef1a71176e5ddf8)|2018-11-12 16:40:20 
|26|Jan Keromnes|staticanalysis/bot: Use the right diffs for the improvement patch. (#1671)|[URL](https://github.com/mozilla/release-services/commit/e505e8e2aad9ff34e5dc2f9e8cbe100684ca9200)|2018-11-08 13:47:00 
|25|Rok Garbas|setup: bumping to v51 (#1672)|[URL](https://github.com/mozilla/release-services/commit/8650a55cb9e33bcbe429ad9e3a8b5759e530129b)|2018-11-07 22:14:32 
|24|Bastien Abadie|docs: Remove IRC notification (#1646)|[URL](https://github.com/mozilla/release-services/commit/b9843defb782381398b0c486d6cc87e9fbc33599)|2018-11-02 15:15:35 
|23|Rok Garbas|tooltool/api: upload does not work (#1667)    backend_common: wrong relengapi token serializer used      tooltool/api: wrong flask subcommand used      releng_frontend: sha of node module changed      releng_frontend: pass correct variables to body      releng_frontend: serve static folder when development|[URL](https://github.com/mozilla/release-services/commit/a8b878937771d1cc49413b9a463e98ff2ca3da2c)|2018-11-02 14:23:59 
|22|Rail Aliiev|shipit/frontend: Add release ETA (#1658)    Add release ETA      Add better validation      Remove margins|[URL](https://github.com/mozilla/release-services/commit/62b6769893e1f277009316dd026a30eb42524546)|2018-11-02 14:23:02 
|21|Rail Aliiev|shipit/api: add /sync API (#1665)    shipit/api: add /sync API    This is a reland of #1517. It was tested in staging and worked fine  without any issues so far.      Remove temp hack|[URL](https://github.com/mozilla/release-services/commit/a34281bd1ce00a66662c479d4ea53b364ec3a685)|2018-11-02 14:22:49 
|20|Tom Prince|shipit/frontend: Generate partial suggestions when selecting a revision manually. (#1666)|[URL](https://github.com/mozilla/release-services/commit/654810cdc036230b5a5722a06dcc55e10ecca36b)|2018-11-02 00:31:32 
|19|ANdi|staticanalysis/bot: Update cbindgen to 0.6.7 (#1663)|[URL](https://github.com/mozilla/release-services/commit/2ca1463b97a98d56424d4b6360e113e68b96c4e3)|2018-10-31 12:03:11 
|18|Rail Aliiev|Fix IRC env var (#1660)|[URL](https://github.com/mozilla/release-services/commit/d500a1adc76e7a330bcee5559dad848b7ac7fd3e)|2018-10-30 16:35:56 
|17|Rail Aliiev|shipit/api: Use env vars for TC IRC notifications (#1659)    Use env vars for TC IRC notifications      Fallback to secrets|[URL](https://github.com/mozilla/release-services/commit/ef49454d8884fb8e0cf6c83d48b5d979461a73f6)|2018-10-30 16:17:39 
|16|Rail Aliiev|shipit/frontend: Use BACKEND_URL (renamed to SHIPIT_API_URL) from data-shipit-api-url for accessing backend (#1656)|[URL](https://github.com/mozilla/release-services/commit/f6e18607663b8db905c07bc17b0fabe4dd4f38e5)|2018-10-30 08:18:30 
|15|Bastien Abadie|staticanalysis/bot: Update rust-cbindgen to 0.6.6 (#1654)|[URL](https://github.com/mozilla/release-services/commit/f2d082a8dcfff3a7c92bb9ab7f22f67fed90abe9)|2018-10-29 09:37:54 
|14|Bastien Abadie|staticanalysis/frontend: Load all tasks & support http errors (#1651)|[URL](https://github.com/mozilla/release-services/commit/548dc131d79a2785a0987b5992d89291d9992b1d)|2018-10-26 09:44:46 
|13|Bastien Abadie|uplift/frontend: Display issue level & type for infer issues. (#1652)|[URL](https://github.com/mozilla/release-services/commit/ea7a20f9a77a8ab377e038b2188cff0e5a0191c7)|2018-10-25 20:06:50 
|12|Bastien Abadie|setup: bumping to v50 (#1639)|[URL](https://github.com/mozilla/release-services/commit/3b53407210704488fab2abd4e0bd35a68c518a09)|2018-10-25 19:58:05 
|11|ANdi|Add to logger if we don't have clang nor infer files into the revision. (#1648)|[URL](https://github.com/mozilla/release-services/commit/c301a08836d9f18a1e7dcdd8e706600942b8094d)|2018-10-25 19:23:32 
|10|Rail Aliiev|shipit/frontend: Revert "Use BACKEND_URL from data-shipit-api-url for accessing backend." (#1653)|[URL](https://github.com/mozilla/release-services/commit/f8066c3096e8c9880b4c21a37be887d2441fcc31)|2018-10-25 17:34:31 
|9|Marco|codecoverage/bot: Update ActiveData query URL (#1644)|[URL](https://github.com/mozilla/release-services/commit/c1721b62984da89dbb5c44047ad0593d086750dd)|2018-10-24 20:11:57 
|8|ANdi|staticanalysis/bot: Create gradle properties file that prevents gradle from running in daemon mode (#1643)|[URL](https://github.com/mozilla/release-services/commit/7fe5f92b5a5c8f0f277845c0f5e8b2df4a5cbabd)|2018-10-24 18:13:17 
|7|Marco|codecoverage/bot: Fix detection of Windows platforms (#1642)|[URL](https://github.com/mozilla/release-services/commit/1afa68a59e22e32de6ee26db267e021fe9b7d7bd)|2018-10-24 16:21:32 
|6|Marco| codecoverage/bot: Consider build machines as test platforms as they could contain coverage artifacts (#1637)|[URL](https://github.com/mozilla/release-services/commit/c5f3f6599c80120f33605f7f59d8f24bc9da472c)|2018-10-24 10:50:06 
|5|Rahul Verma|please_cli: Notify '#ci' and '#moc' IRC channels that deployment to production is about to start.(#1568) (#1634)|[URL](https://github.com/mozilla/release-services/commit/5216954426786b8f369e04878c3224db01082c1f)|2018-10-23 16:47:24 
|4|Tom Prince|shipit/frontend: Use URL from data-shipit-api-url for accessing backend. (#1636)|[URL](https://github.com/mozilla/release-services/commit/58e752dd7a5c558fc585b70b12eb4d3f5a2c57a9)|2018-10-23 16:19:37 
|3|Rahul Verma| staticanalysis/bot: Allow justifying clang-tidy checkers with a 'reason' text field #1556, fixes #1481|[URL](https://github.com/mozilla/release-services/commit/b0cc3616918877ebf5d7ce48e1320daf4b08859a)|2018-10-23 14:36:46 
|2|Bastien Abadie|uplift/frontend: Remove project #1638, fixes #1617|[URL](https://github.com/mozilla/release-services/commit/7cd5f1b68e984d52a3d3f00c9ab045ee97eec6fb)|2018-10-23 14:15:54 
|1|Bastien Abadie|staticanalysis/bot: Add localtime and zoneinfo for infer  (#1632)|[URL](https://github.com/mozilla/release-services/commit/1f47de56e6aa1552c3f88719e18bc9dd6faaad66)|2018-10-23 12:52:07 


