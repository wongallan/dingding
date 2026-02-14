---
title: Script Reader
layout: default
---

# Script Reader

Read one line at a time with Chinese, romanization, and English shown together.

<div class="script-reader">
  <label for="scene-select"><strong>Scene:</strong></label>
  <select id="scene-select">
    <option value="1">Scene 1</option>
    <option value="2">Scene 2</option>
    <option value="3">Scene 3</option>
    <option value="4">Scene 4</option>
    <option value="5">Scene 5</option>
    <option value="6">Scene 6</option>
    <option value="7">Scene 7</option>
    <option value="8">Scene 8</option>
    <option value="9">Scene 9</option>
  </select>

  <p id="line-position"></p>

  <div class="line-card">
    <p id="line-zh" class="line-zh"></p>
    <p id="line-rom" class="line-rom"></p>
    <p id="line-en" class="line-en"></p>
  </div>

  <div class="line-controls">
    <button id="prev-line" type="button">Previous</button>
    <button id="next-line" type="button">Next</button>
  </div>
</div>

<div id="scene-source" hidden>
  <div data-scene="1">{% capture scene01 %}{% include_relative scene-01.md %}{% endcapture %}{{ scene01 | markdownify }}</div>
  <div data-scene="2">{% capture scene02 %}{% include_relative scene-02.md %}{% endcapture %}{{ scene02 | markdownify }}</div>
  <div data-scene="3">{% capture scene03 %}{% include_relative scene-03.md %}{% endcapture %}{{ scene03 | markdownify }}</div>
  <div data-scene="4">{% capture scene04 %}{% include_relative scene-04.md %}{% endcapture %}{{ scene04 | markdownify }}</div>
  <div data-scene="5">{% capture scene05 %}{% include_relative scene-05.md %}{% endcapture %}{{ scene05 | markdownify }}</div>
  <div data-scene="6">{% capture scene06 %}{% include_relative scene-06.md %}{% endcapture %}{{ scene06 | markdownify }}</div>
  <div data-scene="7">{% capture scene07 %}{% include_relative scene-07.md %}{% endcapture %}{{ scene07 | markdownify }}</div>
  <div data-scene="8">{% capture scene08 %}{% include_relative scene-08.md %}{% endcapture %}{{ scene08 | markdownify }}</div>
  <div data-scene="9">{% capture scene09 %}{% include_relative scene-09.md %}{% endcapture %}{{ scene09 | markdownify }}</div>
</div>

<style>
  .script-reader {
    max-width: 960px;
  }

  .line-card {
    border: 1px solid #d0d7de;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    background: #fff;
  }

  .line-zh {
    font-size: clamp(2rem, 5vw, 3.2rem);
    line-height: 1.3;
    margin: 0.2rem 0 0.8rem;
    font-weight: 700;
  }

  .line-rom {
    font-size: clamp(1.2rem, 3vw, 2rem);
    line-height: 1.4;
    margin: 0.2rem 0 0.8rem;
    color: #333;
  }

  .line-en {
    font-size: clamp(1.1rem, 2.4vw, 1.8rem);
    line-height: 1.5;
    margin: 0.2rem 0;
  }

  .line-controls {
    display: flex;
    gap: 0.6rem;
  }

  .line-controls button {
    font-size: 1rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
  }

  @media (max-width: 640px) {
    .line-controls {
      flex-wrap: wrap;
    }

    .line-controls button {
      flex: 1 1 0;
    }
  }
</style>

<script>
  (function () {
    const sceneSelect = document.getElementById('scene-select');
    const prevButton = document.getElementById('prev-line');
    const nextButton = document.getElementById('next-line');
    const linePosition = document.getElementById('line-position');
    const lineZh = document.getElementById('line-zh');
    const lineRom = document.getElementById('line-rom');
    const lineEn = document.getElementById('line-en');

    const linesByScene = {};

    document.querySelectorAll('#scene-source [data-scene]').forEach((sceneNode) => {
      const sceneLines = [];
      let started = false;
      let triplet = [];

      Array.from(sceneNode.children).forEach((child) => {
        const tag = child.tagName;

        if (tag === 'H2') {
          started = true;
          return;
        }

        if (!started || tag === 'HR') {
          return;
        }

        if (tag !== 'P') {
          return;
        }

        const parts = child.innerText
          .split('\n')
          .map((part) => part.trim())
          .filter(Boolean);

        parts.forEach((part) => {
          triplet.push(part);
          if (triplet.length === 3) {
            sceneLines.push({
              zh: triplet[0],
              rom: triplet[1],
              en: triplet[2]
            });
            triplet = [];
          }
        });
      });

      linesByScene[sceneNode.dataset.scene] = sceneLines;
    });

    let currentScene = sceneSelect.value;
    let currentLineIndex = 0;

    function renderLine() {
      const sceneLines = linesByScene[currentScene] || [];
      const line = sceneLines[currentLineIndex];

      if (!line) {
        linePosition.textContent = 'No lines found in this scene.';
        lineZh.textContent = '';
        lineRom.textContent = '';
        lineEn.textContent = '';
        prevButton.disabled = true;
        nextButton.disabled = true;
        return;
      }

      linePosition.textContent = 'Line ' + (currentLineIndex + 1) + ' of ' + sceneLines.length;
      lineZh.textContent = line.zh;
      lineRom.textContent = line.rom;
      lineEn.textContent = line.en;
      prevButton.disabled = currentLineIndex === 0;
      nextButton.disabled = currentLineIndex >= sceneLines.length - 1;
    }

    sceneSelect.addEventListener('change', () => {
      currentScene = sceneSelect.value;
      currentLineIndex = 0;
      renderLine();
    });

    prevButton.addEventListener('click', () => {
      if (currentLineIndex > 0) {
        currentLineIndex -= 1;
        renderLine();
      }
    });

    nextButton.addEventListener('click', () => {
      const sceneLines = linesByScene[currentScene] || [];
      if (currentLineIndex < sceneLines.length - 1) {
        currentLineIndex += 1;
        renderLine();
      }
    });

    renderLine();
  })();
</script>

---

[← Back to Script Index](index.md) | [← Back to Home](../index.md)
