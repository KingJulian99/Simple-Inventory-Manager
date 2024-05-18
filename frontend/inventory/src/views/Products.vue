<template>
    <div class="appear w-full h-full flex flex-row justify-start items-start">
        <div class="w-full h-full">
            <DataTable ref="table" :columnDefinitions="productColumns" :tableData="products"/>
        </div>
    
        <div class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
            <Dropdown ref="formDropdown" textSizeClass="text-xl" paddingSizeClass="p-4" title="Create New Product">
                <ProductForm @created="reloadData"/>
            </Dropdown>
        </div>
    </div>
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import DataTable from '@/components/shared/DataTable.vue';
    import FilterSection from '@/components/inventory/FilterSection.vue';
    import ProductForm from '@/components/products/ProductForm.vue';
    import axios from '@/axios';

    export default {
        name: 'Products',
        components: {
            Dropdown,
            DropdownRow,
            FilterSection,
            ProductForm,
            DataTable
        },
        data() {
            return {
                products: [],
                productColumns: [
                    {
                        header: 'Name',
                        field: 'name'
                    },
                    {
                        header: 'Description',
                        field: 'description'
                    },
                ],
            }
        },
        created() {
            this.loadData();
        },
        methods: {
            async reloadData() {
                await this.loadData();
                this.$refs['formDropdown'].toggle();
                this.$refs['table'].flashGreen();
            },
            loadData() {
                this.getProducts();
            },
            async getProducts() {
                const response = await axios.get('/products');
                this.products = response.data.objects;
            }
        }
    }
</script>