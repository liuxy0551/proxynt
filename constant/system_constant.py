class SystemConstant:
    CHUNK_SIZE = 65536 * 8
    DEFAULT_TIMEOUT = 0.5

    HEART_BEAT_INTERVAL = 5

    MAX_HEART_BEAT_SECONDS = 60  # 超过一定秒数没有心跳就关闭
