#!/bin/sh
# Assembles src/* into index.html. Chapter content and past papers stay as
# separate files under data/ and are fetched on demand, so deploy the folder.
set -e
cd "$(dirname "$0")"

{
  cat <<'HEAD'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ATSWA Part II — Study</title>
<meta name="description" content="The four ATSWA Part II subjects as chapter-by-chapter study notes with worked examples, typeset formulas, per-chapter quizzes, and five diets of past papers with expanded solutions.">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F2F1EC" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#12110F" media="(prefers-color-scheme: dark)">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231F6244'/%3E%3Cpath d='M7 6h18v6H13v5h11v6H13v6H7z' fill='%23FCFBF7'/%3E%3C/svg%3E">
</head>
<body>
HEAD
  # the fragment carries its own <title>; the head above owns it now
  grep -v '^<title>ATSWA Part II</title>$' src/page.html
  echo '<script>'
  cat src/subjects.js src/math.js src/render.js src/app.js src/quiz.js src/exams.js
  echo '</script>'
  echo '</body>'
  echo '</html>'
} > index.html

echo "built index.html  $(wc -c < index.html | tr -d ' ') bytes"
for f in data/*.js; do
  [ -e "$f" ] && echo "      $f  $(wc -c < "$f" | tr -d ' ') bytes"
done
