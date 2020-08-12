# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: warp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='warp.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nwarp.proto\"<\n\x11RemoteMachineInfo\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"+\n\x13RemoteMachineAvatar\x12\x14\n\x0c\x61vatar_chunk\x18\x01 \x01(\x0c\"/\n\nLookupName\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rreadable_name\x18\x02 \x01(\t\"\x1e\n\nHaveDuplex\x12\x10\n\x08response\x18\x02 \x01(\x08\"\x19\n\x08VoidType\x12\r\n\x05\x64ummy\x18\x01 \x01(\x05\"A\n\x06OpInfo\x12\r\n\x05ident\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x15\n\rreadable_name\x18\x03 \x01(\t\"0\n\x08StopInfo\x12\x15\n\x04info\x18\x01 \x01(\x0b\x32\x07.OpInfo\x12\r\n\x05\x65rror\x18\x02 \x01(\x08\"\xd0\x01\n\x11TransferOpRequest\x12\x15\n\x04info\x18\x01 \x01(\x0b\x32\x07.OpInfo\x12\x13\n\x0bsender_name\x18\x02 \x01(\t\x12\x15\n\rreceiver_name\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\x04\x12\r\n\x05\x63ount\x18\x06 \x01(\x04\x12\x16\n\x0ename_if_single\x18\x07 \x01(\t\x12\x16\n\x0emime_if_single\x18\x08 \x01(\t\x12\x19\n\x11top_dir_basenames\x18\t \x03(\t\"\\\n\tFileChunk\x12\x15\n\rrelative_path\x18\x01 \x01(\t\x12\x11\n\tfile_type\x18\x02 \x01(\x05\x12\x16\n\x0esymlink_target\x18\x03 \x01(\t\x12\r\n\x05\x63hunk\x18\x04 \x01(\x0c\x32\xf3\x03\n\x04Warp\x12\x33\n\x15\x43heckDuplexConnection\x12\x0b.LookupName\x1a\x0b.HaveDuplex\"\x00\x12\x39\n\x14GetRemoteMachineInfo\x12\x0b.LookupName\x1a\x12.RemoteMachineInfo\"\x00\x12?\n\x16GetRemoteMachineAvatar\x12\x0b.LookupName\x1a\x14.RemoteMachineAvatar\"\x00\x30\x01\x12;\n\x18ProcessTransferOpRequest\x12\x12.TransferOpRequest\x1a\t.VoidType\"\x00\x12\'\n\x0fPauseTransferOp\x12\x07.OpInfo\x1a\t.VoidType\"\x00\x12/\n\x17\x41\x63\x63\x65ptTransferOpRequest\x12\x07.OpInfo\x1a\t.VoidType\"\x00\x12(\n\rStartTransfer\x12\x07.OpInfo\x1a\n.FileChunk\"\x00\x30\x01\x12/\n\x17\x43\x61ncelTransferOpRequest\x12\x07.OpInfo\x1a\t.VoidType\"\x00\x12&\n\x0cStopTransfer\x12\t.StopInfo\x1a\t.VoidType\"\x00\x12 \n\x04Ping\x12\x0b.LookupName\x1a\t.VoidType\"\x00\x62\x06proto3')
)




_REMOTEMACHINEINFO = _descriptor.Descriptor(
  name='RemoteMachineInfo',
  full_name='RemoteMachineInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display_name', full_name='RemoteMachineInfo.display_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='RemoteMachineInfo.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=74,
)


_REMOTEMACHINEAVATAR = _descriptor.Descriptor(
  name='RemoteMachineAvatar',
  full_name='RemoteMachineAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar_chunk', full_name='RemoteMachineAvatar.avatar_chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=119,
)


_LOOKUPNAME = _descriptor.Descriptor(
  name='LookupName',
  full_name='LookupName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LookupName.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readable_name', full_name='LookupName.readable_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=168,
)


_HAVEDUPLEX = _descriptor.Descriptor(
  name='HaveDuplex',
  full_name='HaveDuplex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='HaveDuplex.response', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=200,
)


_VOIDTYPE = _descriptor.Descriptor(
  name='VoidType',
  full_name='VoidType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dummy', full_name='VoidType.dummy', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=227,
)


_OPINFO = _descriptor.Descriptor(
  name='OpInfo',
  full_name='OpInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ident', full_name='OpInfo.ident', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='OpInfo.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readable_name', full_name='OpInfo.readable_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=294,
)


_STOPINFO = _descriptor.Descriptor(
  name='StopInfo',
  full_name='StopInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='StopInfo.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='StopInfo.error', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=344,
)


_TRANSFEROPREQUEST = _descriptor.Descriptor(
  name='TransferOpRequest',
  full_name='TransferOpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='TransferOpRequest.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='TransferOpRequest.sender_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_name', full_name='TransferOpRequest.receiver_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='TransferOpRequest.receiver', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='TransferOpRequest.size', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='TransferOpRequest.count', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_if_single', full_name='TransferOpRequest.name_if_single', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mime_if_single', full_name='TransferOpRequest.mime_if_single', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_dir_basenames', full_name='TransferOpRequest.top_dir_basenames', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=555,
)


_FILECHUNK = _descriptor.Descriptor(
  name='FileChunk',
  full_name='FileChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relative_path', full_name='FileChunk.relative_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_type', full_name='FileChunk.file_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symlink_target', full_name='FileChunk.symlink_target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk', full_name='FileChunk.chunk', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=649,
)

_STOPINFO.fields_by_name['info'].message_type = _OPINFO
_TRANSFEROPREQUEST.fields_by_name['info'].message_type = _OPINFO
DESCRIPTOR.message_types_by_name['RemoteMachineInfo'] = _REMOTEMACHINEINFO
DESCRIPTOR.message_types_by_name['RemoteMachineAvatar'] = _REMOTEMACHINEAVATAR
DESCRIPTOR.message_types_by_name['LookupName'] = _LOOKUPNAME
DESCRIPTOR.message_types_by_name['HaveDuplex'] = _HAVEDUPLEX
DESCRIPTOR.message_types_by_name['VoidType'] = _VOIDTYPE
DESCRIPTOR.message_types_by_name['OpInfo'] = _OPINFO
DESCRIPTOR.message_types_by_name['StopInfo'] = _STOPINFO
DESCRIPTOR.message_types_by_name['TransferOpRequest'] = _TRANSFEROPREQUEST
DESCRIPTOR.message_types_by_name['FileChunk'] = _FILECHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoteMachineInfo = _reflection.GeneratedProtocolMessageType('RemoteMachineInfo', (_message.Message,), dict(
  DESCRIPTOR = _REMOTEMACHINEINFO,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:RemoteMachineInfo)
  ))
_sym_db.RegisterMessage(RemoteMachineInfo)

RemoteMachineAvatar = _reflection.GeneratedProtocolMessageType('RemoteMachineAvatar', (_message.Message,), dict(
  DESCRIPTOR = _REMOTEMACHINEAVATAR,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:RemoteMachineAvatar)
  ))
_sym_db.RegisterMessage(RemoteMachineAvatar)

LookupName = _reflection.GeneratedProtocolMessageType('LookupName', (_message.Message,), dict(
  DESCRIPTOR = _LOOKUPNAME,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:LookupName)
  ))
_sym_db.RegisterMessage(LookupName)

HaveDuplex = _reflection.GeneratedProtocolMessageType('HaveDuplex', (_message.Message,), dict(
  DESCRIPTOR = _HAVEDUPLEX,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:HaveDuplex)
  ))
_sym_db.RegisterMessage(HaveDuplex)

VoidType = _reflection.GeneratedProtocolMessageType('VoidType', (_message.Message,), dict(
  DESCRIPTOR = _VOIDTYPE,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:VoidType)
  ))
_sym_db.RegisterMessage(VoidType)

OpInfo = _reflection.GeneratedProtocolMessageType('OpInfo', (_message.Message,), dict(
  DESCRIPTOR = _OPINFO,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:OpInfo)
  ))
_sym_db.RegisterMessage(OpInfo)

StopInfo = _reflection.GeneratedProtocolMessageType('StopInfo', (_message.Message,), dict(
  DESCRIPTOR = _STOPINFO,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:StopInfo)
  ))
_sym_db.RegisterMessage(StopInfo)

TransferOpRequest = _reflection.GeneratedProtocolMessageType('TransferOpRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFEROPREQUEST,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:TransferOpRequest)
  ))
_sym_db.RegisterMessage(TransferOpRequest)

FileChunk = _reflection.GeneratedProtocolMessageType('FileChunk', (_message.Message,), dict(
  DESCRIPTOR = _FILECHUNK,
  __module__ = 'warp_pb2'
  # @@protoc_insertion_point(class_scope:FileChunk)
  ))
_sym_db.RegisterMessage(FileChunk)



_WARP = _descriptor.ServiceDescriptor(
  name='Warp',
  full_name='Warp',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=652,
  serialized_end=1151,
  methods=[
  _descriptor.MethodDescriptor(
    name='CheckDuplexConnection',
    full_name='Warp.CheckDuplexConnection',
    index=0,
    containing_service=None,
    input_type=_LOOKUPNAME,
    output_type=_HAVEDUPLEX,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRemoteMachineInfo',
    full_name='Warp.GetRemoteMachineInfo',
    index=1,
    containing_service=None,
    input_type=_LOOKUPNAME,
    output_type=_REMOTEMACHINEINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRemoteMachineAvatar',
    full_name='Warp.GetRemoteMachineAvatar',
    index=2,
    containing_service=None,
    input_type=_LOOKUPNAME,
    output_type=_REMOTEMACHINEAVATAR,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessTransferOpRequest',
    full_name='Warp.ProcessTransferOpRequest',
    index=3,
    containing_service=None,
    input_type=_TRANSFEROPREQUEST,
    output_type=_VOIDTYPE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PauseTransferOp',
    full_name='Warp.PauseTransferOp',
    index=4,
    containing_service=None,
    input_type=_OPINFO,
    output_type=_VOIDTYPE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AcceptTransferOpRequest',
    full_name='Warp.AcceptTransferOpRequest',
    index=5,
    containing_service=None,
    input_type=_OPINFO,
    output_type=_VOIDTYPE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartTransfer',
    full_name='Warp.StartTransfer',
    index=6,
    containing_service=None,
    input_type=_OPINFO,
    output_type=_FILECHUNK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelTransferOpRequest',
    full_name='Warp.CancelTransferOpRequest',
    index=7,
    containing_service=None,
    input_type=_OPINFO,
    output_type=_VOIDTYPE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopTransfer',
    full_name='Warp.StopTransfer',
    index=8,
    containing_service=None,
    input_type=_STOPINFO,
    output_type=_VOIDTYPE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='Warp.Ping',
    index=9,
    containing_service=None,
    input_type=_LOOKUPNAME,
    output_type=_VOIDTYPE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WARP)

DESCRIPTOR.services_by_name['Warp'] = _WARP

# @@protoc_insertion_point(module_scope)
