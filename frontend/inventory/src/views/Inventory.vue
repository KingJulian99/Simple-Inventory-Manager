<template>
    
    <div class="appear w-full h-full flex flex-col justify-start items-center">
        <div class="w-full h-24">
            <FilterSection :categories="categories.map(category => category.name)" :suppliers="suppliers" :filters="filters"/>
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
                suppliers: [
                    'Sony',
                    'AMD',
                    'Communica',
                    'DIYElectronics',
                    'Nintendo'
                ],
                filters: [
                    {
                        type: 'category',
                        objectId: 0,
                        text: 'Consoles'
                    }
                ]
            }
        },
        created() {
            this.loadData();
            console.log(this.$route.path);
        },
        methods: {
            loadData() {
                this.getCategories();
            },
            async getCategories() {
                const response = await axios.get('/categories/get');
                this.categories = response.data.objects;
            }
        }
    }
</script>