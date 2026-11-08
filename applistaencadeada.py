import streamlit as st

# ==========================================
# SIMULADOR DE LISTA ENCADEADA
# Estrutura de Dados - Python + Streamlit
# ==========================================

st.set_page_config(
    page_title="Simulador de Lista Encadeada",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ==========================================
# ESTRUTURA DE DADOS: NO E LISTA ENCADEADA
# ==========================================

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
        return f"'{valor}' inserido no início!"

    def inserir_final(self, valor):
        novo_no = No(valor)

        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

        return f"'{valor}' inserido no final!"

    def inserir_posicao(self, valor, posicao):
        if posicao < 1:
            return "Posição inválida! Use uma posição a partir de 1."

        novo_no = No(valor)

        if posicao == 1:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
            return f"'{valor}' inserido na posição {posicao}!"

        atual = self.inicio
        contador = 1

        while atual is not None and contador < posicao - 1:
            atual = atual.proximo
            contador += 1

        if atual is None:
            return "Posição inválida! Não existe nó anterior nessa posição."

        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        return f"'{valor}' inserido na posição {posicao}!"

    def valores(self):
        resultado = []
        atual = self.inicio

        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo

        return resultado

    def buscar(self, valor):
        atual = self.inicio
        posicao = 1

        while atual is not None:
            if atual.valor.casefold() == valor.casefold():
                return posicao, atual.valor
            atual = atual.proximo
            posicao += 1

        return None

    def remover(self, valor):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.valor.casefold() == valor.casefold():
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                return f"'{atual.valor}' removido da lista!"

            anterior = atual
            atual = atual.proximo

        return f"'{valor}' não encontrado!"

    def limpar(self):
        self.inicio = None


# ==========================================
# ESTADO DA SESSAO
# ==========================================

if "lista_encadeada" not in st.session_state:
    lista_inicial = ListaEncadeada()
    for nome in ["Ana", "Bia", "Caio", "Duda"]:
        lista_inicial.inserir_final(nome)
    st.session_state.lista_encadeada = lista_inicial

if "historico_encadeada" not in st.session_state:
    st.session_state.historico_encadeada = []

if "mensagem_encadeada" not in st.session_state:
    st.session_state.mensagem_encadeada = "Lista inicial carregada com quatro nomes."

if "tipo_mensagem_encadeada" not in st.session_state:
    st.session_state.tipo_mensagem_encadeada = "info"


# ==========================================
# ESTILO VISUAL
# ==========================================

st.markdown(
    """
    <style>
    .stApp {
        background: #0b1220;
        color: #edf4ff;
    }
    [data-testid="stHeader"] {
        background: rgba(11, 18, 32, .95);
    }
    .main .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .hero {
        background: linear-gradient(120deg, #10243b, #123c42);
        border: 1px solid #245c61;
        border-radius: 18px;
        padding: 24px 28px;
        margin-bottom: 20px;
    }
    .hero h1 {
        color: #55e6b2;
        margin: 0;
        font-size: 2rem;
    }
    .hero p {
        color: #c3d4e8;
        margin: 6px 0 0 0;
    }
    .metric-card {
        background: #142238;
        border: 1px solid #263d59;
        border-radius: 14px;
        padding: 15px 18px;
        min-height: 88px;
    }
    .metric-label {
        color: #9fb2c9;
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .08em;
    }
    .metric-value {
        color: #55e6b2;
        font-size: 1.45rem;
        font-weight: 800;
        margin-top: 5px;
        overflow-wrap: anywhere;
    }
    .linked-area {
        background: #101c2e;
        border: 1px solid #263d59;
        border-radius: 18px;
        padding: 20px;
        min-height: 270px;
    }
    .linked-title {
        color: #55e6b2;
        text-align: center;
        font-weight: 800;
        letter-spacing: .08em;
        margin-bottom: 18px;
    }
    .node {
        display: inline-block;
        vertical-align: middle;
        background: linear-gradient(135deg, #1d4960, #245b70);
        border: 1px solid #4a8797;
        color: #f4f8ff;
        border-radius: 12px;
        padding: 15px 18px;
        margin: 7px 3px;
        min-width: 90px;
        text-align: center;
        font-size: 1rem;
        font-weight: 800;
        box-shadow: 0 5px 12px rgba(0,0,0,.18);
    }
    .pointer {
        display: inline-block;
        color: #55e6b2;
        font-size: 1.4rem;
        font-weight: 900;
        vertical-align: middle;
        margin: 0 2px;
    }
    .null-node {
        display: inline-block;
        background: #392c42;
        border: 1px solid #94618f;
        color: #ffd7f4;
        border-radius: 10px;
        padding: 13px 15px;
        margin: 7px 3px;
        font-weight: 800;
    }
    .empty-list {
        color: #9fb2c9;
        text-align: center;
        padding: 65px 10px;
        border: 1px dashed #49617d;
        border-radius: 12px;
    }
    .history-item {
        color: #c8d8e9;
        background: #142238;
        border: 1px solid #263d59;
        border-radius: 8px;
        padding: 8px 12px;
        margin: 5px 0;
        font-size: .9rem;
    }
    div.stButton > button {
        width: 100%;
        min-height: 43px;
        border-radius: 10px;
        font-weight: 800;
        border: 1px solid #42617e;
    }
    div.stButton > button[kind="primary"] {
        background: #087e5b;
        color: white;
        border: 1px solid #22bd8a;
    }
    div.stButton > button:hover {
        border-color: #55e6b2;
        color: white;
    }
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input {
        background: #142238;
        color: white;
    }
    .footer {
        color: #8195ad;
        text-align: center;
        font-size: .8rem;
        padding-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==========================================
# FUNCOES AUXILIARES
# ==========================================

def registrar(resultado, tipo="success"):
    st.session_state.mensagem_encadeada = resultado
    st.session_state.tipo_mensagem_encadeada = tipo
    st.session_state.historico_encadeada.insert(0, resultado)


def obter_lista():
    return st.session_state.lista_encadeada


# ==========================================
# CABECALHO
# ==========================================

st.markdown(
    """
    <div class="hero">
        <h1>🔗 SIMULADOR DE LISTA ENCADEADA</h1>
        <p>ESTRUTURA DE DADOS &nbsp; | &nbsp; NÓS • PONTEIROS • INSERÇÃO • BUSCA • REMOÇÃO</p>
    </div>
    """,
    unsafe_allow_html=True,
)

lista = obter_lista()
valores = lista.valores()

# ==========================================
# INDICADORES
# ==========================================

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">QUANTIDADE DE NÓS</div>'
        f'<div class="metric-value">{len(valores)}</div></div>',
        unsafe_allow_html=True,
    )

with c2:
    inicio = valores[0] if valores else "---"
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">PRIMEIRO NÓ (INÍCIO)</div>'
        f'<div class="metric-value">{inicio}</div></div>',
        unsafe_allow_html=True,
    )

with c3:
    fim = valores[-1] if valores else "---"
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">ÚLTIMO NÓ</div>'
        f'<div class="metric-value">{fim}</div></div>',
        unsafe_allow_html=True,
    )

st.write("")

# ==========================================
# VISUALIZACAO E OPERACOES
# ==========================================

col_visual, col_operacoes = st.columns([1.45, 1], gap="large")

with col_visual:
    st.subheader("🧩 Visualização dos nós")
    st.markdown('<div class="linked-area">', unsafe_allow_html=True)
    st.markdown('<div class="linked-title">INÍCIO → LISTA ENCADEADA</div>',
                unsafe_allow_html=True)

    if valores:
        partes = ['<span class="pointer">INÍCIO →</span>']
        for valor in valores:
            partes.append(f'<span class="node">{valor}</span>')
            partes.append('<span class="pointer">→</span>')
        partes.append('<span class="null-node">NULL</span>')

        st.markdown(
            '<div style="text-align:center;line-height:3.8;overflow-wrap:anywhere">'
            + "".join(partes) + "</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="empty-list">LISTA VAZIA<br><br>Insira um novo nó para começar.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
    st.caption("Cada nó armazena um valor e uma referência para o próximo nó.")

    with st.expander("🔍 Ver estrutura nó por nó"):
        if valores:
            for i, valor in enumerate(valores):
                proximo = valores[i + 1] if i + 1 < len(valores) else "NULL"
                st.write(f"**Nó {i + 1}:** valor = `{valor}`  |  próximo = `{proximo}`")
        else:
            st.write("Não há nós na lista.")


with col_operacoes:
    st.subheader("⚙️ Operações")

    st.markdown("**Inserir no início**")
    with st.form("form_inicio", clear_on_submit=True):
        nome_inicio = st.text_input("Nome para inserir no início", placeholder="Ex.: Eva", key="nome_inicio")
        enviar_inicio = st.form_submit_button("＋ INSERIR NO INÍCIO", type="primary")
        if enviar_inicio:
            nome = nome_inicio.strip()
            if nome:
                registrar(obter_lista().inserir_inicio(nome))
            else:
                registrar("Digite um nome válido.", "warning")
            st.rerun()

    st.divider()

    st.markdown("**Inserir no final**")
    with st.form("form_final", clear_on_submit=True):
        nome_final = st.text_input("Nome para inserir no final", placeholder="Ex.: Enzo", key="nome_final")
        enviar_final = st.form_submit_button("＋ INSERIR NO FINAL")
        if enviar_final:
            nome = nome_final.strip()
            if nome:
                registrar(obter_lista().inserir_final(nome))
            else:
                registrar("Digite um nome válido.", "warning")
            st.rerun()

    st.divider()

    st.markdown("**Inserir em uma posição**")
    with st.form("form_posicao", clear_on_submit=True):
        nome_posicao = st.text_input("Nome", placeholder="Ex.: Fábio", key="nome_posicao")
        posicao = st.number_input("Posição (começa em 1)", min_value=1, step=1, value=2, key="posicao")
        enviar_posicao = st.form_submit_button("＋ INSERIR NA POSIÇÃO")
        if enviar_posicao:
            nome = nome_posicao.strip()
            if nome:
                resultado = obter_lista().inserir_posicao(nome, int(posicao))
                tipo = "success" if "inserido" in resultado else "warning"
                registrar(resultado, tipo)
            else:
                registrar("Digite um nome válido.", "warning")
            st.rerun()

    st.divider()

    st.markdown("**Remover um nome**")
    with st.form("form_remover", clear_on_submit=True):
        nome_remover = st.text_input("Nome para remover", placeholder="Ex.: Bia", key="nome_remover")
        enviar_remover = st.form_submit_button("－ REMOVER NOME")
        if enviar_remover:
            nome = nome_remover.strip()
            if nome:
                resultado = obter_lista().remover(nome)
                tipo = "success" if "removido" in resultado else "warning"
                registrar(resultado, tipo)
            else:
                registrar("Digite um nome válido.", "warning")
            st.rerun()

    st.divider()

    st.markdown("**Buscar um nome**")
    with st.form("form_buscar", clear_on_submit=True):
        nome_buscar = st.text_input("Nome para buscar", placeholder="Ex.: Caio", key="nome_buscar")
        enviar_buscar = st.form_submit_button("🔍 BUSCAR NOME")
        if enviar_buscar:
            nome = nome_buscar.strip()
            if nome:
                resultado = obter_lista().buscar(nome)
                if resultado:
                    pos, nome_encontrado = resultado
                    registrar(f"'{nome_encontrado}' encontrado na posição {pos}!")
                else:
                    registrar(f"'{nome}' não encontrado na lista.", "warning")
            else:
                registrar("Digite um nome válido.", "warning")
            st.rerun()


# ==========================================
# STATUS
# ==========================================

st.write("")
tipo = st.session_state.tipo_mensagem_encadeada
mensagem = st.session_state.mensagem_encadeada

if tipo == "success":
    st.success(mensagem)
elif tipo == "warning":
    st.warning(mensagem)
else:
    st.info(mensagem)


# ==========================================
# ACOES ADICIONAIS
# ==========================================

a1, a2 = st.columns(2)

with a1:
    if st.button("↩️ RESTAURAR LISTA INICIAL", use_container_width=True):
        nova_lista = ListaEncadeada()
        for nome in ["Ana", "Bia", "Caio", "Duda"]:
            nova_lista.inserir_final(nome)
        st.session_state.lista_encadeada = nova_lista
        registrar("Lista inicial restaurada: Ana → Bia → Caio → Duda.")
        st.rerun()

with a2:
    if st.button("🧹 LIMPAR TODA A LISTA", use_container_width=True):
        obter_lista().limpar()
        registrar("Todos os nós foram removidos da lista.")
        st.rerun()


# ==========================================
# HISTORICO
# ==========================================

st.write("")
st.subheader("📋 Histórico de operações")

if st.session_state.historico_encadeada:
    for item in st.session_state.historico_encadeada[:10]:
        st.markdown(
            f'<div class="history-item">{item}</div>',
            unsafe_allow_html=True,
        )
    if st.button("Limpar histórico"):
        st.session_state.historico_encadeada.clear()
        st.rerun()
else:
    st.caption("Nenhuma operação realizada até o momento.")


# ==========================================
# EXPLICACAO DIDATICA
# ==========================================

with st.expander("📘 Como funciona uma lista encadeada?"):
    st.markdown(
        """
        - **Nó:** contém um valor e uma referência chamada `proximo`.
        - **Início:** aponta para o primeiro nó da lista.
        - **Inserir no início:** o novo nó passa a apontar para o antigo primeiro nó.
        - **Inserir no final:** percorre os nós até encontrar aquele cujo `proximo` é `None`.
        - **Inserir em uma posição:** ajusta as referências do nó anterior e do novo nó.
        - **Remover:** altera a referência do nó anterior para pular o nó removido.
        - **NULL:** indica que não existe um próximo nó.
        """
    )

st.markdown(
    '<div class="footer">SIMULADOR DIDÁTICO DE ESTRUTURA DE DADOS • LISTA ENCADEADA</div>',
    unsafe_allow_html=True,
)
