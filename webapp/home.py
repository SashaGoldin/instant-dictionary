import justpy as jp
from webapp import layout
from webapp import page

class Home(page.Page):

    path = "/"

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

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is Home Page", classes="text-4xl m-2")
        jp.Div(a=div, text="""This is some long text with the description of the Home Page""",
               classes="text-lg")
        return wp




