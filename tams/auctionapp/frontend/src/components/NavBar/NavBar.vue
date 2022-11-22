<template>
    <div class="navbar" :style="{ width: navbarWidth }">
        <h1>
            <span v-if="collapsed">
                <div>A</div>
                <div>A</div>
            </span>
            <span v-else>Auction App</span>
        </h1>
        <span
          class="collapse-icon"
          :class="{ 'rotate-180': collapsed }"
          @click="toggleNavBar"
        >
          <i class="fas fa-angle-double-left" />
        </span>
    </div>
</template>

<script lang="ts">
import { collapsed, toggleNavBar, navbarWidth } from './state';
export default {
    // props: {},
    // in props make readonly:true to not get error
    setup() {
        return { collapsed, toggleNavBar, navbarWidth }

    }
}
</script>

<style>
:root {
    --navbar-bg-color: #2f855a ;
    --navbar-item-hover: #38a169;
    --navbar-item-active: #276749;
}
</style>

<style scoped>
.navbar {
    color: white;
    background-color: var(--navbar-bg-color);

    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;

    transition: 0.3s ease;

    display: flex;
    flex-direction: column;
}

.collapse-icon {
    position: absolute;
    bottom: 0;
    padding: 0.75em;

    color: rgba(255, 255, 255, 0.7);

    transition: 0.2s linear;
}

.rotate-180 {
    transform: rotate(180deg);
    transition: 0.2s linear;
}
</style>