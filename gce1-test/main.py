import time
import endpoints

from protorpc import remote
from protorpc.message_types import DateTimeMessage
from protorpc.message_types import VoidMessage


@endpoints.api(name="gce1", version="v1", description="GCE 1.0 Test API",
               allowed_client_ids=[endpoints.API_EXPLORER_CLIENT_ID])
class Endpoints1TestApi(remote.Service):

  @endpoints.method(VoidMessage, DateTimeMessage, path='get_time', http_method='GET')
  def get_server_time(self, unused):
    return DateTimeMessage(milliseconds=int(time.time()*1000.0))


rpc_app = endpoints.api_server([Endpoints1TestApi])

