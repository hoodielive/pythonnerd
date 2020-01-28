def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value

def get_new_bookmark_data():
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False),
    }

def get_bookmark_id_for_deletion():
    return get_user_input('Enter a bookmark ID to delete.')

if __name__ == '__main__':
    ...
    'A': Option('Delete a bookmark.', commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
    ...
    'D': Option('Delete a bookmark.', commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
