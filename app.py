from flask import Flask, render_template, jsonify
import yfinance as yf
import threading
import webbrowser
import time
from datetime import datetime


# ============================================================
# CONFIGURAÇÕES
# ============================================================

tickerPrefix = {
    "AXIA": [30, 40.6, 133.2],
    "BBAS": [30],
    "BBSE": [86, 58.1, 64.8, 97.4, 86.1, 106.7],
    "BRSR": [40],
    "CMIG": [54.2, 52.5, 71.6],
    "CXSE": [90, 91.7, 91.1],
    "EGIE": [55],
    "ISAE": [75],
    "ITSA": [62, 68, 76],
    "ITUB": [60.3, 62.1, 67.6],
    "KLBN": [15],
    "PSSA": [43, 50, 55],
    "TAEE": [100]
}


priceSuffix = {
    "AXIA": ["3"],
    "BBAS": ["3"],
    "BBSE": ["3"],
    "BRSR": ["6"],
    "CMIG": ["4"],
    "CXSE": ["3"],
    "EGIE": ["3"],
    "ISAE": ["4"],
    "ITSA": ["3", "4"],
    "ITUB": ["3", "4"],
    "KLBN": ["3", "4"],
    "PSSA": ["3"],
    "TAEE": ["3", "4"]
}


epsTicker = {
    "AXIA3": ("AXIA3", 1),
    "BBAS3": ("BBAS3", 1),
    "BBSE3": ("BBSE3", 1),
    "BRSR6": ("BRSR6", 1),
    "CMIG4": ("CMIG4", 1),
    "CXSE3": ("CXSE3", 1),
    "EGIE3": ("EGIE3", 1),
    "ISAE4": ("ISAE4", 1),
    "ITSA3": ("ITSA4", 1),
    "ITSA4": ("ITSA4", 1),
    "ITUB3": ("ITUB4", 1),
    "ITUB4": ("ITUB4", 1),
    "KLBN3": ("KLBN11", 1),
    "KLBN4": ("KLBN11", 1),
    "PSSA3": ("PSSA3", 1),
    "TAEE3": ("TAEE11", 3),
    "TAEE4": ("TAEE11", 3)
}


# ============================================================
# FLASK
# ============================================================

app = Flask(__name__)


# ============================================================
# VARIÁVEIS
# ============================================================

resultados = []

atualizando = False

ultima_atualizacao = None


# ============================================================
# CONSULTA DOS DADOS
# ============================================================

def consultar_dados():

    novosResultados = []


    for prefix, payouts in tickerPrefix.items():

        for suffix in priceSuffix[prefix]:

            ticker = prefix + suffix


            print(
                f"Consultando {ticker}..."
            )


            # ------------------------------------------------
            # COTAÇÃO
            # ------------------------------------------------

            try:

                acao = yf.Ticker(
                    ticker + ".SA"
                )

                cotacao = (
                    acao.fast_info["last_price"]
                )

            except Exception as erro:

                print(
                    f"Erro na cotação de "
                    f"{ticker}: {erro}"
                )

                cotacao = None


            # ------------------------------------------------
            # EPS
            # ------------------------------------------------

            try:

                tickerEps, divisorEps = (
                    epsTicker[ticker]
                )


                acaoEps = yf.Ticker(
                    tickerEps + ".SA"
                )


                eps = (
                    acaoEps
                    .get_earnings_estimate()
                    .loc["0y", "avg"]
                )


                eps = eps / divisorEps


            except (
                KeyError,
                TypeError,
                AttributeError,
                IndexError,
                ZeroDivisionError
            ):

                eps = None


            # ------------------------------------------------
            # PAYOUT MÉDIO
            # ------------------------------------------------

            payout = (
                sum(payouts)
                / len(payouts)
            )


            # ------------------------------------------------
            # CÁLCULOS
            # ------------------------------------------------

            if eps is not None:

                ppa = (
                    eps
                    * (payout / 100)
                )


                precoTeto = (
                    ppa / 0.06
                )


                if (
                    cotacao is not None
                    and cotacao != 0
                ):

                    dy = (
                        ppa
                        / cotacao
                        * 100
                    )

                else:

                    dy = None

            else:

                ppa = None

                precoTeto = None

                dy = None


            # ------------------------------------------------
            # RESULTADO
            # ------------------------------------------------

            novosResultados.append({

                "ticker": ticker,

                "cotacao": cotacao,

                "precoTeto": precoTeto,

                "dy": dy,

                "ppa": ppa,

                "eps": eps,

                "payout": payout

            })


    return novosResultados


# ============================================================
# ATUALIZAÇÃO DOS DADOS
# ============================================================

def atualizar_dados():

    global resultados
    global atualizando
    global ultima_atualizacao


    if atualizando:

        return


    atualizando = True


    try:

        print()

        print(
            "Iniciando atualização..."
        )

        print()


        resultados = (
            consultar_dados()
        )


        # ----------------------------------------------------
        # DATA E HORA DA ATUALIZAÇÃO
        # ----------------------------------------------------

        ultima_atualizacao = (
            datetime.now().strftime(
                "%d/%m/%Y às %H:%M:%S"
            )
        )


        print()

        print(
            f"Dados atualizados em "
            f"{ultima_atualizacao}"
        )

        print()


    finally:

        atualizando = False


# ============================================================
# ROTA PRINCIPAL
# ============================================================

@app.route("/")
def index():

    return render_template(
        "index.html",
        resultados=resultados
    )


# ============================================================
# API — DADOS
# ============================================================

@app.route("/api/dados")
def api_dados():

    return jsonify({

        "resultados":
            resultados,

        "atualizando":
            atualizando,

        "ultima_atualizacao":
            ultima_atualizacao

    })


# ============================================================
# API — ATUALIZAR
# ============================================================

@app.route(
    "/api/atualizar",
    methods=["POST"]
)
def api_atualizar():

    global atualizando


    if atualizando:

        return jsonify({

            "status":
                "atualizando"

        })


    thread = threading.Thread(
        target=atualizar_dados
    )


    thread.daemon = True


    thread.start()


    return jsonify({

        "status":
            "iniciado"

    })


# ============================================================
# ABRIR NAVEGADOR
# ============================================================

def abrir_navegador():

    time.sleep(1)


    webbrowser.open(
        "http://127.0.0.1:5000"
    )


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    print()

    print(
        "=========================================="
    )

    print(
        "              PREÇO TETO"
    )

    print(
        "=========================================="
    )

    print()


    # --------------------------------------------------------
    # PRIMEIRA CONSULTA
    # --------------------------------------------------------

    print(
        "Consultando dados iniciais..."
    )


    atualizar_dados()


    # --------------------------------------------------------
    # ABRIR NAVEGADOR
    # --------------------------------------------------------

    threading.Thread(
        target=abrir_navegador,
        daemon=True
    ).start()


    # --------------------------------------------------------
    # INICIAR FLASK
    # --------------------------------------------------------

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=False,

        use_reloader=False

    )
