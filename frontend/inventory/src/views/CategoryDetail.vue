<template>
    <div class="appear w-full flex flex-row justify-between items-start">
        <div ref="details" class="shrink-0 flex flex-col justify-start items-start gap-4 border-2 border-black p-4">
            <div v-for="key in Object.keys(data)" :key="key" class="flex flex-row justify-start items-start">
                <div class="w-32 font-bold flex flex-col justify-center items-start">
                    {{ key }}
                </div>
                <div class="flex flex-col justify-center items-start">
                    {{ data[key] }}
                </div>
            </div>
        </div>

        <div class="w-full flex flex-row justify-end items-start gap-4">
            <div @click="handleDelete" :class="{'bg-red-500': deleteCheck, 'hover:bg-stone-400': !deleteCheck, 'w-20': !deleteCheck, 'w-48': deleteCheck}" class="h-20 gap-2 border-2 border-black flex flex-row justify-center items-center cursor-pointer transition-all duration-200">
                <img src="/images/bin.svg" class="h-2/3 black-filter">
                <p v-show="deleteCheck" class="appear">Are you sure?</p>
            </div>
            <div v-if="Object.keys(data).length > 0" class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
                <Dropdown ref="formDropdown" textSizeClass="text-xl" paddingSizeClass="p-4" title="Edit Category">
                    <CategoryForm :name="data['name']" :description="data['description']" :isUpdate="true" @updated="reloadData"/>
                </Dropdown>
            </div>
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
                data: {},
                deleteCheck: false
            }
        },
        created() {
            this.loadData();
        },
        methods: {
            async reloadData() {
                await this.loadData();
                this.$refs['formDropdown'].toggle();
                this.$refs['details'].classList.add('flash-green');
                setTimeout(() => {
                    this.$refs['details'].classList.remove('flash-green');
                }, 500);
            },
            async loadData() {
                const response = await axios.get(`/categories/${this.$route.params.id}`)
                this.data = response.data.object;
            },
            handleDelete() {
                if (this.deleteCheck) {
                    this.tryDelete();
                } else {
                    this.deleteCheck = true;

                    setTimeout(() => {
                        this.deleteCheck = false;
                    }, 3000)
                }
            },
            async tryDelete() {
                const response = await axios.delete(`/categories/${this.$route.params.id}`)
                this.$router.push({ name: 'categories' });
            }
        }
    }
</script>

<style scoped>
.black-filter {
    filter: invert(100%) grayscale(100%);
}
</style>