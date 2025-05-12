USE PoC_DB;
GO
CREATE TABLE etl_table (
  id INT PRIMARY KEY,
  value INT,
  value_transformed INT
);
CREATE TABLE HealthMetrics (
  Timestamp DATETIME,
  CPU FLOAT,
  FreeMemory INT
);
CREATE TABLE batch_logs (
  cpu FLOAT,
  memory_free INT,
  duration_seconds FLOAT,
  failed BIT
);