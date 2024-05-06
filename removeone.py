from bs4 import BeautifulSoup


def remove_tags(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

 
    tr_elements = soup.find_all('tr')

  
    for tr in tr_elements:
        td_elements = tr.find_all('td')

        # Check if all <td> elements meet the conditions
        if (len(td_elements) == 3 and
                td_elements[0].a and td_elements[0].a.get('href') == '#10104' and
                td_elements[0].a.text.strip() == 'User Agent Fuzzer' and
                td_elements[1].get('align') == 'center' and td_elements[1].get('class') == ['risk-0'] and
                td_elements[1].text.strip() == 'Informational' and
                td_elements[2].get('align') == 'center' and td_elements[2].text.strip() == '88'):
            # Remove the <tr> element
            tr.extract()
    table_elements = soup.find_all('table')
    id_value='10104'
    for table in table_elements:
           # Find the <a> tag with the specified id
        a_tag = table.find('a', id=id_value)
        
        # Check if the <a> tag with the specified id exists
        if a_tag:
            # Remove the entire table
            table.extract()
        #     # Find all <td> elements within the <tr>
        # tr_elements = table.find_all('tr')

        # # Check if all <td> elements meet the conditions
        # if (tr_elements[0].a and tr_elements[0].a.get('id') == '#10104'):
        #     # Remove the <tr> element
        #     table.extract()

    modified_html = soup.prettify()

    with open(html_file, 'w') as file:
        file.write(modified_html)

