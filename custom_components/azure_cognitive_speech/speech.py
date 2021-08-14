import time
import requests
import logging
from .const import (
    DOMAIN, DEFAULT_VOICE,
    ENDPOINT_URI, TTS_URL,
    TOKEN_OUTDATE, VOICES_LIST)

_LOGGER = logging.getLogger(__name__)


class CognitiveToken:
    def __init__(self, hass, region, apikey):
        if DOMAIN not in hass.data:
            hass.data[DOMAIN] = {}
        if apikey not in hass.data[DOMAIN]:
            hass.data[DOMAIN][apikey] = {}
        self._data = hass.data[DOMAIN][apikey]
        self._region = region
        self._apikey = apikey

    def refresh_token(self):
        headers = {"Ocp-Apim-Subscription-Key": self._apikey}
        try:
            r = requests.post(ENDPOINT_URI.format(self._region), headers=headers, timeout=10)
            if r.status_code == 200:
                _LOGGER.debug(f"Refresh token successful")
                return r.text
            else:
                _LOGGER.debug(f"Refresh token failed, reason: {r.reason}")
        except Exception as e:
            _LOGGER.debug(f"Refresh token failed, reason: {e}")
        return None

    def get_token(self):
        if "outdate" in self._data and self._data["outdate"] < time.time():
            token = self._data["toekn"]
        else:
            token = self.refresh_token()
            if token is not None:
                self._data["outdate"] = time.time() + TOKEN_OUTDATE
                self._data["toekn"] = token
        return token


class CognitiveSpeech:
    def __init__(self, hass, region, apikey, default_voice):
        self._token = CognitiveToken(hass, region, apikey)
        self._apikey = apikey
        self._region = region
        self._default_voice = default_voice

    def ssml_gen(self, text, voice=DEFAULT_VOICE, speed=0, style=None, role=None):
        if self._default_voice in VOICES_LIST:
            cur_voice = VOICES_LIST[self._default_voice]
        else:
            cur_voice = VOICES_LIST[DEFAULT_VOICE]
        ssml_speed = 0
        ssml_style = None
        ssml_role = None
        if voice is not None and voice in VOICES_LIST:
            cur_voice = VOICES_LIST[voice]
        if speed is not None and -5 <= speed <= 5:
            ssml_speed = speed
        if style is not None and "StyleList" in cur_voice and style in cur_voice["StyleList"]:
            ssml_style = style
        if role is not None and "RolePlayList" in cur_voice and role in cur_voice["RolePlayList"]:
            ssml_role = role
        if ssml_style is not None or ssml_role is not None:
            ssml_style_seg = ""
            ssml_role_seg = ""
            if ssml_style is not None:
                ssml_style_seg = f" style ='{ssml_style}' styledegree = '2'"
            if ssml_role is not None:
                ssml_role_seg = f" role='{ssml_role}'"
            ssml_mstts_seg = f"<mstts:express-as{ssml_style_seg}{ssml_role_seg}>{text}</mstts:express-as>"
            ssml_mstts_head = " xmlns:mstts='https://www.w3.org/2001/mstts'"
        else:
            ssml_mstts_seg = text
            ssml_mstts_head = ""
        if ssml_speed != 0:
            ssml_rate = f"{'+' if ssml_speed >= 0 else ''}{ssml_speed * 10}%"
            ssml_prosody_seg = f"<prosody rate='{ssml_rate}'>{ssml_mstts_seg}</prosody>"
        else:
            ssml_prosody_seg = ssml_mstts_seg
        ssml_voice_seg = f"<voice xml:lang='{cur_voice['Locale']}' xml:gender='{cur_voice['Gender']}' " \
                         f"name='{cur_voice['ShortName']}'>{ssml_prosody_seg}</voice>"
        ssml = f"<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis'{ssml_mstts_head} xml:lang='{cur_voice['Locale']}'>" \
               f"{ssml_voice_seg}</speak>"
        _LOGGER.debug(f"SSML: {ssml}")
        return ssml

    def speech(self, text, voice, speed=0, style=None, role=None):
        token = self._token.get_token()
        ssml = self.ssml_gen(text, voice=voice, speed=speed, style=style, role=role)
        headers = {
            "authorization": f"Bearer {token}",
            "content-type": "application/ssml+xml",
            "x-microsoft-outputformat": "audio-16khz-32kbitrate-mono-mp3"
        }
        try:
            r = requests.post(TTS_URL.format(self._region), headers=headers, data=ssml.encode('utf-8'), timeout=10)
            if r.status_code == 200:
                return r.content
            else:
                _LOGGER.debug(f"Text to speech failed, reason: {r.reason}")
        except Exception as e:
            _LOGGER.debug(f"Text to speech failed, reason: {e}")
            pass
        return None
