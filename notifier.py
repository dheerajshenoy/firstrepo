
import gi 
gi.require_version('Gtk','3.0')
gi.require_version('Notify','0.7')
from gi.repository import Gtk,Notify 


class Timeit:
    def __init__(self):
        
        
        
        
        
        
        
        
    def notif(self):
        Notify.init('TIMEIT')
        N = Notify.Notification.new("TIMEIT","THAT'S WHAT SHE SAID")
        N.set_urgency(2)
        N.add_action("action_complete","Done",self.done)
        N.add_action("action_snooze","Snooze",self.snooze)
        N.show()
        Gtk.main()
    
    def done(self, notifyObj, action):
        print("Completed it! Nice")
        notifyObj.close()
        Gtk.main_quit()
        #notifyObj.close()
        
        
    def snooze(self, notifyObj, action):
        print("Snoozed it for 5 mins")
        notifyObj.close()
        Gtk.main_quit()#notifyObj.close()
    
if __name__ == "__main__":
    
    obj = Timeit()
    
