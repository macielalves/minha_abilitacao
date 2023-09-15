"""_summary_
"""
# charset_
# inserir campo nome
# inserir campo RG - orgão emissor - UF
# inserir campo cpf - data/nascimento
# inserir campo filiação -> campo para inserir o nome do pai e da mãe
# inserir campo permissão - ACC - CAT.HAB -> (AD) -> [A, B, C, D ou E]
# inserir campo Nº de Registro - Validade - 1ª Habilitação
# inserir campo de Observações
# inserir Campo destinado para <assinatura do portador> externa
# inserir campo Local - data de emissão
# inserir Campo destinado a <assinatura do emissor>
# inserir em um lugar da folha a imagem de perfil


class CNH:
    nome = None
    rg = None
    cpf = None
    filiacao = None  # (nome_mae, nome_pai)
    permissao = None
    acc = None
    cats_hab = ('A', 'B', 'C', 'D', 'E')
    cat_hab = None
    n_reg = None
    val = None
    primery_hab = None
    obs = None
    data_emissao = None
    img_profile = None

    def __init__(self,
                 nome, rg, cpf, filiacao, cat_hab, img_profile=None) -> None:
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.filiacao = filiacao
        self.cat_hab = cat_hab
        self.img_profile = img_profile
        pass
