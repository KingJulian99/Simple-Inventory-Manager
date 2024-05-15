<template>
    <div class="relative w-full h-full">
        <div @click="toggle" class="w-full h-full flex flex-row justify-start items-center gap-4 border-2 border-black select-none transition-all duration-200 hover:cursor-pointer hover:bg-stone-400" :class="{[paddingSizeClass]: true}">
            <div class="flex flex-col justify-center items-center scale-75 transition-all duration-200" :class="{[textSizeClass]: true, ['rotate-180']: !isOpen}">
                ▲
            </div>
            <div class="h-full flex flex-col justify-center items-center">
                <p :class="{[textSizeClass]: true}">{{ title }}</p>
            </div>
        </div>

        <div v-show="isOpen" class="absolute dropdown shadow-lg bottom-0 left-0 flex flex-col justify-start items-center w-full translate-y-full border-2 border-b-0 border-slate-700 transition-all duration-200" :class="{['opacity-0']: !isOpen}">
            <slot></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Dropdown',
        props: {
            title: {
                type: String,
                default: 'Title'
            },
            paddingSizeClass: {
                type: String,
                default: 'p-2'
            },
            textSizeClass: {
                type: String,
                default: 'text-lg'
            }
        },
        data() {
            return {
                isOpen: false
            }
        },
        methods: {
            toggle() {
                this.isOpen = !this.isOpen;
            }
        }
    }
</script>

<style scoped>
.dropdown {
    animation: dropdown 100ms ease-in forwards;
}

@keyframes dropdown {
    0% {
        opacity: 0;
        transform: translateY(95%);
    }
    100% {
        opacity: 100;
        transform: translateY(100%);
    }
}
</style>