<template>
    <div class="appear w-full flex flex-row justify-between items-start">
        <div ref="details" class="shrink-0 flex flex-col justify-start items-start gap-4 border-2 border-black p-4">
            <div v-for="key in Object.keys(data)" :key="key" class="flex flex-row justify-start items-start gap-4">
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
                    <SupplierForm :name="data['name']" :description="data['description']" :email="data['email']" :address="data['address']" :number="data['contact_number']" :isUpdate="true" @updated="reloadData"/>
                </Dropdown>
            </div>
        </div>
        
    </div>
    
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import SupplierForm from '@/components/suppliers/SupplierForm.vue';
    import axios from '@/axios';

    export default {
        name: 'SupplierDetail',
        components: {
            Dropdown,
            SupplierForm
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
                const response = await axios.get(`/suppliers/${this.$route.params.id}`)
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
                const response = await axios.delete(`/suppliers/${this.$route.params.id}`)
                this.$router.push({ name: 'suppliers' });
            }
        }
    }
</script>

<style scoped>
.black-filter {
    filter: invert(100%) grayscale(100%);
}
</style>