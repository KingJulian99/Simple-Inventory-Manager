<template>
    <div @click="fillDB" class="w-20 h-20 flex flex-col justify-center items-center hover:cursor-pointer hover:bg-stone-400 border-black border-2">
        <p>Fill DB</p>
    </div>
</template>

<script>
    import axios from '@/axios';

    export default {
        name: 'Management',
        methods: {
            fillDB() {
                axios.get('/fill');
            }
        }
    }
</script>