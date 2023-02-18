<script>
  import fastApi from '../lib/api';
  import Error from '../components/Error.svelte';

  export let params = {};
  let question_id = params.question_id;
  let question = { answers: [] };
  let content = '';
  let error = { detail: [] };

  const get_question = () => {
    fastApi('get', '/api/question/detail/' + question_id, {}, (json) => {
      question = json;
    });
  };

  get_question();

  const post_answer = (event) => {
    event.preventDefault();
    let url = '/api/answer/create' + question_id;
    let params = {
      content: content,
    };
    fastApi(
      'post',
      url,
      params,
      (json) => {
        content = '';
        error = { detail: [] }; // 재시도 후 성공 시 오류 초기화
        get_question();
      },
      (err_json) => {
        error = err_json;
      }
    );
  };
</script>

<h1>{question.subject}</h1>
<div>{question.content}</div>
<ul>
  {#each question.answers as answer}
    <li>{answer.content}</li>
  {/each}
</ul>
<Error {error} />
<form method="post">
  <textarea rows="15" bind:value={content} />
  <input type="submit" value="답변 등록" on:click={post_answer} />
</form>

<style>
  textarea {
    width: 100%;
  }
  input[type='submit'] {
    margin-top: 10px;
  }
</style>
