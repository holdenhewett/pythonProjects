class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_addr):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_addr = ip_addr

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model         :{self.model}\n'\
               f'Software Version     :{self.swversion}\n'\
               f'Management IP Address:{self.ip_addr}'
        return desc

class Switch(Router):
    '''Switch Class'''
    def getdesc(self):
        '''return a formatted description of the switch'''
        desc = f'Switch Model         :{self.model}\n'\
                f'Software Version     :{self.swversion}\n'\
                f'Management IP Address:{self.ip_addr}'
        return desc