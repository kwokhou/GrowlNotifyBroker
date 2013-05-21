import subprocess, sublime, sublime_plugin, os

class GrowlNotifyBroker(sublime_plugin.EventListener):
  def post_to_growl(self, title, msg):
		cmd = 'growlnotify.com /t:"'+title+'" "'+msg+'"'
		subprocess.call(cmd,shell=True)
		print title + "|growl|"+ msg
	def on_post_save(self, view):
		filename = os.path.basename(view.file_name())
		self.post_to_growl("Saved!", filename)
