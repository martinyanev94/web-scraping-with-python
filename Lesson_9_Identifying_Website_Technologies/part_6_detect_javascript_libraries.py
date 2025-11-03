def search_for_javascript_libraries(soup):
    script_tags = soup.find_all('script')
    libraries = []
    
    for tag in script_tags:
        if 'jquery' in str(tag):
            libraries.append('jQuery detected')
        elif 'react' in str(tag):
            libraries.append('React detected')

    return libraries

additional_libraries = search_for_javascript_libraries(soup)
print(additional_libraries)
