import slack
# import exception_slack
# import exception_slack1

class CreateChannelError(Exception):
    pass

class ChannelLengthError(Exception):
    pass

class slackChannel():

        def __init__(self,token):
            self.token = token

        def connection(self):
            client = slack.WebClient(token=self.token, run_async = True)
            return client

        def createchannel(self, channelname):
            try:
                if type(channelname) == int:
                    raise CreateChannelError
                elif len(channelname) > 10:
                    raise ChannelLengthError
                else:
                    value = slackChannel.connection(self)
                    value.groups_create(
                    name=channelname
                    )
            except CreateChannelError:
                print("Channel name cannot be a number!")
            except ChannelLengthError:
                print("Channel name character count exceeded!")
            except e:
                print("Exceptional Error")
