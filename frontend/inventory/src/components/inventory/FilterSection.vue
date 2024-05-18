<template>
    <div class="w-full h-24 p-4 flex flex-row justify-start items-center gap-10">
        <h2 class="text-4xl text-nowrap shrink-0">Filter By:</h2>
        
        <div class="w-36 shrink-0 h-10">
            <Dropdown ref="categoryDropdown" title="Category">
                <DropdownRow @click="addCategoryFilter(category)" v-for="(category, index) in categories" :key="index" :text="category.name" size="sm"/>
            </Dropdown>
        </div>

        <div class="w-36 shrink-0 h-10">
            <Dropdown ref="supplierDropdown" title="Supplier">
                <DropdownRow @click="addSupplierFilter(supplier)" v-for="(supplier, index) in suppliers" :key="index" :text="supplier.name" size="sm"/>
            </Dropdown>
        </div>

        <div class="border-r-2 border-dashed border-black">&nbsp;</div>

        <div class="w-full h-10 flex flex-row justify-start items-center gap-2">
            <Tag @remove="removeCategoryFilter(categoryFilter)" v-for="(categoryFilter, index) in categoryFilters" :key="index" :text="categoryFilter.name" class="appear"/>
            <Tag @remove="removeSupplierFilter(supplierFilter)" v-for="(supplierFilter, index) in supplierFilters" :key="index" :text="supplierFilter.name" class="appear"/>
        </div>
        
    </div>
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import Tag from '@/components/shared/Tag.vue';

    export default {
        name: 'FilterSection',
        components: {
            Dropdown,
            DropdownRow,
            Tag
        },
        props: {
            categories: {
                type: Array,
                default: []
            },
            suppliers: {
                type: Array,
                default: []
            },
            categoryFilters: {
                type: Array,
                default: []
            },
            supplierFilters: {
                type: Array,
                default: [] 
            }
        },
        methods: {
            addCategoryFilter(category) {
                this.$refs['categoryDropdown'].toggle();
                this.$emit('addCategoryFilter', category);
            },
            removeCategoryFilter(category) {
                this.$emit('removeCategoryFilter', category);
            },
            addSupplierFilter(supplier) {
                this.$refs['supplierDropdown'].toggle();
                this.$emit('addSupplierFilter', supplier);
            },
            removeSupplierFilter(supplier) {
                this.$emit('removeSupplierFilter', supplier);
            },
        }
    }
</script>