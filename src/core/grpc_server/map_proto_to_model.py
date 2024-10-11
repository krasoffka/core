from antifraud_service import models
from antifraud_service_proto import client_pb2 as client_pb

MAP_PROTO_TO_MODEL = {
    client_pb.CheckBlockRequisiteRequest: models.CheckBlockRequisite,
    client_pb.TemporaryBlockRequisiteRequest: models.TemporaryBlockRequisite,
}


def map_proto_to_model(proto):
    model = MAP_PROTO_TO_MODEL.get(type(proto), None)
    if model is None:
        raise NotImplementedError(f"Model for {type(proto)} is not implemented to MAP_PROTO_TO_MODEL")
    return model.from_proto(proto)
