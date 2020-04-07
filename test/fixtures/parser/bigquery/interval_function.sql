SELECT
    TIMESTAMP_TRUNC(TIMESTAMP_ADD(session_start.eventTimestamp, INTERVAL cast(TIMESTAMP_DIFF(session_end.eventTimestamp, session_start.eventTimestamp, SECOND)/2 AS int64) second), HOUR) AS avgAtHour
FROM dummy;