import sublime, sublime_plugin, base64, SublimeSelections;

def output_text(self, text):
	v = self.view.window().get_output_panel("Base64");
	# v.set_syntax_file("Packages/Javascript/Javascript.tmLanguage");

	edit = v.begin_edit("Base64");
	amount = v.insert(edit, 0, text);
	v.end_edit(edit);

	v.sel().clear();
	v.sel().add(sublime.Region(0, amount));

	self.view.window().run_command("show_panel", {"panel": "output.Base64"});
	self.view.window().focus_view(v);


class base64EncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selectiontext = SublimeSelections.get_selection_text();
		textlist = [];

		for text in selectiontext:
			textlist.append(base64.b64encode(text));

		output_text(self, "\n".join(textlist));

class base64DecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.sel()) and self.view.sel()[0].empty() == 1:
			def on_done(str):
				output_text(self, base64.b64decode(str));

			def on_change(str):
				pass;

			def on_cancel():
				pass;

			self.view.window().show_input_panel("Text to base64 decode", "", on_done, on_change, on_cancel);

		else:
			selectiontext = SublimeSelections.get_selection_text();
			textlist = [];

			for text in selectiontext:
				textlist.append(base64.b64decode(text));

			output_text(self, "\n".join(textlist));
