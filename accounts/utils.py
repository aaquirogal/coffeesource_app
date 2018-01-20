import json

from steem import Steem
from app import settings


def get_user_posts(username, from_id, limit=60):
    s = Steem(nodes=settings.STEEM_NODES)

    blog_entries = s.get_blog(
        account=username,
        entry_id=from_id,
        limit=limit,
    )

    entries_list = []

    for entry in blog_entries:
        comment = entry['comment']

        # Could be util to load posts on utopian directly.
        # parent_permlink = comment.get('permlink')
        author = comment.get('author')

        if username == author:
            metadata = json.loads(comment.get('json_metadata'))
            category = comment.get('category')
            entry_dict = {
                'id': comment.get('id'),
                'title': comment.get('title'),
                'clickable': 'https://www.steemit.com/{0}/@{1}/{2}'.format(
                    category,
                    author,
                    comment.get('permlink'),
                ),
                'url': '/{0}/@{1}/{2}'.format(
                    category,
                    author,
                    comment.get('permlink'),
                ),
                'author': author,
                'category': category,
                'tags': metadata.get('tags'),
                'images': metadata.get('image'),
                'entry_id': entry['entry_id']
            }

            entries_list.append(entry_dict)

    return entries_list
