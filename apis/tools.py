import hashlib
import urllib


class Tools:
    @classmethod
    def signature(cls, params):
        params = sorted(params.iteritems(), key=lambda d: d[0], reverse=False)
        message = urllib.urlencode(params)
        m = hashlib.md5()
        m.update(message)
        m.digest()
        sig = m.hexdigest()
        return sig
