<script>
  import fastApi from '../lib/api';
  let question_list = [];

  function get_question_list() {
    fastApi('get', '/api/question/list', {}, (json) => {
      question_list = json;
    });
  }

  get_question_list();
</script>

<ul>
  {#each question_list as question}
    <li>{question.subject}</li>
  {/each}
</ul>
