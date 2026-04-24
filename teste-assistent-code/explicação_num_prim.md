# Explicação da Função is_prime

A função `is_prime(n)` verifica se um número inteiro `n` é primo. Um número primo é aquele maior que 1 que não tem divisores positivos além de 1 e ele mesmo.

## Código da Função

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

## Explicação Passo a Passo

1. **Verificação inicial**: Se `n` for menor ou igual a 1, a função retorna `False` imediatamente, pois números primos são maiores que 1.

2. **Loop de verificação**: O loop `for` itera sobre `i` começando de 2 até a raiz quadrada de `n` (usando `int(n**0.5) + 1` para incluir o valor arredondado). Isso é eficiente porque se `n` tem um divisor maior que sua raiz quadrada, o outro divisor será menor.

3. **Teste de divisibilidade**: Dentro do loop, se `n % i == 0` (ou seja, `n` é divisível por `i`), então `n` não é primo e a função retorna `False`.

4. **Retorno final**: Se nenhum divisor for encontrado no loop, a função retorna `True`, indicando que `n` é primo.

## Exemplos de Uso

- `is_prime(5)` retorna `True` (5 é primo).
- `is_prime(4)` retorna `False` (4 não é primo, pois é divisível por 2).
- `is_prime(1)` retorna `False` (1 não é primo).
- `is_prime(2)` retorna `True` (2 é o menor primo).