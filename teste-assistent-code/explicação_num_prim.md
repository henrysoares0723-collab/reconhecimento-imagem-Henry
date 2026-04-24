# Explicação da Função is_prime

A função `is_prime(number: int) -> bool` verifica se um número inteiro `number` é primo. Um número primo é aquele maior que 1 que não tem divisores positivos além de 1 e ele mesmo.

## Código da Função

```python
def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    A prime number is greater than 1 with no positive divisors other than 1 and itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
```

## Explicação Passo a Passo

1. **Verificação inicial**: Se `number` for menor ou igual a 1, a função retorna `False` imediatamente, pois números primos são maiores que 1.

2. **Loop de verificação**: O loop `for` itera sobre `divisor` começando de 2 até a raiz quadrada de `number` (usando `int(number ** 0.5) + 1` para incluir o valor arredondado). Isso é eficiente porque se `number` tem um divisor maior que sua raiz quadrada, o outro divisor será menor.

3. **Teste de divisibilidade**: Dentro do loop, se `number % divisor == 0` (ou seja, `number` é divisível por `divisor`), então `number` não é primo e a função retorna `False`.

4. **Retorno final**: Se nenhum divisor for encontrado no loop, a função retorna `True`, indicando que `number` é primo.

## Melhorias Aplicadas (Clean Code)

- **Type Hints**: Adicionados `number: int` e `-> bool` para indicar o tipo do parâmetro e retorno, melhorando a legibilidade e permitindo verificações estáticas.
- **Docstring**: Incluída uma docstring detalhada explicando o propósito, argumentos e retorno da função.
- **Nomes Descritivos**: O parâmetro foi renomeado de `n` para `number`, e a variável do loop de `i` para `divisor`, tornando o código mais autoexplicativo.
- **Formatação**: Código formatado de acordo com convenções Python (PEP 8), com indentação consistente.

## Exemplos de Uso

- `is_prime(5)` retorna `True` (5 é primo).
- `is_prime(4)` retorna `False` (4 não é primo, pois é divisível por 2).
- `is_prime(1)` retorna `False` (1 não é primo).
- `is_prime(2)` retorna `True` (2 é o menor primo).