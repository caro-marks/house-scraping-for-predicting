import bs4
import requests
import pandas as pd


class Dry_Imobs:
    def __init__(slf):
        slf.paths = {
            'casaraoimoveis':
            'https://casaraoimoveis.com.br/imoveis/vendas/pelotas/Apartamento&Cobertura/2-3-4-5-quartos/1-2-3-vagas/nao-mobiliado/?bairro=Centro&zona=Centro',
            'oliveiraimoveis':
            'https://www.oliveiraimoveis.net.br/imoveis/a-venda/rs/pelotas/centro/apartamento?valor_min=&valor_max=&dormitorios%5B%5D=2&banheiros%5B%5D=1&vagas%5B%5D=1&ordem=recentes',
            'eduardolangimoveis':
            'https://eduardolangimoveis.com.br/busca?estado%5B%5D=2&cidade%5B%5D=364&bairro%5B%5D=1869&valor-min=&valor-max=&operacao=venda&tipo-imovel%5B%5D=6&dormitorios%5B%5D=&dormitorios%5B%5D=2&area-min=&area-max=&page=2',
            'marquesimoveis':
            'http://marquesimoveis.imb.br/imoveis-venda.php?codigo_imovel=&negociacao=Venda&situacao=&tipo[]=3943&cidade=50758&bairro[]=117596&area_minima=70&area_maxima=110&valor_minimo=&valor_maximo=&qtd_quartos=2&qtd_suites=&qtd_vagas=1',
            'fuhrosouto':
            'https://www.fuhrosouto.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade[]=2&id_tipo_imovel[]=8&id_bairro[]=2&finalidade=residencial&dormitorio=2&garagem=1&vmi=&vma=&ordem=3',
            'requinte':
            'https://www.requinte.net/imoveis/a-venda/rs/pelotas/apartamento?valor_min=&valor_max=&dormitorios%5B%5D=2&banheiros%5B%5D=1&vagas%5B%5D=1&comodidades%5B%5D=38&ordem=valor_min',
            'krolowimobiliaria':
            'https://krolowimobiliaria.com.br/busca/?finalidade=Venda&tipo%5B%5D=Apartamento&cidade=Pelotas&bairro%5B%5D=Centro&valor%5B0%5D=&valor%5B1%5D=&area%5B0%5D=&area%5B1%5D=&dormitorios%5B%5D=2&banheiros%5B%5D=1&vagas%5B%5D=1&codigo=',
        }
        slf.bodies = []

    def dry_casarao(slf, object):
        estates = object.select('div#imoveis div.card-imovel')
        response = []
        for estate in estates:
            try:
                price = estate.select('p.title')[0].get_text().split()[1]
                details = estate.select('div.card-imovel-icones')[0]
                rooms = details.select('div.col')[0].get_text().split()[0]
                garages = details.select('div.col')[1].get_text().split()[0]
                bathrooms = details.select('div.col')[2].get_text().split()[0]
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])

        return response

    def dry_oliveira(slf, object):
        estates = object.select('ul#imoveis-list div.list-group')
        response = []
        for estate in estates:
            try:
                price = estate.select('div.definition')[
                    0].get_text().split()[1]
                details = estate.select('span.top-info')
                rooms = details[0].get_text().split()[0]
                bathrooms = details[1].get_text().split()[0]
                garages = details[2].get_text().split()[0]
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])
        return response

    def dry_eduardo(slf, object):
        estates = object.select('a.imovel div.detalhes')
        response = []
        for estate in estates:
            try:
                price = estate.select(
                    'div.objeto-valor strong')[0].get_text().split()[1]
                details = estate.select('span.numero')
                rooms = details[0].get_text()
                bathrooms = details[1].get_text()
                garages = details[2].get_text()
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])
        return response

    def dry_marques(slf, object):
        estates = object.select('div.item-body')
        response = []
        for estate in estates:
            try:
                price = estate.select('h3.h4')[0].get_text().split(' ')[-1]
                details = estate.select('span')[:-1]
                rooms = details[0].get_text().split()[0]
                garages = details[1].get_text().split()[0]
                bathrooms = details[2].get_text().split()[0]
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])
        return response

    def dry_fuhro(slf, object):
        estates = object.select('div.row div.item.col-sm-6')
        response = []
        for estate in estates:
            try:
                price = estate.select('div.price span')[0].get_text()
                details = estate.select('div.info ul li')[0:3]
                rooms = details[0].get_text().split()[0]
                bathrooms = details[1].get_text().split()[0]
                garages = details[2].get_text().split()[0]
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])
        return response

    def dry_requinte(slf, object):
        estates = object.select('ul#imoveis-list div.list-group')
        response = []
        for estate in estates:
            try:
                price = estate.select('div.definition')[
                    0].get_text().split()[1]
                details = estate.select('span.top-info')
                rooms = details[0].get_text().split()[0]
                bathrooms = details[1].get_text().split()[0]
                garages = details[2].get_text().split()[0]
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])
        return response

    def dry_krolow(slf, object):
        estates = object.select('div.properties-full div.property-thumb-info')
        response = []
        for estate in estates:
            try:
                price = estate.select('span.price')[0].get_text().split()[1]
                details = estate.select('ul.pull-right li')
                rooms = details[0].get_text().split()[0]
                bathrooms = details[1].get_text().split()[0]
                garages = details[2].get_text().split()[0]
            except Exception:
                pass
            else:
                response.append([price, rooms, garages, bathrooms])
        return response

    def counter(slf, fallen):
        for each in fallen:
            slf.bodies.append(each)

    def dryer(slf, imob, meal):
        if imob == 'casaraoimoveis':
            slf.counter(slf.dry_casarao(meal))
        elif imob == 'oliveiraimoveis':
            slf.counter(slf.dry_oliveira(meal))
        elif imob == 'eduardolangimoveis':
            slf.counter(slf.dry_eduardo(meal))
        elif imob == 'marquesimoveis':
            slf.counter(slf.dry_marques(meal))
        elif imob == 'fuhrosouto':
            slf.counter(slf.dry_fuhro(meal))
        elif imob == 'requinte':
            slf.counter(slf.dry_requinte(meal))
        else:
            slf.counter(slf.dry_krolow(meal))

    def chase(slf, path):
        request = requests.get(f'{slf.paths[path]}')
        request.raise_for_status()
        try:
            soup = bs4.BeautifulSoup(request.text, 'html.parser')
        except UnicodeDecodeError:
            soup = bs4.BeautifulSoup(
                request.text, from_encoding='latin-1')
        slf.dryer(path, soup)

    def feed(slf):
        df = pd.DataFrame(slf.bodies,
                          columns=['price', 'rooms', 'garages', 'bathrooms'])
        df.to_csv('data.csv')

    def hunt(slf):
        for path in slf.paths:
            slf.chase(path)
        slf.feed()


vamp = Dry_Imobs()
vamp.hunt()
