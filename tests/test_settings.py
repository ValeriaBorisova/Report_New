from fixtures.models.settings_model import SettingsData


class TestSettings:
    def test_settings_with_valid_data(self, app, user_data):

        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        4. Open settings
        5. Add new settings
        """

        app.open_login_page()
        app.login.auth( data=user_data, is_submit=True)
        app.open_settings_page()
        data = SettingsData.random()
        app.settings.add_settings(data = data)
        assert 1 == 1