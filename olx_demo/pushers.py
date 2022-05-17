import pusher


def notify_me(my_event, message):
    pusher_client = pusher.Pusher(
      app_id='1410038',
      key='f0603427583c810bef7b',
      secret='a2d87ba81faafc0d82b6',
      cluster='ap2',
      ssl=True
    )

    pusher_client.trigger('my_channel', my_event, {'message': message})
