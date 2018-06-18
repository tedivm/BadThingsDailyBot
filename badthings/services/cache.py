from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from badthings import app

cache_root = app.config['general'].get('filecache', '/tmp/badthings')

cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': cache_root + '/data',
    'cache.expire': 3600,
    'cache.lock_dir': cache_root + '/lock'
}

cache = CacheManager(**parse_cache_config_options(cache_opts))
