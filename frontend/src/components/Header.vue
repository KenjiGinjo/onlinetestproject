<script setup lang="ts"></script>
<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a class="text-sm font-semibold">笔试项目</a>
    </div>
    <div class="flex-none">
      <ul class="menu menu-horizontal px-1 z-40">
        <li>
          <a
            href="https://www.kenjiginjo.com/"
            target="_blank"
            aria-label="Portfolio"
            >关于我</a
          >
        </li>
        <li>
          <details>
            <summary>More</summary>
            <ul class="p-2 bg-base-100 rounded-t-none">
              <li>
                <a
                  href="https://github.com/kenjiginjo"
                  target="_blank"
                  aria-label="Github"
                  >Github</a
                >
              </li>
              <li>
                <a
                  href="https://www.linkedin.com/in/kenjiginjo/"
                  target="_blank"
                  aria-label="Linkedin"
                  >Linkedin</a
                >
              </li>
            </ul>
          </details>
        </li>
      </ul>
    </div>
  </div>
</template>
