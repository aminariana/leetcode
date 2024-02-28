# @param {String} s
# @return {String}
def reverse_words(s)
    s.split(' ').reject(&:empty?).reverse.join(' ')
end
