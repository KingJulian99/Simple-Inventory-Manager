<template>
    <div class="w-full h-24 p-4 flex flex-row justify-start items-center gap-10">
        <h2 class="text-4xl text-nowrap shrink-0">Filter By:</h2>
        
        <div class="w-36 shrink-0 h-10">
            <Dropdown title="Category">
                <DropdownRow v-for="(category, index) in categories" :key="index" :text="category" size="sm"/>
            </Dropdown>
        </div>

        <div class="w-36 shrink-0 h-10">
            <Dropdown title="Supplier">
                <DropdownRow v-for="(supplier, index) in suppliers" :key="index" :text="supplier" size="sm"/>
            </Dropdown>
        </div>

        <div class="border-r-2 border-dashed border-black">&nbsp;</div>

        <div class="w-full h-10 flex flex-row justify-start items-center">
            <Filter v-for="(filter, index) in filters" :key="index" :text="filter.text"/>
        </div>
        
    </div>
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import Filter from '@/components/inventory/Filter.vue';

    export default {
        name: 'FilterSection',
        components: {
            Dropdown,
            DropdownRow,
            Filter
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
            filters: {
                type: Array,
                default: []
            }
        }
    }
</script>