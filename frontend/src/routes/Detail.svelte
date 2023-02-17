<script>
  import fastApi from '../lib/api';

  export let params = {};
  let question_id = params.question_id;
  let question = {};

  const get_question = () => {
    fastApi('get', '/api/question/detail/' + question_id, {}, (json) => {
      question = json;
    });
  };

  get_question();
</script>

<h1>{question.subject}</h1>
<div>{question.content}</div>
