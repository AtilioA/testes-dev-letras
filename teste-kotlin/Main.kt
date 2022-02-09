import java.util.*

fun substitui_final_duplicado(strings: List<String>): List<String> {
    // Assume-se que a string só possui letras, como especificado; do contrário, poderíamos usar (.+?)
    // Pattern para procurar sequência de letras até encontrar uma ou mais repetições - como o quantificador '?' torna o '+' não guloso, tem boa performance
    val patternRepeticao = "(\\w+?)\\1+$".toRegex()

    // Cria array para acrescentar novas strings
    var stringsDeduplicadas: Array<String> = Array(strings.size) { "" }
    var modificadas: Int = 0

    var novaString: String
    for (string in strings) {
        // Substitui ocorrências do padrão por apenas uma ocorrência - ratoato -> rato, banana -> bana
        // Caso não exista ocorrência, nada acontece, pois o grupo \1 estará vazio
        // novaString = re.sub(patternRepeticao, r"\1", tstring)
        novaString = string.replace(patternRepeticao, "$1")

        // No entanto, neste caso devemos não fazer nada com as outras strings, portanto retornamos as strings originais
        if (novaString == string) {
            return strings
        }
        else {
            stringsDeduplicadas[modificadas] = novaString
            modificadas++
        }
    }

    return stringsDeduplicadas.toList()
}

fun main() {
    var entrada = readLine()!!
    var resposta: String = entrada

    // Divide entrada em múltiplas strings, separando pelo espaço
    var strings = entrada.split(" ")

    // Se alguma palavra de entrada possuir tamanho menor que 1, sabemos que não precisamos fazer nada
    // Teste pouco custoso e que se beneficia de artigos do português de uma única letra ('o', 'a')
    val predicate: (String) -> Boolean = {it.length > 1}
    if (strings.any(predicate)) {
        // Aplica a função substitui_final_duplicado() a todas as palavras
        val stringsDeduplicadas = substitui_final_duplicado(strings)
        // Junta a lista em uma única string, como originalmente
        resposta = stringsDeduplicadas.joinToString(" ")
    }

    // Imprime com ponto final
    println("$resposta.")
}
