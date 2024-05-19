<template>
    <div @click="handleClick" :class="{'hover:cursor-pointer': isClickable, 'hover:bg-stone-400': isClickable}" class="disappear parent w-fit h-full flex flex-row justify-start items-center border-2 border-black transition-all duration-200">
        <div @click="remove" v-show="!readOnly" class="brother w-full h-full flex flex-col justify-center items-start p-2 hover:cursor-pointer hover:bg-red-500 transition-all duration-200">
            <p :class="{'text-lg': size=='lg', 'text-base': size=='md', 'text-sm': size=='sm'}" class="font-bold">X</p>
        </div>
        <div :class="{'pl-0': !readOnly, 'pl-2': readOnly}" class="sister w-full h-full flex flex-col justify-center items-start p-2 transition-all duration-200">
            <p class="text-nowrap" :class="{'text-lg': size=='lg', 'text-base': size=='md', 'text-sm': size=='sm'}">{{ text }}</p>
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
            },
            readOnly: {
                type: Boolean,
                default: false
            },
            isClickable: {
                type: Boolean,
                default: false
            },
            pathName: {
                type: String,
                default: ''
            },
            pathParam: {
                type: String,
                default: ''
            }
        },
        methods: {
            remove() {
                this.$emit('remove');
            },
            handleClick() {
                if (this.isClickable) {
                    this.$router.push({ name: this.pathName, params: { id: this.pathParam } });
                }
            }
        }
    }
</script>

<style scoped>
.brother:hover ~ .sister {
  background-color: rgb(239 68 68);
}
</style>