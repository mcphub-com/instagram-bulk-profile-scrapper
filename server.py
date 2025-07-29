import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/thekirtan/api/instagram-bulk-profile-scrapper'

mcp = FastMCP('instagram-bulk-profile-scrapper')

@mcp.tool()
def bulk_profile_fast_response(ig: Annotated[str, Field(description='')],
                               response_type: Annotated[str, Field(description='')],
                               corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''**Contact me for Custom package or requirements** Fetch Instagram Short Profile without recent feeds, Useful for Profile verification, This endpoint use smart caching algorithm, Contact me to reduce caching time.'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bulk_profile_cors_enabled(response_type: Annotated[str, Field(description='')],
                              ig: Annotated[str, Field(description='')],
                              corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This API Images and Video url can be used directly in browser'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'response_type': response_type,
        'ig': ig,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bulk_profile(response_type: Annotated[str, Field(description='')],
                 ig: Annotated[str, Field(description='')],
                 corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Scrap Instagram Profile using username. This API response take around 5-6 seconds scrap one profile with post. It is designed and capable to handle bulk request. but we recommend to add 5-10 seconds random delay between each request. This API also support optional parameter corsEnabled to generate image/video link which can be directly used in Browser'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'response_type': response_type,
        'ig': ig,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_username(ig: Annotated[str, Field(description='')],
                    response_type: Annotated[str, Field(description='')],
                    corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''**Contact me for Custom package or requirements** This API will be usefull for Instagram username validation or finding similar usernames to pick correct one. This API also support CORS enabled image URL.'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def bulk_profile_by_pk(ig: Annotated[str, Field(description='')],
                       response_type: Annotated[str, Field(description='')],
                       corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This API return time will be faster, As this fetch profile data directly from userid (pk) Scrap instagram profile by pk'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def suggested_profiles(ig: Annotated[str, Field(description='')],
                       response_type: Annotated[str, Field(description='')]) -> dict: 
    '''Instagram Discover Profiles endpoint'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tagged_posts(ig: Annotated[str, Field(description='')],
                 corsEnabled: Annotated[str, Field(description='')],
                 nextMaxId: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Instagram Users Tagged posts'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/tagged'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def advance_bulk_profile(response_type: Annotated[str, Field(description='')],
                         ig: Annotated[str, Field(description='')],
                         corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''[Available on Request] Scrap email and phone number using this api Scrap Instagram Profile using username. This API response take around 5-6 seconds scrap one profile with post. It is designed and capable to handle bulk request. but we recommend to add 5-10 seconds random delay between each request. This API also support optional parameter corsEnabled to generate image/video link which can be directly used in Browser'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/advance_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'response_type': response_type,
        'ig': ig,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pk_to_username(pk: Annotated[str, Field(description='')]) -> dict: 
    '''Get Username from pk/id'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/pk_to_username'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pk': pk,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def validate_username(username: Annotated[str, Field(description='')]) -> dict: 
    '''**Contact me for Custom package or requirements** This API will be usefull for Instagram username validation or finding similar usernames to pick correct one.'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/username_validation'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def about_account(pk: Annotated[str, Field(description='')]) -> dict: 
    '''**Contact me for Custom package or requirements** This API will be useful to get Instagram about account information such as date joined or account country etc'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/about_info'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pk': pk,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_feed_by_hashtags(tag: Annotated[str, Field(description='')],
                         feed_type: Annotated[str, Field(description='')],
                         corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                         nextMaxId: Annotated[Union[str, None], Field(description='Use to load next batch. Pass this value from previous api response')] = None) -> dict: 
    '''Get Instagram Feeds by Hashtag'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/media_by_tag'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tag': tag,
        'feed_type': feed_type,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtags_search(name: Annotated[str, Field(description='')],
                    corsEnabled: Annotated[str, Field(description='')]) -> dict: 
    '''Search hashtags on Instagram'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/search_hashtags'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_with_cursor(ig: Annotated[str, Field(description='')],
                     corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                     nextMaxId: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This API return time will be faster, As this fetch profile data directly from userid (pk) Scrap instagram profile by pk or username'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/feeds'
    headers = {'ig': 'fairytalefolkdorset', 'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_post_by_shortcode(shortcode: Annotated[str, Field(description='')],
                          response_type: Annotated[str, Field(description='')]) -> dict: 
    '''**Contact me for Custom package or requirements** Fetch Instagram post/feed from shortcode'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/media_by_id'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'shortcode': shortcode,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_feed_by_username(ig: Annotated[str, Field(description='')],
                         response_type: Annotated[str, Field(description='')]) -> dict: 
    '''Get Instagram Profile Feeds by Username'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_likers(media_id: Annotated[str, Field(description='')],
                corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''[Under Maintenance] Get Instagram Post Likers list by media_id'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/liker_by_media'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'media_id': media_id,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def post_commenter(media_id: Annotated[str, Field(description='')],
                   corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                   nextMinId: Annotated[Union[str, None], Field(description='Encoded URL content of whole JSON object Browser Console Example: encodeURIComponent(decodeURI(Your JSON String)) Example Value: %7B%22cached_comments_cursor%22%3A%20%2218142440796202967%22%2C%20%22bifilter_token%22%3A%20%22KKEBAEJEOfp_qT8AhH3X4HKlPwBEQXS88tI_AIhv3iz-nz8ATKsDM6e7PwANscnnWbE_AM47SjD8fD8AEAQV9lKPQABRH4m_idU_ANP3u_xobj8AWeQ7JEjXQABZUoETn68_ABvmpdJksT8AIkvNnjdoQACoNqIOTKk_AOoixmjiiz8ANJaxT-SlPwD6zgQE9INAADsPnDQIlj8AvF-5NdaZPwAA%22%7D')] = None) -> dict: 
    '''[Under Maintenance] Get Instagram Post Commenter's list by media_id'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/commenter_by_media'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'media_id': media_id,
        'corsEnabled': corsEnabled,
        'nextMinId': nextMinId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_story_by_username(ig: Annotated[str, Field(description='')],
                          response_type: Annotated[str, Field(description='')]) -> dict: 
    '''Fetch Instagram stories from username'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def story_highlights(ig: Annotated[str, Field(description='')],
                     response_type: Annotated[str, Field(description='')]) -> dict: 
    '''Instagram Story Highlights'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_story_by_shortcode(shortcode: Annotated[str, Field(description='')],
                           response_type: Annotated[str, Field(description='')]) -> dict: 
    '''Fetch Instagram story from shortcode'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/media_by_id'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'shortcode': shortcode,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def highlights_tray_by_id(id: Annotated[str, Field(description='')],
                          response_type: Annotated[str, Field(description='')],
                          corsEnabled: Annotated[str, Field(description='')]) -> dict: 
    '''Fetch Instagram story highlights tray list by Highlight id'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/media_by_id'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'response_type': response_type,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_reels_by_shortcode(shortcode: Annotated[str, Field(description='')],
                           response_type: Annotated[str, Field(description='')]) -> dict: 
    '''**Contact me for Custom package or requirements** Fetch Instagram reels/clips from short code'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/media_by_id'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'shortcode': shortcode,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_reels_by_pk(ig: Annotated[str, Field(description='')],
                    response_type: Annotated[str, Field(description='')]) -> dict: 
    '''Fetch Instagram reels/clips from username'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'response_type': response_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reels_with_cursor(ig: Annotated[str, Field(description='')],
                      corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                      nextMaxId: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Scrap instagram reels by pk or username'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/reels'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ig': ig,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def reels_by_music_id(query: Annotated[str, Field(description='')],
                      request_type: Annotated[str, Field(description='')],
                      nextMaxId: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Instagram reels music by id You can use nextMaxId to fetch next page'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/music'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'request_type': request_type,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def followers_by_username(username: Annotated[str, Field(description='')],
                          nextMaxId: Annotated[Union[str, None], Field(description='Leave this empty in first batch')] = None,
                          corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''[Under Maintenance] Fetch followers list Carry forward nextMaxId to retrieve next batch'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/followers'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'nextMaxId': nextMaxId,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def followers_by_pk(pk: Annotated[str, Field(description='')],
                    corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                    nextMaxId: Annotated[Union[str, None], Field(description='Leave this empty in first batch')] = None) -> dict: 
    '''Fetch followers list Carry forward nextMaxId to retrieve next batch'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/followers'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pk': pk,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def followings_by_pk(pk: Annotated[str, Field(description='')],
                     corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                     nextMaxId: Annotated[Union[str, None], Field(description='Leave this empty in first batch')] = None) -> dict: 
    '''Fetch following list Carry forward nextMaxId to retrieve next batch'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/following'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'pk': pk,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def followings_by_username(username: Annotated[str, Field(description='')],
                           corsEnabled: Annotated[Union[str, None], Field(description='')] = None,
                           nextMaxId: Annotated[Union[str, None], Field(description='Leave this empty in first batch')] = None) -> dict: 
    '''[Under Maintenance] Fetch following list Carry forward nextMaxId to retrieve next batch'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/following'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'corsEnabled': corsEnabled,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def music_search_by_keyword(query: Annotated[str, Field(description='')],
                            nextMaxId: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''**Contact me for Custom package or requirements** Search Music by Keyword You can pass nextMaxId to fetch more reels'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/audio'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'nextMaxId': nextMaxId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_feed_by_location_id(feed_type: Annotated[str, Field(description='')],
                            loc_id: Annotated[str, Field(description='')],
                            corsEnabled: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get Instagram Feeds by Location'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/media_by_loc'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'feed_type': feed_type,
        'loc_id': loc_id,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_search(name: Annotated[str, Field(description='')],
                    corsEnabled: Annotated[str, Field(description='')]) -> dict: 
    '''Location search on Instagram'''
    url = 'https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/search_locations'
    headers = {'x-rapidapi-host': 'instagram-bulk-profile-scrapper.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'corsEnabled': corsEnabled,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
