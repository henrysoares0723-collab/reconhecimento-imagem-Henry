# Explicação dos Erros e Correções em debug.py

Este documento descreve todos os erros encontrados no código e como foram corrigidos.

## Erros Identificados

### Erro 1: Falta de Aspas em String (Linha 6)
**Localização:** `item1 = float(input(Preço do item 1? ))`

**Problema:** A string `Preço do item 1?` não está entre aspas duplas ou simples.

**Causa:** Em Python, todas as strings literais devem estar envolvidas por aspas. Sem elas, o interpretador tenta identificar "Preço" como uma variável, causando um erro de sintaxe.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### Erro 2: Tipo de Dados Incorreto (Linha 20)
**Localização:** `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`

**Problema:** A função `input()` retorna uma string, mas no código a variável é usada em operações matemáticas (`desconto_cupom / 100` e `desconto_cupom > 0`).

**Causa:** Strings não podem ser comparadas diretamente com números em operações aritméticas. Isso causa um erro de tipo `TypeError`.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

### Erro 3: F-string Faltando (Linha 33)
**Localização:** `print(" Item 2:        R$ {total_item2:.2f}")`

**Problema:** A string contém uma interpolação `{total_item2:.2f}` mas não possui o prefixo `f` que indica uma f-string.

**Causa:** Sem o `f` no início, Python trata a string como literal e não substitui as variáveis pelos seus valores.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### Erro 4: Indentação Incorreta (Linha 38-39)
**Localização:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problema:** O bloco `print` dentro da estrutura `if` não está indentado corretamente.

**Causa:** Em Python, blocos de código dentro de estruturas de controle (`if`, `for`, `while`, etc.) devem ser indentados. Sem a indentação apropriada, o Python não consegue identificar que o print faz parte do if.

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## Código Corrigido

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

## Resumo das Correções

| Erro | Linha | Tipo | Solução |
|------|-------|------|---------|
| Falta de aspas | 6 | Sintaxe | Adicionar aspas: `"Preço do item 1? "` |
| Tipo incorreto | 20 | Tipo de Dados | Converter para float: `float(input(...))` |
| F-string faltando | 33 | Formatação | Adicionar `f` antes da string |
| Indentação | 38-39 | Sintaxe | Indentar o bloco `print` dentro do `if` |