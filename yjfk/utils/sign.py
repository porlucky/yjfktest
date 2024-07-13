import hashlib
import urllib.parse
from urllib.parse import urlparse, unquote_plus
import random
import string


class DdConfigSign:
    @staticmethod
    def sign(jsticket, nonce_str, timestamp, url):
        plain = f"jsapi_ticket={jsticket}&noncestr={nonce_str}&timestamp={timestamp}&url={DdConfigSign.decode_url(url)}"
        sha1 = hashlib.sha256(plain.encode('utf-8')).digest()
        return DdConfigSign.byte_to_hex(sha1)

    @staticmethod
    def byte_to_hex(hash_bytes):
        return ''.join(['%02x' % b for b in hash_bytes])

    @staticmethod
    def decode_url(url):
        parsed_url = urlparse(url)
        url_buffer = [parsed_url.scheme, '://']
        if parsed_url.netloc:
            url_buffer.append(parsed_url.netloc)
        url_buffer.append(parsed_url.path)
        if parsed_url.query:
            url_buffer.append('?')
            url_buffer.append(urllib.parse.unquote_plus(parsed_url.query))
        return ''.join(url_buffer)

    @staticmethod
    def getRandomStr(count):
        base = string.ascii_letters + string.digits
        return ''.join(random.choice(base) for _ in range(count))
