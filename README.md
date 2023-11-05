# Configurable Bluetooth Receiver with Raspberry Pi Zero W and HiFiBerry DAC+

This project aims to create an affordable, configurable Bluetooth receiver using a Raspberry Pi Zero W running RaspiOS Bullseye and a HiFiBerry DAC+ Lite. It's designed to be simple to set up and use, requiring only a standard button and connection to an audio system via RCA cable. The receiver operates in a binary mode: ready to connect and play music or turned off.

## Features

- **Simple Control**: Toggle the speaker on and off with a physical button.
- **Easy Configuration**: Modify settings in `/boot/bt_config.ini` on the SD card when mounted on a PC.
- **Bluetooth Name Configuration**: Personalize the Bluetooth discovery name.
- **Startup and Shutdown Sounds**: Set custom sounds for turning on and off the receiver. These sounds must be in `.ogg` format and can be saved in the `/boot` directory for easy access.

## Installation

You have two methods to install the software for this project:

### Method 1: Manual Installation

1. Connect to your Raspberry Pi in a root session with `sudo -i`.
2. Execute the installation script:

```console
$ bash <(curl -s https://raw.githubusercontent.com/cynnfx/bt-speaker/master/install.sh)
```

3. To configure, copy the `bt_config.ini.default` file to `/boot/bt_config.ini` and edit as needed.

### Method 2: Prebuilt Image

1. Download the `.img.gz` file from this repository.
2. Flash it onto your SD card using a tool like rpi-imager.
3. Insert the SD card into your Raspberry Pi, and you're ready to go.

## Configuration File

The `bt_config.ini` file is located in the `/boot` directory, which is the mountable partition when the SD card is inserted into a PC. This makes it easy to change settings without needing to access the Raspberry Pi directly.

## Credits

This project is a fork of the `bt-speaker` repository originally created by [lukasjapan](https://github.com/lukasjapan). It relies heavily on his work, and many configurations are explained in his README. I have included an untouched version as `README.original` in this repository.

## License

GNU GENERAL PUBLIC LICENSE

## Contributing

I welcome contributions! Please feel free to submit pull requests or open issues for any improvements you suggest.

---

Enjoy your music wirelessly with this easily configurable Bluetooth receiver!
