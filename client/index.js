import React from 'react';
import ReactDOM from 'react-dom';
import Root from './components/Root';
import registerServiceWorker from './registerServiceWorker'

document.addEventListener("DOMContentLoaded", () => {
  const root = document.getElementById('root')
  ReactDOM.render(<Root />, root);
  // registerServiceWorker();
}
);

