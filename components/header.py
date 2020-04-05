import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='http://logonoid.com/images/vanguard-logo.png', height='40', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/dash-vanguard-report/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Vanguard 500 Index Fund Investor Shares')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/dash-vanguard-report/overview', className="tab first"),

        dcc.Link('Price Performance   ', href='/dash-vanguard-report/price-performance', className="tab"),

        dcc.Link('Portfolio & Management   ', href='/dash-vanguard-report/portfolio-management', className="tab"),

        dcc.Link('Fees & Minimums   ', href='/dash-vanguard-report/fees', className="tab"),

        dcc.Link('Distributions   ', href='/dash-vanguard-report/distributions', className="tab"),

        dcc.Link('News & Reviews   ', href='/dash-vanguard-report/news-and-reviews', className="tab")

    ], className="row ")
    return menu
