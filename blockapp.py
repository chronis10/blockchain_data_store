#Based on https://towardsdatascience.com/building-a-minimal-blockchain-in-python-4f2e9934101d

from chain import *
import json
import pickle

def data_import():
    name = input('Insert name: ')
    lastname  = input('Insert lastname: ')
    ticket_number = input('Insert Ticket numer: ')
    event = input('Insert Event: ')
    data = {'name' : name, 'lastname' : lastname, 'ticket_number':ticket_number,'event':event }
    return json.dumps(data)

def load_chain():
    try:
        return pickle.load( open( "chain.p", "rb" ) )
    except:
        return MinimalChain()

def save_chain(chain):
    pickle.dump( chain, open( "chain.p", "wb" ) )

if __name__ == '__main__':
    mainchain = load_chain()
    while True:
        usr_inp = input('Insert Command: ')
        if usr_inp == 'add':
            print('Add block')
            mainchain.add_block(data_import())
            save_chain(mainchain)
        elif usr_inp == 'size':
            print(mainchain.get_chain_size())
        elif usr_inp == 'verify all':
            if mainchain.verify_all():
                print('Chain Verified')
            else:
                print('Chain Corrupted')
        elif usr_inp == 'print all':
            mainchain.print_all_chains()
        elif usr_inp == 'corrupt':
            mainchain.blocks[1].data = 'Corrupted data insertion'
        elif usr_inp == 'exit':
            break
