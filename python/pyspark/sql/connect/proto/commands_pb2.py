#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/commands.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyspark.sql.connect.proto import common_pb2 as spark_dot_connect_dot_common__pb2
from pyspark.sql.connect.proto import expressions_pb2 as spark_dot_connect_dot_expressions__pb2
from pyspark.sql.connect.proto import relations_pb2 as spark_dot_connect_dot_relations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cspark/connect/commands.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1aspark/connect/common.proto\x1a\x1fspark/connect/expressions.proto\x1a\x1dspark/connect/relations.proto"\x90\x06\n\x07\x43ommand\x12]\n\x11register_function\x18\x01 \x01(\x0b\x32..spark.connect.CommonInlineUserDefinedFunctionH\x00R\x10registerFunction\x12H\n\x0fwrite_operation\x18\x02 \x01(\x0b\x32\x1d.spark.connect.WriteOperationH\x00R\x0ewriteOperation\x12_\n\x15\x63reate_dataframe_view\x18\x03 \x01(\x0b\x32).spark.connect.CreateDataFrameViewCommandH\x00R\x13\x63reateDataframeView\x12O\n\x12write_operation_v2\x18\x04 \x01(\x0b\x32\x1f.spark.connect.WriteOperationV2H\x00R\x10writeOperationV2\x12<\n\x0bsql_command\x18\x05 \x01(\x0b\x32\x19.spark.connect.SqlCommandH\x00R\nsqlCommand\x12k\n\x1cwrite_stream_operation_start\x18\x06 \x01(\x0b\x32(.spark.connect.WriteStreamOperationStartH\x00R\x19writeStreamOperationStart\x12^\n\x17streaming_query_command\x18\x07 \x01(\x0b\x32$.spark.connect.StreamingQueryCommandH\x00R\x15streamingQueryCommand\x12X\n\x15get_resources_command\x18\x08 \x01(\x0b\x32".spark.connect.GetResourcesCommandH\x00R\x13getResourcesCommand\x12\x35\n\textension\x18\xe7\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\textensionB\x0e\n\x0c\x63ommand_type"\xb3\x01\n\nSqlCommand\x12\x10\n\x03sql\x18\x01 \x01(\tR\x03sql\x12\x37\n\x04\x61rgs\x18\x02 \x03(\x0b\x32#.spark.connect.SqlCommand.ArgsEntryR\x04\x61rgs\x1aZ\n\tArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x05value:\x02\x38\x01"\x96\x01\n\x1a\x43reateDataFrameViewCommand\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1b\n\tis_global\x18\x03 \x01(\x08R\x08isGlobal\x12\x18\n\x07replace\x18\x04 \x01(\x08R\x07replace"\x9b\x08\n\x0eWriteOperation\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1b\n\x06source\x18\x02 \x01(\tH\x01R\x06source\x88\x01\x01\x12\x14\n\x04path\x18\x03 \x01(\tH\x00R\x04path\x12?\n\x05table\x18\x04 \x01(\x0b\x32\'.spark.connect.WriteOperation.SaveTableH\x00R\x05table\x12:\n\x04mode\x18\x05 \x01(\x0e\x32&.spark.connect.WriteOperation.SaveModeR\x04mode\x12*\n\x11sort_column_names\x18\x06 \x03(\tR\x0fsortColumnNames\x12\x31\n\x14partitioning_columns\x18\x07 \x03(\tR\x13partitioningColumns\x12\x43\n\tbucket_by\x18\x08 \x01(\x0b\x32&.spark.connect.WriteOperation.BucketByR\x08\x62ucketBy\x12\x44\n\x07options\x18\t \x03(\x0b\x32*.spark.connect.WriteOperation.OptionsEntryR\x07options\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x82\x02\n\tSaveTable\x12\x1d\n\ntable_name\x18\x01 \x01(\tR\ttableName\x12X\n\x0bsave_method\x18\x02 \x01(\x0e\x32\x37.spark.connect.WriteOperation.SaveTable.TableSaveMethodR\nsaveMethod"|\n\x0fTableSaveMethod\x12!\n\x1dTABLE_SAVE_METHOD_UNSPECIFIED\x10\x00\x12#\n\x1fTABLE_SAVE_METHOD_SAVE_AS_TABLE\x10\x01\x12!\n\x1dTABLE_SAVE_METHOD_INSERT_INTO\x10\x02\x1a[\n\x08\x42ucketBy\x12.\n\x13\x62ucket_column_names\x18\x01 \x03(\tR\x11\x62ucketColumnNames\x12\x1f\n\x0bnum_buckets\x18\x02 \x01(\x05R\nnumBuckets"\x89\x01\n\x08SaveMode\x12\x19\n\x15SAVE_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SAVE_MODE_APPEND\x10\x01\x12\x17\n\x13SAVE_MODE_OVERWRITE\x10\x02\x12\x1d\n\x19SAVE_MODE_ERROR_IF_EXISTS\x10\x03\x12\x14\n\x10SAVE_MODE_IGNORE\x10\x04\x42\x0b\n\tsave_typeB\t\n\x07_source"\xad\x06\n\x10WriteOperationV2\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1d\n\ntable_name\x18\x02 \x01(\tR\ttableName\x12\x1f\n\x08provider\x18\x03 \x01(\tH\x00R\x08provider\x88\x01\x01\x12L\n\x14partitioning_columns\x18\x04 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x13partitioningColumns\x12\x46\n\x07options\x18\x05 \x03(\x0b\x32,.spark.connect.WriteOperationV2.OptionsEntryR\x07options\x12_\n\x10table_properties\x18\x06 \x03(\x0b\x32\x34.spark.connect.WriteOperationV2.TablePropertiesEntryR\x0ftableProperties\x12\x38\n\x04mode\x18\x07 \x01(\x0e\x32$.spark.connect.WriteOperationV2.ModeR\x04mode\x12J\n\x13overwrite_condition\x18\x08 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x12overwriteCondition\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x42\n\x14TablePropertiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\x9f\x01\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_CREATE\x10\x01\x12\x12\n\x0eMODE_OVERWRITE\x10\x02\x12\x1d\n\x19MODE_OVERWRITE_PARTITIONS\x10\x03\x12\x0f\n\x0bMODE_APPEND\x10\x04\x12\x10\n\x0cMODE_REPLACE\x10\x05\x12\x1a\n\x16MODE_CREATE_OR_REPLACE\x10\x06\x42\x0b\n\t_provider"\x82\x05\n\x19WriteStreamOperationStart\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x16\n\x06\x66ormat\x18\x02 \x01(\tR\x06\x66ormat\x12O\n\x07options\x18\x03 \x03(\x0b\x32\x35.spark.connect.WriteStreamOperationStart.OptionsEntryR\x07options\x12:\n\x19partitioning_column_names\x18\x04 \x03(\tR\x17partitioningColumnNames\x12:\n\x18processing_time_interval\x18\x05 \x01(\tH\x00R\x16processingTimeInterval\x12%\n\ravailable_now\x18\x06 \x01(\x08H\x00R\x0c\x61vailableNow\x12\x14\n\x04once\x18\x07 \x01(\x08H\x00R\x04once\x12\x46\n\x1e\x63ontinuous_checkpoint_interval\x18\x08 \x01(\tH\x00R\x1c\x63ontinuousCheckpointInterval\x12\x1f\n\x0boutput_mode\x18\t \x01(\tR\noutputMode\x12\x1d\n\nquery_name\x18\n \x01(\tR\tqueryName\x12\x14\n\x04path\x18\x0b \x01(\tH\x01R\x04path\x12\x1f\n\ntable_name\x18\x0c \x01(\tH\x01R\ttableName\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\t\n\x07triggerB\x12\n\x10sink_destination"y\n\x1fWriteStreamOperationStartResult\x12\x42\n\x08query_id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x07queryId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"A\n\x18StreamingQueryInstanceId\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06run_id\x18\x02 \x01(\tR\x05runId"\xf8\x04\n\x15StreamingQueryCommand\x12\x42\n\x08query_id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x07queryId\x12\x18\n\x06status\x18\x02 \x01(\x08H\x00R\x06status\x12%\n\rlast_progress\x18\x03 \x01(\x08H\x00R\x0clastProgress\x12)\n\x0frecent_progress\x18\x04 \x01(\x08H\x00R\x0erecentProgress\x12\x14\n\x04stop\x18\x05 \x01(\x08H\x00R\x04stop\x12\x34\n\x15process_all_available\x18\x06 \x01(\x08H\x00R\x13processAllAvailable\x12O\n\x07\x65xplain\x18\x07 \x01(\x0b\x32\x33.spark.connect.StreamingQueryCommand.ExplainCommandH\x00R\x07\x65xplain\x12\x1e\n\texception\x18\x08 \x01(\x08H\x00R\texception\x12k\n\x11\x61wait_termination\x18\t \x01(\x0b\x32<.spark.connect.StreamingQueryCommand.AwaitTerminationCommandH\x00R\x10\x61waitTermination\x1a,\n\x0e\x45xplainCommand\x12\x1a\n\x08\x65xtended\x18\x01 \x01(\x08R\x08\x65xtended\x1aL\n\x17\x41waitTerminationCommand\x12"\n\ntimeout_ms\x18\x02 \x01(\x03H\x00R\ttimeoutMs\x88\x01\x01\x42\r\n\x0b_timeout_msB\t\n\x07\x63ommand"\xf5\x08\n\x1bStreamingQueryCommandResult\x12\x42\n\x08query_id\x18\x01 \x01(\x0b\x32\'.spark.connect.StreamingQueryInstanceIdR\x07queryId\x12Q\n\x06status\x18\x02 \x01(\x0b\x32\x37.spark.connect.StreamingQueryCommandResult.StatusResultH\x00R\x06status\x12j\n\x0frecent_progress\x18\x03 \x01(\x0b\x32?.spark.connect.StreamingQueryCommandResult.RecentProgressResultH\x00R\x0erecentProgress\x12T\n\x07\x65xplain\x18\x04 \x01(\x0b\x32\x38.spark.connect.StreamingQueryCommandResult.ExplainResultH\x00R\x07\x65xplain\x12Z\n\texception\x18\x05 \x01(\x0b\x32:.spark.connect.StreamingQueryCommandResult.ExceptionResultH\x00R\texception\x12p\n\x11\x61wait_termination\x18\x06 \x01(\x0b\x32\x41.spark.connect.StreamingQueryCommandResult.AwaitTerminationResultH\x00R\x10\x61waitTermination\x1a\xaa\x01\n\x0cStatusResult\x12%\n\x0estatus_message\x18\x01 \x01(\tR\rstatusMessage\x12*\n\x11is_data_available\x18\x02 \x01(\x08R\x0fisDataAvailable\x12*\n\x11is_trigger_active\x18\x03 \x01(\x08R\x0fisTriggerActive\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActive\x1aH\n\x14RecentProgressResult\x12\x30\n\x14recent_progress_json\x18\x05 \x03(\tR\x12recentProgressJson\x1a\'\n\rExplainResult\x12\x16\n\x06result\x18\x01 \x01(\tR\x06result\x1a\xc5\x01\n\x0f\x45xceptionResult\x12\x30\n\x11\x65xception_message\x18\x01 \x01(\tH\x00R\x10\x65xceptionMessage\x88\x01\x01\x12$\n\x0b\x65rror_class\x18\x02 \x01(\tH\x01R\nerrorClass\x88\x01\x01\x12$\n\x0bstack_trace\x18\x03 \x01(\tH\x02R\nstackTrace\x88\x01\x01\x42\x14\n\x12_exception_messageB\x0e\n\x0c_error_classB\x0e\n\x0c_stack_trace\x1a\x38\n\x16\x41waitTerminationResult\x12\x1e\n\nterminated\x18\x01 \x01(\x08R\nterminatedB\r\n\x0bresult_type"\x15\n\x13GetResourcesCommand"\xd4\x01\n\x19GetResourcesCommandResult\x12U\n\tresources\x18\x01 \x03(\x0b\x32\x37.spark.connect.GetResourcesCommandResult.ResourcesEntryR\tresources\x1a`\n\x0eResourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32".spark.connect.ResourceInformationR\x05value:\x02\x38\x01\x42"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)


_COMMAND = DESCRIPTOR.message_types_by_name["Command"]
_SQLCOMMAND = DESCRIPTOR.message_types_by_name["SqlCommand"]
_SQLCOMMAND_ARGSENTRY = _SQLCOMMAND.nested_types_by_name["ArgsEntry"]
_CREATEDATAFRAMEVIEWCOMMAND = DESCRIPTOR.message_types_by_name["CreateDataFrameViewCommand"]
_WRITEOPERATION = DESCRIPTOR.message_types_by_name["WriteOperation"]
_WRITEOPERATION_OPTIONSENTRY = _WRITEOPERATION.nested_types_by_name["OptionsEntry"]
_WRITEOPERATION_SAVETABLE = _WRITEOPERATION.nested_types_by_name["SaveTable"]
_WRITEOPERATION_BUCKETBY = _WRITEOPERATION.nested_types_by_name["BucketBy"]
_WRITEOPERATIONV2 = DESCRIPTOR.message_types_by_name["WriteOperationV2"]
_WRITEOPERATIONV2_OPTIONSENTRY = _WRITEOPERATIONV2.nested_types_by_name["OptionsEntry"]
_WRITEOPERATIONV2_TABLEPROPERTIESENTRY = _WRITEOPERATIONV2.nested_types_by_name[
    "TablePropertiesEntry"
]
_WRITESTREAMOPERATIONSTART = DESCRIPTOR.message_types_by_name["WriteStreamOperationStart"]
_WRITESTREAMOPERATIONSTART_OPTIONSENTRY = _WRITESTREAMOPERATIONSTART.nested_types_by_name[
    "OptionsEntry"
]
_WRITESTREAMOPERATIONSTARTRESULT = DESCRIPTOR.message_types_by_name[
    "WriteStreamOperationStartResult"
]
_STREAMINGQUERYINSTANCEID = DESCRIPTOR.message_types_by_name["StreamingQueryInstanceId"]
_STREAMINGQUERYCOMMAND = DESCRIPTOR.message_types_by_name["StreamingQueryCommand"]
_STREAMINGQUERYCOMMAND_EXPLAINCOMMAND = _STREAMINGQUERYCOMMAND.nested_types_by_name[
    "ExplainCommand"
]
_STREAMINGQUERYCOMMAND_AWAITTERMINATIONCOMMAND = _STREAMINGQUERYCOMMAND.nested_types_by_name[
    "AwaitTerminationCommand"
]
_STREAMINGQUERYCOMMANDRESULT = DESCRIPTOR.message_types_by_name["StreamingQueryCommandResult"]
_STREAMINGQUERYCOMMANDRESULT_STATUSRESULT = _STREAMINGQUERYCOMMANDRESULT.nested_types_by_name[
    "StatusResult"
]
_STREAMINGQUERYCOMMANDRESULT_RECENTPROGRESSRESULT = (
    _STREAMINGQUERYCOMMANDRESULT.nested_types_by_name["RecentProgressResult"]
)
_STREAMINGQUERYCOMMANDRESULT_EXPLAINRESULT = _STREAMINGQUERYCOMMANDRESULT.nested_types_by_name[
    "ExplainResult"
]
_STREAMINGQUERYCOMMANDRESULT_EXCEPTIONRESULT = _STREAMINGQUERYCOMMANDRESULT.nested_types_by_name[
    "ExceptionResult"
]
_STREAMINGQUERYCOMMANDRESULT_AWAITTERMINATIONRESULT = (
    _STREAMINGQUERYCOMMANDRESULT.nested_types_by_name["AwaitTerminationResult"]
)
_GETRESOURCESCOMMAND = DESCRIPTOR.message_types_by_name["GetResourcesCommand"]
_GETRESOURCESCOMMANDRESULT = DESCRIPTOR.message_types_by_name["GetResourcesCommandResult"]
_GETRESOURCESCOMMANDRESULT_RESOURCESENTRY = _GETRESOURCESCOMMANDRESULT.nested_types_by_name[
    "ResourcesEntry"
]
_WRITEOPERATION_SAVETABLE_TABLESAVEMETHOD = _WRITEOPERATION_SAVETABLE.enum_types_by_name[
    "TableSaveMethod"
]
_WRITEOPERATION_SAVEMODE = _WRITEOPERATION.enum_types_by_name["SaveMode"]
_WRITEOPERATIONV2_MODE = _WRITEOPERATIONV2.enum_types_by_name["Mode"]
Command = _reflection.GeneratedProtocolMessageType(
    "Command",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMMAND,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Command)
    },
)
_sym_db.RegisterMessage(Command)

SqlCommand = _reflection.GeneratedProtocolMessageType(
    "SqlCommand",
    (_message.Message,),
    {
        "ArgsEntry": _reflection.GeneratedProtocolMessageType(
            "ArgsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SQLCOMMAND_ARGSENTRY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.SqlCommand.ArgsEntry)
            },
        ),
        "DESCRIPTOR": _SQLCOMMAND,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.SqlCommand)
    },
)
_sym_db.RegisterMessage(SqlCommand)
_sym_db.RegisterMessage(SqlCommand.ArgsEntry)

CreateDataFrameViewCommand = _reflection.GeneratedProtocolMessageType(
    "CreateDataFrameViewCommand",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEDATAFRAMEVIEWCOMMAND,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.CreateDataFrameViewCommand)
    },
)
_sym_db.RegisterMessage(CreateDataFrameViewCommand)

WriteOperation = _reflection.GeneratedProtocolMessageType(
    "WriteOperation",
    (_message.Message,),
    {
        "OptionsEntry": _reflection.GeneratedProtocolMessageType(
            "OptionsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _WRITEOPERATION_OPTIONSENTRY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.WriteOperation.OptionsEntry)
            },
        ),
        "SaveTable": _reflection.GeneratedProtocolMessageType(
            "SaveTable",
            (_message.Message,),
            {
                "DESCRIPTOR": _WRITEOPERATION_SAVETABLE,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.WriteOperation.SaveTable)
            },
        ),
        "BucketBy": _reflection.GeneratedProtocolMessageType(
            "BucketBy",
            (_message.Message,),
            {
                "DESCRIPTOR": _WRITEOPERATION_BUCKETBY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.WriteOperation.BucketBy)
            },
        ),
        "DESCRIPTOR": _WRITEOPERATION,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.WriteOperation)
    },
)
_sym_db.RegisterMessage(WriteOperation)
_sym_db.RegisterMessage(WriteOperation.OptionsEntry)
_sym_db.RegisterMessage(WriteOperation.SaveTable)
_sym_db.RegisterMessage(WriteOperation.BucketBy)

WriteOperationV2 = _reflection.GeneratedProtocolMessageType(
    "WriteOperationV2",
    (_message.Message,),
    {
        "OptionsEntry": _reflection.GeneratedProtocolMessageType(
            "OptionsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _WRITEOPERATIONV2_OPTIONSENTRY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.WriteOperationV2.OptionsEntry)
            },
        ),
        "TablePropertiesEntry": _reflection.GeneratedProtocolMessageType(
            "TablePropertiesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _WRITEOPERATIONV2_TABLEPROPERTIESENTRY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.WriteOperationV2.TablePropertiesEntry)
            },
        ),
        "DESCRIPTOR": _WRITEOPERATIONV2,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.WriteOperationV2)
    },
)
_sym_db.RegisterMessage(WriteOperationV2)
_sym_db.RegisterMessage(WriteOperationV2.OptionsEntry)
_sym_db.RegisterMessage(WriteOperationV2.TablePropertiesEntry)

WriteStreamOperationStart = _reflection.GeneratedProtocolMessageType(
    "WriteStreamOperationStart",
    (_message.Message,),
    {
        "OptionsEntry": _reflection.GeneratedProtocolMessageType(
            "OptionsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _WRITESTREAMOPERATIONSTART_OPTIONSENTRY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.WriteStreamOperationStart.OptionsEntry)
            },
        ),
        "DESCRIPTOR": _WRITESTREAMOPERATIONSTART,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.WriteStreamOperationStart)
    },
)
_sym_db.RegisterMessage(WriteStreamOperationStart)
_sym_db.RegisterMessage(WriteStreamOperationStart.OptionsEntry)

WriteStreamOperationStartResult = _reflection.GeneratedProtocolMessageType(
    "WriteStreamOperationStartResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _WRITESTREAMOPERATIONSTARTRESULT,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.WriteStreamOperationStartResult)
    },
)
_sym_db.RegisterMessage(WriteStreamOperationStartResult)

StreamingQueryInstanceId = _reflection.GeneratedProtocolMessageType(
    "StreamingQueryInstanceId",
    (_message.Message,),
    {
        "DESCRIPTOR": _STREAMINGQUERYINSTANCEID,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryInstanceId)
    },
)
_sym_db.RegisterMessage(StreamingQueryInstanceId)

StreamingQueryCommand = _reflection.GeneratedProtocolMessageType(
    "StreamingQueryCommand",
    (_message.Message,),
    {
        "ExplainCommand": _reflection.GeneratedProtocolMessageType(
            "ExplainCommand",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMAND_EXPLAINCOMMAND,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommand.ExplainCommand)
            },
        ),
        "AwaitTerminationCommand": _reflection.GeneratedProtocolMessageType(
            "AwaitTerminationCommand",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMAND_AWAITTERMINATIONCOMMAND,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommand.AwaitTerminationCommand)
            },
        ),
        "DESCRIPTOR": _STREAMINGQUERYCOMMAND,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommand)
    },
)
_sym_db.RegisterMessage(StreamingQueryCommand)
_sym_db.RegisterMessage(StreamingQueryCommand.ExplainCommand)
_sym_db.RegisterMessage(StreamingQueryCommand.AwaitTerminationCommand)

StreamingQueryCommandResult = _reflection.GeneratedProtocolMessageType(
    "StreamingQueryCommandResult",
    (_message.Message,),
    {
        "StatusResult": _reflection.GeneratedProtocolMessageType(
            "StatusResult",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMANDRESULT_STATUSRESULT,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommandResult.StatusResult)
            },
        ),
        "RecentProgressResult": _reflection.GeneratedProtocolMessageType(
            "RecentProgressResult",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMANDRESULT_RECENTPROGRESSRESULT,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommandResult.RecentProgressResult)
            },
        ),
        "ExplainResult": _reflection.GeneratedProtocolMessageType(
            "ExplainResult",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMANDRESULT_EXPLAINRESULT,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommandResult.ExplainResult)
            },
        ),
        "ExceptionResult": _reflection.GeneratedProtocolMessageType(
            "ExceptionResult",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMANDRESULT_EXCEPTIONRESULT,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommandResult.ExceptionResult)
            },
        ),
        "AwaitTerminationResult": _reflection.GeneratedProtocolMessageType(
            "AwaitTerminationResult",
            (_message.Message,),
            {
                "DESCRIPTOR": _STREAMINGQUERYCOMMANDRESULT_AWAITTERMINATIONRESULT,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommandResult.AwaitTerminationResult)
            },
        ),
        "DESCRIPTOR": _STREAMINGQUERYCOMMANDRESULT,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StreamingQueryCommandResult)
    },
)
_sym_db.RegisterMessage(StreamingQueryCommandResult)
_sym_db.RegisterMessage(StreamingQueryCommandResult.StatusResult)
_sym_db.RegisterMessage(StreamingQueryCommandResult.RecentProgressResult)
_sym_db.RegisterMessage(StreamingQueryCommandResult.ExplainResult)
_sym_db.RegisterMessage(StreamingQueryCommandResult.ExceptionResult)
_sym_db.RegisterMessage(StreamingQueryCommandResult.AwaitTerminationResult)

GetResourcesCommand = _reflection.GeneratedProtocolMessageType(
    "GetResourcesCommand",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETRESOURCESCOMMAND,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.GetResourcesCommand)
    },
)
_sym_db.RegisterMessage(GetResourcesCommand)

GetResourcesCommandResult = _reflection.GeneratedProtocolMessageType(
    "GetResourcesCommandResult",
    (_message.Message,),
    {
        "ResourcesEntry": _reflection.GeneratedProtocolMessageType(
            "ResourcesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY,
                "__module__": "spark.connect.commands_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.GetResourcesCommandResult.ResourcesEntry)
            },
        ),
        "DESCRIPTOR": _GETRESOURCESCOMMANDRESULT,
        "__module__": "spark.connect.commands_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.GetResourcesCommandResult)
    },
)
_sym_db.RegisterMessage(GetResourcesCommandResult)
_sym_db.RegisterMessage(GetResourcesCommandResult.ResourcesEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _SQLCOMMAND_ARGSENTRY._options = None
    _SQLCOMMAND_ARGSENTRY._serialized_options = b"8\001"
    _WRITEOPERATION_OPTIONSENTRY._options = None
    _WRITEOPERATION_OPTIONSENTRY._serialized_options = b"8\001"
    _WRITEOPERATIONV2_OPTIONSENTRY._options = None
    _WRITEOPERATIONV2_OPTIONSENTRY._serialized_options = b"8\001"
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._options = None
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._serialized_options = b"8\001"
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._options = None
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._serialized_options = b"8\001"
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._options = None
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._serialized_options = b"8\001"
    _COMMAND._serialized_start = 167
    _COMMAND._serialized_end = 951
    _SQLCOMMAND._serialized_start = 954
    _SQLCOMMAND._serialized_end = 1133
    _SQLCOMMAND_ARGSENTRY._serialized_start = 1043
    _SQLCOMMAND_ARGSENTRY._serialized_end = 1133
    _CREATEDATAFRAMEVIEWCOMMAND._serialized_start = 1136
    _CREATEDATAFRAMEVIEWCOMMAND._serialized_end = 1286
    _WRITEOPERATION._serialized_start = 1289
    _WRITEOPERATION._serialized_end = 2340
    _WRITEOPERATION_OPTIONSENTRY._serialized_start = 1764
    _WRITEOPERATION_OPTIONSENTRY._serialized_end = 1822
    _WRITEOPERATION_SAVETABLE._serialized_start = 1825
    _WRITEOPERATION_SAVETABLE._serialized_end = 2083
    _WRITEOPERATION_SAVETABLE_TABLESAVEMETHOD._serialized_start = 1959
    _WRITEOPERATION_SAVETABLE_TABLESAVEMETHOD._serialized_end = 2083
    _WRITEOPERATION_BUCKETBY._serialized_start = 2085
    _WRITEOPERATION_BUCKETBY._serialized_end = 2176
    _WRITEOPERATION_SAVEMODE._serialized_start = 2179
    _WRITEOPERATION_SAVEMODE._serialized_end = 2316
    _WRITEOPERATIONV2._serialized_start = 2343
    _WRITEOPERATIONV2._serialized_end = 3156
    _WRITEOPERATIONV2_OPTIONSENTRY._serialized_start = 1764
    _WRITEOPERATIONV2_OPTIONSENTRY._serialized_end = 1822
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._serialized_start = 2915
    _WRITEOPERATIONV2_TABLEPROPERTIESENTRY._serialized_end = 2981
    _WRITEOPERATIONV2_MODE._serialized_start = 2984
    _WRITEOPERATIONV2_MODE._serialized_end = 3143
    _WRITESTREAMOPERATIONSTART._serialized_start = 3159
    _WRITESTREAMOPERATIONSTART._serialized_end = 3801
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._serialized_start = 1764
    _WRITESTREAMOPERATIONSTART_OPTIONSENTRY._serialized_end = 1822
    _WRITESTREAMOPERATIONSTARTRESULT._serialized_start = 3803
    _WRITESTREAMOPERATIONSTARTRESULT._serialized_end = 3924
    _STREAMINGQUERYINSTANCEID._serialized_start = 3926
    _STREAMINGQUERYINSTANCEID._serialized_end = 3991
    _STREAMINGQUERYCOMMAND._serialized_start = 3994
    _STREAMINGQUERYCOMMAND._serialized_end = 4626
    _STREAMINGQUERYCOMMAND_EXPLAINCOMMAND._serialized_start = 4493
    _STREAMINGQUERYCOMMAND_EXPLAINCOMMAND._serialized_end = 4537
    _STREAMINGQUERYCOMMAND_AWAITTERMINATIONCOMMAND._serialized_start = 4539
    _STREAMINGQUERYCOMMAND_AWAITTERMINATIONCOMMAND._serialized_end = 4615
    _STREAMINGQUERYCOMMANDRESULT._serialized_start = 4629
    _STREAMINGQUERYCOMMANDRESULT._serialized_end = 5770
    _STREAMINGQUERYCOMMANDRESULT_STATUSRESULT._serialized_start = 5212
    _STREAMINGQUERYCOMMANDRESULT_STATUSRESULT._serialized_end = 5382
    _STREAMINGQUERYCOMMANDRESULT_RECENTPROGRESSRESULT._serialized_start = 5384
    _STREAMINGQUERYCOMMANDRESULT_RECENTPROGRESSRESULT._serialized_end = 5456
    _STREAMINGQUERYCOMMANDRESULT_EXPLAINRESULT._serialized_start = 5458
    _STREAMINGQUERYCOMMANDRESULT_EXPLAINRESULT._serialized_end = 5497
    _STREAMINGQUERYCOMMANDRESULT_EXCEPTIONRESULT._serialized_start = 5500
    _STREAMINGQUERYCOMMANDRESULT_EXCEPTIONRESULT._serialized_end = 5697
    _STREAMINGQUERYCOMMANDRESULT_AWAITTERMINATIONRESULT._serialized_start = 5699
    _STREAMINGQUERYCOMMANDRESULT_AWAITTERMINATIONRESULT._serialized_end = 5755
    _GETRESOURCESCOMMAND._serialized_start = 5772
    _GETRESOURCESCOMMAND._serialized_end = 5793
    _GETRESOURCESCOMMANDRESULT._serialized_start = 5796
    _GETRESOURCESCOMMANDRESULT._serialized_end = 6008
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._serialized_start = 5912
    _GETRESOURCESCOMMANDRESULT_RESOURCESENTRY._serialized_end = 6008
# @@protoc_insertion_point(module_scope)
