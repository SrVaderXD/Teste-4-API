<script>
export default {
  data() {
    return {
      search : "",
      operadoras : []
    }
  },
  methods: {
    async submit() {
      console.log("D:")
      const response = await fetch("http://127.0.0.1:8000/cadastros/procurar?palavra=" + this.search)
      const operadoras = await response.json()
      this.operadoras = operadoras.resultado
    }
  }
}
</script>

<template>
  <header>
    <h1>
      Cadastros de Operadoras
    </h1>

  <form @submit.prevent = "submit">
    <input type="text" v-model="search" placeholder="Exemplo: UNIMED">
    <button>
      Pesquisar
    </button>
  </form>
  </header>

  <main>
    <table>
    <tr>
      <th>
        Registro Ans
      </th>

      <th>
        CNPJ
      </th>

      <th>
        Razão Social
      </th>

      <th>
        Nome Fantasia
      </th>

      <th>
        Modalidade
      </th>

      <th>
        Logradouro
      </th>

      <th>
        Número
      </th>

      <th>
        Complemento
      </th>

      <th>
        Bairro
      </th>

      <th>
        Cidade
      </th>

      <th>
        UF
      </th>

      <th>
        CEP
      </th>

      <th>
        DDD
      </th>

      <th>
        Telefone
      </th>

      <th>
        Fax
      </th>

      <th>
        Endereço Eletrônico
      </th>

      <th>
        Representante
      </th>

      <th>
        Cargo Representate
      </th>

      <th>
        Região de Comercialização
      </th>

      <th>
        Data Registro ANS
      </th>
    </tr>

    <tr v-for = "operadora in operadoras">
      <td>
        {{operadora.registro_ans}}
      </td>
      <td>
        {{operadora.cnpj}}
      </td>
      <td>
        {{operadora.razao_social}}
      </td>
      <td>
        {{operadora.nome_fantasia}}
      </td>
      <td>
        {{operadora.modalidade}}
      </td>
      <td>
        {{operadora.logradouro}}
      </td>
      <td>
        {{operadora.numero}}
      </td>
      <td>
        {{operadora.complemento}}
      </td>
      <td>
        {{operadora.bairro}}
      </td>
      <td>
        {{operadora.cidade}}
      </td>
      <td>
        {{operadora.uf}}
      </td>
      <td>
        {{operadora.cep}}
      </td>
      <td>
        {{operadora.ddd}}
      </td>
      <td>
        {{operadora.telefone}}
      </td>
      <td>
        {{operadora.fax}}
      </td>
      <td>
        {{operadora.enderco_eletronico}}
      </td>
      <td>
        {{operadora.representante}}
      </td>
      <td>
        {{operadora.cargo_representante}}
      </td>
      <td>
        {{operadora.regiao_de_comercializacao}}
      </td>
      <td>
        {{operadora.data_registro_ans}}
      </td>
    </tr>
    </table>

  </main>

</template>

<style scoped>
  header {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-bottom: 30px;
    color: rgb(212, 212, 212);
  }

  header h1 {
    font-size: 48px;
    font-weight: bold;
  }

  form button {
    border: 2px solid rgb(71, 71, 71);
    background-color: rgb(188, 188, 188);
    color : black;
    padding: 14px 28px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 10px;
  }

  form button:hover {
    background: rgb(231, 231, 231);
  }

  form input {
    margin-right: 10px;
    border: 2px solid rgb(71, 71, 71);
    background-color: rgb(188, 188, 188);
    padding: 14px 60px;
    font-size: 16px;
    padding-left: 10px;
    border-radius: 10px;
  }

  form input::placeholder {
    color: black;
  }

  table {
    width: 100%;
  }

  tr {
    background-color: #2f2f2f;
  }

  tr:nth-child(even) {
    background-color: #242424
  }

  td {
    text-align: center;
  }
</style>