from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

SHORT_RETENTION_POLICY = getattr(
    settings, 'OPENWISP_MONITORING_SHORT_RETENTION_POLICY', '24h0m0s'
)
CRITICAL_DEVICE_METRICS = getattr(
    settings,
    'OPENWISP_MONITORING_CRITICAL_DEVICE_METRICS',
    [{'key': 'ping', 'field_name': 'reachable'}],
)
HEALTH_STATUS_LABELS = getattr(
    settings,
    'OPENWISP_MONITORING_HEALTH_STATUS_LABELS',
    {'unknown': 'unknown', 'ok': 'ok', 'problem': 'problem', 'critical': 'critical'},
)
MANAGEMENT_IP_ONLY = getattr(settings, 'OPENWISP_MONITORING_MANAGEMENT_IP_ONLY', True)

# Triggers spontaneous recovery of device based on corresponding signals
DEVICE_RECOVERY_DETECTION = getattr(
    settings, 'OPENWISP_MONITORING_DEVICE_RECOVERY_DETECTION', True
)

for item in CRITICAL_DEVICE_METRICS:  # pragma: no-cover
    if not all(['key' in item, 'field_name' in item]):
        raise ImproperlyConfigured(
            'OPENWISP_MONITORING_CRITICAL_DEVICE_METRICS contains invalid items'
        )

try:
    assert 'unknown' in HEALTH_STATUS_LABELS
    assert 'ok' in HEALTH_STATUS_LABELS
    assert 'problem' in HEALTH_STATUS_LABELS
    assert 'critical' in HEALTH_STATUS_LABELS
except AssertionError:  # pragma: no-cover
    raise ImproperlyConfigured(
        'OPENWISP_MONITORING_HEALTH_STATUS_LABELS must contain the following '
        'keys: unknown, ok, problem, critical'
    )
