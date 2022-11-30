import { ref, computed } from 'vue'

export const collapsed = ref(false)
export const toggleNavBar = () => (collapsed.value = !collapsed.value)

// export const NAVBAR_WIDTH = 180
export const NAVBAR_WIDTH = 250
// export const NAVBAR_WIDTH_COLLAPSED = 38
export const NAVBAR_WIDTH_COLLAPSED = 120
export const navbarWidth = computed(
    () => `${collapsed.value ? NAVBAR_WIDTH_COLLAPSED : NAVBAR_WIDTH}px`
)