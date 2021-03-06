definition = {
    'node_batch_size': 50,
    'edge_size': 2000,
    'fields': {
        'admin_creator': {'omit': True},
        'application': {'omit': True},
        # Example: 10152641184872228_10152641800227228
        'attachment': {'omit_on_error': 1},
        'can_comment': {'omit': True},
        'can_hide': {'omit': True},
        'can_like': {'omit': True},
        'can_remove': {'omit': True},
        'can_reply_privately': {'omit': True},
        'comment_count': {},
        'comments': {'edge_type': 'comment'},
        'created_time': {'default': True},
        'from': {},
        'is_hidden': {'omit': True},
        'is_private': {'omit': True},
        'like_count': {},
        'likes': {},
        'live_broadcast_timestamp': {'omit': True},
        'message': {'default': True},
        'message_tags': {},
        # Example: 10151633674272733_30276158
        'object': {'edge_type': 'object', 'follow_edge': False, 'omit_on_error': 10},
        'parent': {'edge_type': 'comment'},
        'permalink_url': {'default': True},
        'private_reply_conversation': {'omit': True},
        'reactions': {},
        'user_likes': {'omit': True},
    },
    'csv_fields': [
        'created_time',
        'message',
        'permalink_url',
        {'parent_video_or_photo': ['object', 'id']},
        {'parent_comment': ['parent', 'id']},
        'comment_count',
        'like_count'
    ]
}
