# Write a function that builds html tags. Apply html escaping for html special chars.
# The function will receive 2 parameters – tag type and tag content. It will return the generated html as text.
# - eg: f(‘b’, ‘Ham&Eggs’) returns “<b>Ham&amp;Eggs</b>”
#- HTML char escaping:
# < == &lt;
# > == &gt;
# “ == &quot;
# & == &amp;

def to_html(tag = 'b', text:str = ''):
    text = text.replace('&', "&amp").replace('<', '&lt').replace('>', '&gt').replace('"','&quot')
    text = '<'+tag+'>'+text+'<'+tag+'/>'
    return text

content = 'Formula: " res = a > b & c < d "'
print(to_html('H', content))