from setuptools import setup, find_packages
from setuptools.command.install import install
import os


class CustomInstallCommand(install):
    """Customized setuptools install command - creates systemd service."""

    def run(self):
        install.run(self)
        service_content = """
        [Unit]
        Description=Flask Application
        After=network.target
        [Service]
        User=root
        WorkingDirectory=/home/pi/FlaskRGB-controller
        ExecStart=/usr/bin/python3 /home/pi/FlaskRGB-controller/app.py
        Restart=always
        [Install]
        WantedBy=multi-user.target
        """
        service_file_path = "/etc/systemd/system/flask_app.service"
        with open(service_file_path, "w") as service_file:
            service_file.write(service_content)

        # Reload systemd, enable and start the service
        os.system("systemctl daemon-reload")
        os.system("systemctl enable flask_app.service")
        os.system("systemctl start flask_app.service")


setup(
    name="flask_app",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Flask==2.0.1"],
    cmdclass={
        "install": CustomInstallCommand,
    },
)
