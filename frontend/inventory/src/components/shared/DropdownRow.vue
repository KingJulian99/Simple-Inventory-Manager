<template>
    <div class="group w-full flex flex-row justify-start items-center border-b-2 border-black hover:cursor-pointer bg-white hover:bg-stone-200 transition-all duration-200" :class="{['h-6']: size === 'sm', ['h-10']: size === 'md', ['h-16']: size === 'lg', ['p-2']: size === 'sm', ['p-4']: size === 'md', ['p-8']: size === 'lg'}">
        <p class="group-hover:translate-x-2 transition-all duration-200" :class="{['text-sm']: size === 'sm', ['text-base']: size === 'md', ['text-lg']: size === 'lg'}">{{ text }}</p>
    </div>
</template>

<script>
    export default { 
        name: 'DropdownRow',
        props: {
            text: {
                type: String,
                default: ''
            },
            size: {
                type: String,
                default: 'md'
            }
        }
    }
</script>