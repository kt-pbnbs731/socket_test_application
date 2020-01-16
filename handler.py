import socket

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    _server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print('Server Started')
        _server.bind(('0.0.0.0', 5555))
        _server.listen(5)
        print('Wait Client ...')
        # 接続待受
        _client, (_client_address, _client_port) = \
            _server.accept()

        # 受信したメッセージを出力
        recv_raw_msg = _client.recv(4096)
        recv_msg = recv_raw_msg.decode()
        print('Recv={}'.format(recv_msg))
        _client.send(recv_raw_msg)
        _client.close()
    except KeyboardInterrupt:
        print('Socket Server End')
    except Exception as err:
        print('Socket Server Error : {}'.format(err))
    finally:
        _server.close()

    return "Python serverless on Unubo Cloud."
