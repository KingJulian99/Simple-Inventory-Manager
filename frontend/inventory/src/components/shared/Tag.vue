<template>
    <div class="disappear parent w-fit h-full flex flex-row justify-start items-center border-2 border-black">
        <div @click="remove" class="brother w-full h-full flex flex-col justify-center items-start p-2 hover:cursor-pointer  hover:bg-red-500 transition-all duration-200">
            <p :class="{'text-lg': size=='lg', 'text-base': size=='md', 'text-sm': size=='sm'}" class="font-bold">X</p>
        </div>
        <div class="sister w-full h-full flex flex-col justify-center items-start p-2 pl-0 transition-all duration-200">
            <p :class="{'text-lg': size=='lg', 'text-base': size=='md', 'text-sm': size=='sm'}">{{ text }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Tag',
        props: {
            text: {
                type: String,
                default: ''
            },
            size: {
                type: String,
                default: 'md'
            }
        },
        methods: {
            remove() {
                this.$emit('remove');
            }
        }
    }
</script>

<style scoped>
.brother:hover ~ .sister {
  background-color: rgb(239 68 68);
}
</style>