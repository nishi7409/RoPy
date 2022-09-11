import requests

def getGroupInfo(groupID):
    response = requests.get(f'https://groups.roblox.com/v2/groups?groupIds={groupID}')
    if response.status_code == 200:
        response = response.json()["data"][0]
        data = {
            "id": response["id"],
            "name": response["name"],
            "description": response["description"],
            "ownerID": response["owner"]["id"]
        }
        return data
    else:
        return response.json()["errors"][0]["message"]

def getUserRanks(userID):
    response = requests.get(f'https://groups.roblox.com/v2/users/{userID}/groups/roles')
    if response.status_code == 200:
        data = dict()
        for index, value in enumerate(response.json()["data"]):
            data[value["group"]["id"]] = value["role"]["rank"]
        return data
    else:
        return response.json()["errors"][0]["message"]

def getRankName(groupID, rankID):
    response = requests.get(f'https://groups.roblox.com/v1/groups/{groupID}/roles')
    if response.status_code == 200:
        for index, value in enumerate(response.json()["roles"]):
            if value["rank"] == rankID:
                return value["name"]
        return f'There is no rank name associated to the rank ID of: {rankID}'
    else:
        return response.json()["errors"][0]["message"]

def setRank(groupID, userID, newRankID):
    pass

def promote(groupID, userID):
    pass

def demote(groupID, userID):
    pass

def deleteWallPost(groupID, postID):
    pass

def exile(groupID, userID):
    pass

def getAuditLog(groupID):
    pass
