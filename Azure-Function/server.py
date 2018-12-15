from cek import (Clova, SpeechBuilder, ResponseBuilder)
import logging
import random

logger = logging.getLogger("Report Fun for Clova")
application_id = "" #ここにapplication-idをほりこむ
clova = Clova(
    application_id = application_id,
    default_language='ja',
    debug_mode=False)
speech_builder = SpeechBuilder(default_language='ja')
response_builder = ResponseBuilder(default_language='ja')

cheer_words = ["頑張れ！","ファイト！","ダミー3"]

@clova.handle.launch
def launch_quest_handler(clova_request):
    text = "Report Funへようこそ！使いたい機能の名前を話してください。"
    response = response_builder.simple_speech_text(text)
    return response


@clova.handle.default
def default_handler(clova_request):
    return clova.response("上手く聞き取れませんでした。もう一度お願いします。")


@clova.handle.intent('Clova.GuideIntent')
def guide_intent_handler(clova_request):
    text = "Report Fun for Clovaには応援機能、集中を助けるBGM再生機能、期限が迫っているレポートのリマインド機能があります。応援機能を使うには「応援して」、BGMを再生する場合には「集中BGMをかけて」、期限が迫っているレポートを確認したい場合は「期限が迫っているレポートを教えて」と話してください。"
    response = response_builder.simple_speech_text(text)
    return response


@clova.handle.intent('Clova.CancelIntent')
def cancel_intent_handler(clova_request):
    logger.info("User canceled the Service.")


@clova.handle.intent('ReportRemindIntent')
def report_remind_intent_handler(clova_request):
    return 1


@clova.handle.intent('CheerIntent')
def cheer_intent_handler(clova_request):
    text = cheer_words[random.randint(0,len(cheer_words)-1)]
    response = response_builder.simple_speech_text(text)
    return response


@clova.handle.intent('ReadVoiceIntent')
def read_voice_intent_handler(clova_request):
    return 1





