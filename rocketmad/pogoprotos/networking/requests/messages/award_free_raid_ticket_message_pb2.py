# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/award_free_raid_ticket_message.proto

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
  name='pogoprotos/networking/requests/messages/award_free_raid_ticket_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/requests/messages/award_free_raid_ticket_message.proto\x12\'pogoprotos.networking.requests.messages\"d\n\x1a\x41wardFreeRaidTicketMessage\x12\x0e\n\x06gym_id\x18\x01 \x01(\t\x12\x1a\n\x12player_lat_degrees\x18\x02 \x01(\x01\x12\x1a\n\x12player_lng_degrees\x18\x03 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AWARDFREERAIDTICKETMESSAGE = _descriptor.Descriptor(
  name='AwardFreeRaidTicketMessage',
  full_name='pogoprotos.networking.requests.messages.AwardFreeRaidTicketMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_id', full_name='pogoprotos.networking.requests.messages.AwardFreeRaidTicketMessage.gym_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_lat_degrees', full_name='pogoprotos.networking.requests.messages.AwardFreeRaidTicketMessage.player_lat_degrees', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_lng_degrees', full_name='pogoprotos.networking.requests.messages.AwardFreeRaidTicketMessage.player_lng_degrees', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_end=221,
)

DESCRIPTOR.message_types_by_name['AwardFreeRaidTicketMessage'] = _AWARDFREERAIDTICKETMESSAGE

AwardFreeRaidTicketMessage = _reflection.GeneratedProtocolMessageType('AwardFreeRaidTicketMessage', (_message.Message,), dict(
  DESCRIPTOR = _AWARDFREERAIDTICKETMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.award_free_raid_ticket_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.AwardFreeRaidTicketMessage)
  ))
_sym_db.RegisterMessage(AwardFreeRaidTicketMessage)


# @@protoc_insertion_point(module_scope)