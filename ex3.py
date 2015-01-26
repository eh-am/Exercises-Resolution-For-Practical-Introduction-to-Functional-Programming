def zero(s):
    if s[0] == "0":
        return s[1:]

def one(s):
    if s[0] == "1":
        return s[1:]

def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break

    return s



print rule_sequence('0101', [zero, one, zero])

print rule_sequence('0101', [zero, zero])


def rule_sequence_rec(s, rules):
  # Se a regra não bateu ou acabou de aplicar as regras
  if (s == None or len(rules) == 0):
    return s 

  # Roda a função com o resultado da regra aplicada e o resto das regras
  return rule_sequence_rec(rules[0](s), rules[1:])


print rule_sequence_rec('0101', [zero, one, zero])

print rule_sequence_rec('0101', [zero, zero])