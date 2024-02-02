from app import *
from assets.menu_styles import *
from utils.functions import *

from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import os
from dotenv import load_dotenv

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

load_dotenv()

# definicao da chave da API


try:
    df_historico_msgs = pd.read_csv("data/historical_msgs.csv", index_col=0)

except:
    df_historico_msgs = pd.DataFrame(columns=["user", "chatGPT"])

try:
    sectors_df = pd.read_csv("data/sectors.csv", index_col=0)
    sector_map = dict(zip(sectors_df["Código"], sectors_df["Setor"]))
    df_data_wallet = pd.read_csv("data/book_data.csv")
    df_data_wallet.drop("exchange", axis=1, inplace=True)
    df_data_wallet["date"] = df_data_wallet["date"].str.replace("T00:00:00", "")
    df_data_wallet["Setor"] = df_data_wallet["ativo"].map(sector_map)

except:
    sectors_df = pd.DataFrame(columns=["setor", "ativo", "participacao %"])


df_historico_msgs.to_csv("data/historical_msgs.csv")


def generate_card_gpt(pesquisa):
    cardNovo = dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                [
                                                                    html.H5(
                                                                        [
                                                                            html.I(
                                                                                className="fa fa-desktop",
                                                                                style={
                                                                                    "font-size": "85%"
                                                                                },
                                                                            ),
                                                                            " SmartInvestGPT: ",
                                                                        ],
                                                                        className="textoQuartenario",
                                                                    ),
                                                                    html.H5(
                                                                        str(pesquisa),
                                                                        className="textoQuartenarioBranco",
                                                                    ),
                                                                ],
                                                                md=12,
                                                                style={
                                                                    "text-align": "left"
                                                                },
                                                            ),
                                                        ]
                                                    ),
                                                ],
                                                md=11,
                                                xs=6,
                                                style={"text-align": "left"},
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        className="card_chatgpt_gpt",
                    )
                ]
            )
        ],
        className="g-2 my-auto",
    )

    return cardNovo


def generate_card_user(pesquisa):
    cardNovo = dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                [
                                                                    html.H5(
                                                                        [
                                                                            html.I(
                                                                                className="fa fa-user-circle",
                                                                                style={
                                                                                    "font-size": "85%"
                                                                                },
                                                                            ),
                                                                            " User: ",
                                                                        ],
                                                                        className="textoQuartenario",
                                                                    ),
                                                                    html.H5(
                                                                        str(pesquisa),
                                                                        className="textoQuartenarioBranco",
                                                                    ),
                                                                ],
                                                                md=12,
                                                                style={
                                                                    "text-align": "left"
                                                                },
                                                            ),
                                                        ]
                                                    ),
                                                ],
                                                md=11,
                                                xs=6,
                                                style={"text-align": "left"},
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ],
                        className="card_chatgpt_user",
                    )
                ]
            )
        ],
        className="g-2 my-auto",
    )

    return cardNovo


def gerar_resposta(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=1024, temperature=1
        )
        retorno = response.choices[0].message.content
    except:
        retorno = "Não foi possível pesquisar. ChatGPT fora do ar"
    return retorno


def clusterCards(df_msgs_store):

    df_historical_msgs = pd.DataFrame(df_msgs_store)
    cardsList = []

    for line in df_historical_msgs.iterrows():
        card_pergunta = generate_card_user(line[1]["user"])
        card_resposta = generate_card_gpt(line[1]["chatGPT"])

        cardsList.append(card_pergunta)
        cardsList.append(card_resposta)

    return cardsList


layout = (
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        "SmartInvest Chat",
                                        className="textoPrincipal",
                                        style={"margin-top": "10px"},
                                        md=12,
                                    ),
                                ],
                                className="g-2 my-auto",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dbc.Input(
                                                id="msg_user_wallet",
                                                type="text",
                                                placeholder="Insira uma mensagem",
                                            )
                                        ],
                                        md=10,
                                    ),
                                    dbc.Col(
                                        [
                                            dbc.Button(
                                                "Pesquisa", id="botao_search_wallet"
                                            )
                                        ],
                                        md=2,
                                    ),
                                ],
                                className="g-2 my-auto",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [],
                                        md=12,
                                        id="cards_respostas_wallet",
                                        style={
                                            "height": "100%",
                                            "maxHeight": "25rem",
                                            "overflow-y": "auto",
                                        },
                                    ),
                                ],
                                className="g-2 my-auto",
                            ),
                        ],
                        md=12,
                    ),
                ],
                className="g-2 my-auto",
            )
        ],
        fluid=True,
    ),
)


@app.callback(
    Output("cards_respostas_wallet", "children"),
    Input("botao_search_wallet", "n_clicks"),
    State("msg_user_wallet", "value"),
)
def add_msg(n, msg_user):

    df_historical_msgs = pd.read_csv("data/historical_msgs.csv", index_col=0)

    if msg_user == None:
        lista_cards = clusterCards(df_historical_msgs)
        return lista_cards

    if "ativo".lower() or "ativos".lower() in msg_user:
        mensagem = (
            f"{df_data_wallet}, considerando todos os dados existentes dentro do dataframe, desde a primeira linha até a última, qual é a resposta exata de um expert para a pergunta: "
            + msg_user
        )
    else:
        mensagem = f"qual é a resposta exata de um expert para a pergunta: " + msg_user

    mensagens = []
    mensagens.append({"role": "user", "content": str(mensagem)})

    pergunta_user = mensagens[0]["content"]
    resposta_chatgpt = gerar_resposta(mensagens)

    if pergunta_user == "None" or pergunta_user == "":
        lista_cards = clusterCards(df_historical_msgs)
        return lista_cards

    new_line = pd.DataFrame(
        [[pergunta_user, resposta_chatgpt]], columns=["user", "chatGPT"]
    )

    new_line["user"] = new_line["user"].str.split(":")
    new_line["user"] = new_line["user"][0][-1]
    df_historical_msgs = pd.concat([new_line, df_historical_msgs], ignore_index=True)

    df_historical_msgs.to_csv("data/historical_msgs.csv")

    lista_cards = clusterCards(df_historical_msgs)

    return lista_cards
