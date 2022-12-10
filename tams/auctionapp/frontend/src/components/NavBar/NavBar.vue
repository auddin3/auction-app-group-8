<template>
    <div class="navbar" :style="{ width: navbarWidth }">
        <h1>
            <span v-if="collapsed">
                <div>TAMS</div>
            </span>
            <span v-else>TAMS</span>
        </h1>

        <NavBarLink to="/" icon="fas fa-money-bill-trend-up">Auctions</NavBarLink>
        <NavBarLink to="/search" icon="fas fa-box-archive">Inventory</NavBarLink>
        <NavBarLink to="/profile" icon="fas fa-users">My Profile</NavBarLink>
        <button class="btn btn-light btn-md" icon="fas fa-right-from-bracket" @click.prevent="handleLogout">
            <span class="fas fa-right-from-bracket" aria-hidden="true"></span>
            <div class="d-inline p-l-2" v-if="!collapsed">Logout</div>
        </button>

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
import NavBarLink from '../navbar/NavBarLink.vue';
import { collapsed, toggleNavBar, navbarWidth } from './state';
export default {
    // props: {},
    components: { NavBarLink },
    setup() {
        return { collapsed, toggleNavBar, navbarWidth }
    },
    methods: {
        async handleLogout() {
            console.log('write code')
        },
    },
}
</script>

<style>
:root {
    --navbar-bg-color: #C59FC9 ;
    --navbar-item-hover: #C1E0F7;
    --navbar-item-active: #CFBAE1;
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
    padding: 7.5em 0.5em;

    transition: 0.3s ease;

    display: flex;
    flex-direction: column;
}

.navbar h1 {
  height: 1.0em;
  padding-bottom: 1.5em;
  margin-top: -2.5em;
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

.p-l-2 {
    padding-left: 10px;
}
</style>