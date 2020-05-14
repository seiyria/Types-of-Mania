
// @ts-nocheck
import * as childProcess from 'child_process';
import dlgit from 'download-git-repo';
import * as rimraf from 'rimraf';

rimraf.sync('tmp');

dlgit('seiyria/tompp', 'tmp', e => {
  if(e) {
    console.error(e);
    return;
  }

  childProcess.execSync(`npm i && npm run electron:windows`, { cwd: './tmp' });

});