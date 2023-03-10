from ContractData import ContractData
from ds_config import DS_JWT
from docusign_esign import EnvelopesApi, EnvelopeDefinition, TemplateRole, Tabs, Text, Number
from jwt_config import create_api_client
from env import CONTRACT_TEMPLATE_ID

class Contract:
    
    def __init__(self, access_token, base_path, account_id): #TODO add types!
        self.access_token = access_token
        self.base_path = base_path
        self.account_id = account_id
        
        # 1. Create the envelope request object
        self.api_client = create_api_client(base_path=self.base_path, access_token=self.access_token)
        
        # 2. call Envelopes::create API method
        # Exceptions will be caught by the calling function
        self.envelopes_api = EnvelopesApi(self.api_client)
        
    def make_contract(self, contract_data: ContractData):
        results = self.envelopes_api.create_envelope(
            account_id=self.account_id, envelope_definition=contract_data.generate_envelope()
        )
        envelope_id = results.envelope_id
        return {"envelope_id": envelope_id}