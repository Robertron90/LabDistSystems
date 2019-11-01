## rs.config()
```
{
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "host1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "host2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "host3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbc916f4fb2580b5cdbe488")
        }
}
```

## rs.status()
```
{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T20:29:24.719Z"),
        "myState" : 1,
        "term" : NumberLong(1),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572640159, 1),
                        "t" : NumberLong(1)
                },
                "lastCommittedWallTime" : ISODate("2019-11-01T20:29:19.890Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572640159, 1),
                        "t" : NumberLong(1)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-01T20:29:19.890Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572640159, 1),
                        "t" : NumberLong(1)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572640159, 1),
                        "t" : NumberLong(1)
                },
                "lastAppliedWallTime" : ISODate("2019-11-01T20:29:19.890Z"),
                "lastDurableWallTime" : ISODate("2019-11-01T20:29:19.890Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572640119, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572640119, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "electionTimeout",
                "lastElectionDate" : ISODate("2019-11-01T20:11:38.842Z"),
                "termAtElection" : NumberLong(1),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(0, 0),
                        "t" : NumberLong(-1)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572639087, 1),
                        "t" : NumberLong(-1)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "numCatchUpOps" : NumberLong(27017),
                "newTermStartDate" : ISODate("2019-11-01T20:11:39.859Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T20:11:40.726Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "host1:27017",
                        "ip" : "172.31.46.38",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 1184,
                        "optime" : {
                                "ts" : Timestamp(1572640159, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:29:19Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572639098, 1),
                        "electionDate" : ISODate("2019-11-01T20:11:38Z"),
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "host2:27017",
                        "ip" : "172.31.33.48",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1076,
                        "optime" : {
                                "ts" : Timestamp(1572640159, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572640159, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:29:19Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T20:29:19Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T20:29:23.002Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T20:29:22.747Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "host1:27017",
                        "syncSourceHost" : "host1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                },
                {
                        "_id" : 2,
                        "name" : "host3:27017",
                        "ip" : "172.31.44.43",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1076,
                        "optime" : {
                                "ts" : Timestamp(1572640159, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572640159, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:29:19Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T20:29:19Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T20:29:23.002Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T20:29:22.746Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "host1:27017",
                        "syncSourceHost" : "host1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572640159, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572640159, 1)
}
```

![Image]{https://github.com/Robertron90/LabDistSystems/master/Lab9/chat.jpg}
