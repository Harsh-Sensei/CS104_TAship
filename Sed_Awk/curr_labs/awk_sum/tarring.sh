rm -rf .evaluationScripts
cp -r evaluationScripts .evaluationScripts
sed -i s,../evaluationScripts,/home/.evaluationScripts, .evaluationScripts/evaluate.sh
chmod 777 -R .evaluationScripts
tar -cvzf clientEvaluationFiles.tgz .evaluationScripts
tar -cvzf lab.tgz labDirectory