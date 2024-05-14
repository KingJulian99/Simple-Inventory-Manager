<template>
    <div v-show="isVisible" class="w-full border-2 border-black flex flex-row justify-start items-start">
        <div class="w-28 flex flex-col justify-start items-start">
            <div class="border-b-2 border-r-2 border-black p-1 bg-red-500">
                <p class="text-base px-4">Error</p>
            </div>
        </div>
        
        <div class="w-full flex flex-col justify-center items-center p-4">
            <ul>
                <li v-for="(error, index) in errors" :key="index" class="underline p-1">
                    {{ error }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'ErrorContainer',
        props: {
            errors: {
                type: Array,
                default: []
            }
        },
        data() {
            return {
                isVisible: false
            }
        },
        watch: {
            errors: {
                handler(newErrors) {
                    if (newErrors.length > 0 && !this.isVisible) {
                        this.isVisible = true;
                    } else if (newErrors.length == 0 && this.isVisible) {
                        this.isVisible = false;
                    }
                },
                deep: true 
            }
        }
    }
</script>