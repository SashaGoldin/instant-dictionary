import justpy as jp
import definition
from webapp import layout
from webapp import page

class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        wp.head_html = """
                                <style>
                                .q-toolbar__title {
                                    flex: auto !important;
                                    margin-left: 10px;
                                }

                                .q-btn {
                                    flex: auto !important;
                                    margin-left: 10px;
                                }
                                </style>
                                """
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type", classes="text-lg")
        input_div = jp.Div(a=div, classes='grid grid-cols-2')
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40 bg-yellow-500")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 "
                                     "rounded w-64 focus:bg-white focus:outline-none "
                                     "focus:border-purple-500 py-2 px-4")
        input_box.on('input', cls.get_definition)

        # no need for btn, can handle instantly when user types
        # jp.Button(a=input_div, text='Get Definition', classes='border-2 text-gray-500', click=cls.get_definition,
        #           outputdiv=output_div, inputbox=input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
