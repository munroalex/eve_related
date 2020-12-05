import pandas as pd
from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity

app = EsiApp().get_latest_swagger
# replace the redirect_uri, client_id and secret_key values
# with the values you get from the STEP 1 !
security = EsiSecurity(
    redirect_uri="http://localhost:5000/eve_callback",
    client_id="0eeaaa5cec934a60a99f412d43cf387b",
    secret_key="3b5NR5uXW6hcGwT9H2gVMvKlp3NtCDk7zTBBt4cn",
    headers={"User-Agent": "munroa.alex@gmail.com"},
)
# and the client object, replace the header user agent value with something reliable !
client = EsiClient(
    retry_requests=True, headers={"User-Agent": "Corel Dahken"}, security=security,
)

scopes = ['publicData',
          'esi-calendar.respond_calendar_events.v1',
          'esi-calendar.read_calendar_events.v1',
          'esi-location.read_location.v1',
          'esi-location.read_ship_type.v1',
          'esi-mail.organize_mail.v1',
          'esi-mail.read_mail.v1',
          'esi-mail.send_mail.v1',
          'esi-skills.read_skills.v1',
          'esi-skills.read_skillqueue.v1',
          'esi-wallet.read_character_wallet.v1',
          'esi-wallet.read_corporation_wallet.v1',
          'esi-search.search_structures.v1',
          'esi-clones.read_clones.v1',
          'esi-characters.read_contacts.v1',
          'esi-universe.read_structures.v1',
          'esi-bookmarks.read_character_bookmarks.v1',
          'esi-killmails.read_killmails.v1',
          'esi-corporations.read_corporation_membership.v1',
          'esi-assets.read_assets.v1',
          'esi-planets.manage_planets.v1',
          'esi-fleets.read_fleet.v1',
          'esi-fleets.write_fleet.v1',
          'esi-ui.open_window.v1',
          'esi-ui.write_waypoint.v1',
          'esi-characters.write_contacts.v1',
          'esi-fittings.read_fittings.v1',
          'esi-fittings.write_fittings.v1',
          'esi-markets.structure_markets.v1',
          'esi-corporations.read_structures.v1',
          'esi-characters.read_loyalty.v1',
          'esi-characters.read_opportunities.v1',
          'esi-characters.read_chat_channels.v1',
          'esi-characters.read_medals.v1',
          'esi-characters.read_standings.v1',
          'esi-characters.read_agents_research.v1',
          'esi-industry.read_character_jobs.v1',
          'esi-markets.read_character_orders.v1',
          'esi-characters.read_blueprints.v1',
          'esi-characters.read_corporation_roles.v1',
          'esi-location.read_online.v1',
          'esi-contracts.read_character_contracts.v1',
          'esi-clones.read_implants.v1',
          'esi-characters.read_fatigue.v1',
          'esi-killmails.read_corporation_killmails.v1',
          'esi-corporations.track_members.v1',
          'esi-wallet.read_corporation_wallets.v1',
          'esi-characters.read_notifications.v1',
          'esi-corporations.read_divisions.v1',
          'esi-corporations.read_contacts.v1',
          'esi-assets.read_corporation_assets.v1',
          'esi-corporations.read_titles.v1',
          'esi-corporations.read_blueprints.v1',
          'esi-bookmarks.read_corporation_bookmarks.v1',
          'esi-contracts.read_corporation_contracts.v1',
          'esi-corporations.read_standings.v1',
          'esi-corporations.read_starbases.v1',
          'esi-industry.read_corporation_jobs.v1',
          'esi-markets.read_corporation_orders.v1',
          'esi-corporations.read_container_logs.v1',
          'esi-industry.read_character_mining.v1',
          'esi-industry.read_corporation_mining.v1',
          'esi-planets.read_customs_offices.v1',
          'esi-corporations.read_facilities.v1',
          'esi-corporations.read_medals.v1',
          'esi-characters.read_titles.v1',
          'esi-alliances.read_contacts.v1',
          'esi-characters.read_fw_stats.v1',
          'esi-corporations.read_fw_stats.v1',
          'esi-characterstats.read.v1']
          
print(security.get_auth_uri(state='SomeRandomGeneratedState', scopes=scopes))
tokens = security.auth('H2RDKWS8IEuQjnHUGj_zJw')
api_info = security.verify()
token_list = [api_info['name'],tokens['access_token'],tokens['expires_in'],tokens['refresh_token'],api_info['sub'].split(':')[-1]]
token_list
df = df.append(pd.Series(token_list, index=['Name','access_toke','expires_in','refresh_token','character_id']), ignore_index=True)
df
          
          
