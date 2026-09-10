test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'volume': 'high'
}

def add_setting(settings, new_settings):
    key = new_settings[0].lower()
    value = new_settings[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_settings):
    key = new_settings[0].lower()
    value = new_settings[1].lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings, new_settings):
    key = new_settings.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return f"No settings available."
    else:

        result = "Current User Settings:"
        for key, value in settings.items():
            result += f"\n{key.capitalize()}: {value}"
        return result
        
print(view_settings(test_settings))
    

    
