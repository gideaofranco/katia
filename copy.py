import csv

#ARQUIVO_ENTRADA = 'twitter-100-linhas.csv'
ARQUIVO_ENTRADA = 'twitter.csv'
ARQUIVO_SAIDA = 'twitter-new.csv'

MINIMO_DE_PALAVRAS = 60
CAMMPOS = ['tweet_id', 'theme_list', 'account_id', 'account_name', 'scraped_at', 'posted_at ', 'message', 'url_tweet', 
    'relative_score', 'like_count', 'share_count', 'network', 'relative_url']

total_linhas = 0
linhas_coletadas = 0
with open(ARQUIVO_ENTRADA, mode='r', encoding="utf8") as leitorArquivo:

    with open(ARQUIVO_SAIDA, mode='w', newline='', encoding='utf-8') as escritorArquivo:
        leitor = csv.reader(leitorArquivo)
        escritor = csv.writer(escritorArquivo)
        escritor.writerow(CAMMPOS)
        for linhaLida in leitor:
            text_cel = linhaLida[7]                #  7 - Texto
            quantidade_de_palavras = text_cel.count(" ") + 1

            if (quantidade_de_palavras >=  MINIMO_DE_PALAVRAS):
                linhas_coletadas = linhas_coletadas + 1

                tema_cel           = linhaLida[0]  #  0 - Temas
                hashtags_cel       = linhaLida[1]  #  1 - Hashtags
                xid_cel            = linhaLida[2]  #  2 - ID do Tweet
                links_json_cel     = linhaLida[4]  #  4 - Imagens Postadas ou Link de relação (Intertexo)
                # score_json_cel     = linhaLida[5]  #  5 - Scores
                data_public_cel    = linhaLida[6]  #  6 - Data da Postagem/Publicação
                qtd_curtidas_cel   = linhaLida[9]  #  9 - Curtidas
                qtd_reposts_cel    = linhaLida[10] # 10 - Reposts
                nome_no_perfil_cel = linhaLida[11] # 11 - Nome no Perfil
                id_perfil_cel      = linhaLida[12] # 12 - Perfil
                data_ingresso_cel  = linhaLida[13] # 13 - Data de Ingresso Twiter (X)
                qtd_seguidores_cel = linhaLida[15] # 15 - Quantidade de Seguidores
                qtd_seguindo_cel   = linhaLida[16] # 16 - Seguindo quantos
                qtd_postagens_cel  = linhaLida[17] # 17 - Postagens
                link_do_post_cel   = linhaLida[21] # 21 - Link da Publicação
                data_da_coleta_cel = linhaLida[22] # 22 - Data de Coleta
                modo_extracao_cel  = linhaLida[23] # 23 - Modo de Extração
                pontuacao_fake_cel = linhaLida[24] # 24 - Portuação de Fake News (0=Fake, 10=Não Fake)

                linhaParaEscrever =[]
                linhaParaEscrever.append(xid_cel)
                linhaParaEscrever.append(tema_cel)
                linhaParaEscrever.append(id_perfil_cel)
                linhaParaEscrever.append(nome_no_perfil_cel)
                linhaParaEscrever.append(data_da_coleta_cel)
                linhaParaEscrever.append(data_public_cel)
                linhaParaEscrever.append(text_cel)
                linhaParaEscrever.append(link_do_post_cel)
                linhaParaEscrever.append(pontuacao_fake_cel)
                linhaParaEscrever.append(qtd_curtidas_cel)
                linhaParaEscrever.append(qtd_reposts_cel)
                linhaParaEscrever.append(qtd_seguidores_cel)
                linhaParaEscrever.append(links_json_cel)

                escritor.writerow(linhaParaEscrever)
            # else:
            #     print(f"{quantidade_de_palavras} palavras é menos de {MINIMO_DE_PALAVRAS} palavras.")

            total_linhas = total_linhas + 1

            if (total_linhas % 100000 == 0):
                print(f"{total_linhas} linhas processadas/{linhas_coletadas} linhas coletadas")
