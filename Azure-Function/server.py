from cek import (Clova, SpeechBuilder, ResponseBuilder)

application_id = "" #ここにapplication-idをほりこむ
clova = Clova(
    application_id = application_id,
    default_language='ja',
    debug_mode=False)
speech_builder = SpeechBuilder(default_language='ja')
response_builder = ResponseBuilder(default_language='ja')

@clova.handle.launch
def launch_quest_handler(clova_request):
    text = "Report Funへようこそ！使いたい機能の名前を話してください。"
    response = response_builder.simple_speech_text(text)
    return response


@clova.handle.default
def default_handler(clova_request):
    return clova.response("上手く聞き取れませんでした。もう一度お願いします。")


@clova.handle.intent('Clova.GuideIntent'):
def Guide_intent_handler
