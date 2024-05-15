<template>
    <div class="w-full flex flex-row justify-between items-start">
        <div class="shrink-0 flex flex-col justify-start items-start gap-4 border-2 border-black p-4">
            <div v-for="key in Object.keys(data)" :key="key" class="flex flex-row justify-start items-start">
                <div class="w-32 font-bold flex flex-col justify-center items-start">
                    {{ key }}
                </div>
                <div class="flex flex-col justify-center items-start">
                    {{ data[key] }}
                </div>
            </div>
        </div>

        <div class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
            <Dropdown textSizeClass="text-xl" paddingSizeClass="p-4" title="Edit Category">
                <CategoryForm/>
            </Dropdown>
        </div>
    </div>
    
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import CategoryForm from '@/components/categories/CategoryForm.vue';
    import axios from '@/axios';

    export default {
        name: 'CategoryDetail',
        components: {
            Dropdown,
            CategoryForm
        },
        data() {
            return {
                data: {}
            }
        },
        created() {
            this.loadData();
        },
        methods: {
            async loadData() {
                const response = await axios.get(`/categories/${this.$route.params.id}`)
                console.log(response);
                this.data = response.data.object;
                console.log(this.data)
            }
        }
    }
</script>