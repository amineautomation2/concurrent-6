import curl_cffi

cookies = {
    "seoUserId": "1f160c76-d272-4f06-a976-dfd2b05692e0",
    "UMB_SESSION": "CfDJ8L%2Fpl3t4kKNAtp5wrfQXQcZFI4xVSsdBAyRXJzOQZGUasSt456bslbGZnqBO1UhTf1kgV0v2ZlPgH3np0ib%2BlKVKsgET725HiDvbvsRV7fxhUAVesUO7fEWHfjyHNKQWGL%2FMuE42brC5CASq%2FerMnW%2Fu3Yegi%2FLXW%2FvKMisc4vyl",
    "invtype": "Adviser",
    "CookieConsent": "{stamp:%27zM+tNuuw/ONycVMRWoV4rZGr7avq4v1G42GuWKKEkgi3s6OPCMHePw==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1782829118586%2Cregion:%27ma%27}",
    ".AspNetCore.Antiforgery.9fXoN5jHCXs": "CfDJ8L_pl3t4kKNAtp5wrfQXQcZsLYo-tkO7-4tQcn381vhxYIGFte08OQXzfu75wY1xe21qxadQKUjUHNdSxspKevwUOtXsmZlhgfOTsXJbYOy203DCXbIIe3W0I9JJn3ZTMw6fFyiZpQEpdAxjJC_tnpk",
    "tn_factsheets": "1",
    "myCustomTab": "AnnualPerf12to24Months|AssetClass",
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.trustnet.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.trustnet.com/fund/price-performance/u/all-universes?norisk=true&PageSize=25",
    "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    # 'cookie': 'seoUserId=1f160c76-d272-4f06-a976-dfd2b05692e0; UMB_SESSION=CfDJ8L%2Fpl3t4kKNAtp5wrfQXQcZFI4xVSsdBAyRXJzOQZGUasSt456bslbGZnqBO1UhTf1kgV0v2ZlPgH3np0ib%2BlKVKsgET725HiDvbvsRV7fxhUAVesUO7fEWHfjyHNKQWGL%2FMuE42brC5CASq%2FerMnW%2Fu3Yegi%2FLXW%2FvKMisc4vyl; invtype=Adviser; CookieConsent={stamp:%27zM+tNuuw/ONycVMRWoV4rZGr7avq4v1G42GuWKKEkgi3s6OPCMHePw==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1782829118586%2Cregion:%27ma%27}; .AspNetCore.Antiforgery.9fXoN5jHCXs=CfDJ8L_pl3t4kKNAtp5wrfQXQcZsLYo-tkO7-4tQcn381vhxYIGFte08OQXzfu75wY1xe21qxadQKUjUHNdSxspKevwUOtXsmZlhgfOTsXJbYOy203DCXbIIe3W0I9JJn3ZTMw6fFyiZpQEpdAxjJC_tnpk; tn_factsheets=1; myCustomTab=AnnualPerf12to24Months|AssetClass',
}

data = {
    "Keywords": "A195",
    "FundUniverse": "U",
    "__RequestVerificationToken": "CfDJ8L_pl3t4kKNAtp5wrfQXQcbh7h1ybBokEMZ0YvlOxnjoH5W3pdq7QjhRQgOSX37i8odMM8tLF6lVHhj1b6eYfQHsMbC7x3CilQARkk1syqc1YFKs2HgSNS6YqnkNKFblq6YRgZbiZhIvJ-1DL0R17lU",
    "X-Requested-With": "XMLHttpRequest",
}

response = curl_cffi.post(
    "https://www.trustnet.com/umbraco/surface/search/SearchAdvanceFund",
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.content)
