<template>
    
    <div class="appear w-full h-full flex flex-col justify-start items-center">
        <div class="w-full h-24">
            <FilterSection :categories="categories" :suppliers="suppliers" :categoryFilters="categoryFilters" :supplierFilters="supplierFilters" @addCategoryFilter="addCategoryFilter" @removeCategoryFilter="removeCategoryFilter" @addSupplierFilter="addSupplierFilter" @removeSupplierFilter="removeSupplierFilter"/>
        </div>
    </div>
    
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import DataTable from '@/components/shared/DataTable.vue';
    import FilterSection from '@/components/inventory/FilterSection.vue';
    import CategoryForm from '@/components/categories/CategoryForm.vue';
    import axios from '@/axios';

    export default {
        name: 'Inventory',
        components: {
            Dropdown,
            DropdownRow,
            FilterSection,
            CategoryForm,
            DataTable
        },
        data() {
            return {
                categories: [],
                suppliers: [],
                categoryFilters: [],
                supplierFilters: []
            }
        },
        created() {
            this.loadData();
        },
        methods: {
            loadData() {
                this.getCategories();
                this.getSuppliers();
            },
            async getCategories() {
                const response = await axios.get('/categories');
                this.categories = response.data.objects;
            },
            async getSuppliers() {
                const response = await axios.get('/suppliers');
                this.suppliers = response.data.objects;
            },
            addCategoryFilter(category) {
                const exists = this.categoryFilters.some(item => item.id === category.id);

                if (!exists) {
                    this.categoryFilters.push(category);
                }
            },
            removeCategoryFilter(category) {
                this.categoryFilters = this.categoryFilters.filter(item => item.id != category.id);
            },
            addSupplierFilter(supplier) {
                const exists = this.supplierFilters.some(item => item.id === supplier.id);

                if (!exists) {
                    this.supplierFilters.push(supplier);
                }
            },
            removeSupplierFilter(supplier) {
                this.supplierFilters = this.supplierFilters.filter(item => item.id != supplier.id);
            }
        }
    }
</script>