import sublime, sublime_plugin;

def get_all_selections():
	"""
	Returns non-empty selections
	"""
	view = sublime.active_window().active_view();

	viewselections = view.sel();
	selections = [];

	if len(viewselections) == 1:
		if viewselections[0].empty():
			return [sublime.Region(0, view.size())];
		else:
			return [viewselections[0]];

	for i in range(len(viewselections)):
		s = viewselections[i];

		if not s.empty():
			selections.append(s);

	if not len(selections):
		return [sublime.Region(0, view.size())];

	else:
		return selections;

def get_selection_text():
	"""
	Returns non-empty selection text
	"""
	view = sublime.active_window().active_view();

	viewselections = get_all_selections();
	selections = [];

	for s in viewselections:
		selections.append(view.substr(s));

	return selections;

def get_first_selection():
	"""
	Returns first selection. If first selection is empty, returns the entire buffer selection.
	"""
	view = sublime.active_window().active_view();

	firstselection = view.sel()[0];
	if firstselection.empty():
		return sublime.Region(0, view.size());
	else:
		return firstselection;

def get_first_text():
	"""
	Returns first selection text
	"""
	view = sublime.active_window().active_view();

	return view.substr(get_first_selection());
