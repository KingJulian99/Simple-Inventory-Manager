<template>
    <div class="appear w-full flex flex-row justify-between items-start">
        <div ref="details" class="shrink-0 flex flex-col justify-start items-start gap-4 border-2 border-black p-4">
            <div v-for="key in Object.keys(data)" :key="key" v-show="ignoredKeys.indexOf(key) == -1" class="flex flex-row justify-start items-start">
                <div class="w-36 font-bold flex flex-col justify-center items-start">
                    {{ key }}
                </div>
                <div class="flex flex-col justify-center items-start">
                    {{ data[key] }}
                </div>
            </div>

            <div class="w-full flex flex-row justify-start items-center">
                <div class="w-36 shrink-0 font-bold flex flex-col justify-center items-start">
                    product
                </div>
                <div v-if="data.product" class="w-full flex flex-row justify-start items-start flex-wrap">
                    <Tag :text="data.product.name" :readOnly="true" :isClickable="true" pathName="productDetail" :pathParam="String(data.product.id)"/>
                </div>
            </div>

            <div class="w-full flex flex-row justify-start items-center">
                <div class="w-36 shrink-0 font-bold flex flex-col justify-center items-start">
                    supplier
                </div>
                <div v-if="data.supplier" class="w-full flex flex-row justify-start items-start flex-wrap">
                    <Tag :text="data.supplier.name" :readOnly="true" :isClickable="true" pathName="supplierDetail" :pathParam="String(data.supplier.id)"/>
                </div>
            </div>
           
        </div>

        <div class="w-full flex flex-row justify-end items-start gap-4">
            <div @click="handleDelete" :class="{'bg-red-500': deleteCheck, 'hover:bg-stone-400': !deleteCheck, 'w-20': !deleteCheck, 'w-48': deleteCheck}" class="h-20 gap-2 border-2 border-black flex flex-row justify-center items-center cursor-pointer transition-all duration-200">
                <img src="/images/bin.svg" class="h-2/3 black-filter">
                <p v-show="deleteCheck" class="appear">Are you sure?</p>
            </div>
            <div v-if="Object.keys(data).length > 0" class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
                <Dropdown ref="formDropdown" textSizeClass="text-xl" paddingSizeClass="p-4" title="Edit Inventory Item">
                    <InventoryItemForm :product="data.product" :supplier="data.supplier" :purchase_price="data.purchase_price" :isUpdate="true" @updated="reloadData"/>
                </Dropdown>
            </div>
        </div>
        
    </div>
    
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import InventoryItemForm from '@/components/inventory/InventoryItemForm.vue';
    import Tag from '@/components/shared/Tag.vue';
    import axios from '@/axios';

    export default {
        name: 'InventoryDetail',
        components: {
            Dropdown,
            InventoryItemForm,
            Tag
        },
        data() {
            return {
                data: {},
                ignoredKeys: ['product', 'supplier'],
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
                const response = await axios.get(`/inventory/${this.$route.params.id}`)
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
                const response = await axios.delete(`/inventory/${this.$route.params.id}`)
                this.$router.push({ name: 'inventory' });
            }
        }
    }
</script>