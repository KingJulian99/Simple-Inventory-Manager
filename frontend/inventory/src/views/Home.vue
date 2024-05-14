<template>
    <div class="p-10 flex flex-col justify-center items-center">
        <div class="w-full z-10 mb-5">
            <div class="w-fit h-36">
                <Dropdown ref="mainMenu" textSizeClass="text-8xl" paddingSizeClass="p-10" :title="menuOptions[selectedMenuOptionIndex]">
                    <DropdownRow @click="swapMenuOption(index)" v-for="(menuOption, index) in menuOptions" :key="index" v-show="menuOption !== menuOptions[selectedMenuOptionIndex]" :text="menuOption" size="lg"/>
                </Dropdown>
            </div>
        </div>

        <!--Move each menu section to its own component eventually, with their own data moved in-->
        <div v-show="menuOptions[selectedMenuOptionIndex] === 'Inventory'" class="appear w-full h-full flex flex-col justify-start items-center">
            <div class="w-full h-24">
                <FilterSection :categories="categories.map(category => category.name)" :suppliers="suppliers" :filters="filters"/>
            </div>

        </div>
            
        <div v-show="menuOptions[selectedMenuOptionIndex] === 'Categories'" class="appear w-full h-full flex flex-row justify-start items-center">
            <div class="w-full h-full">
                <DataTable :columnDefinitions="categoryColumns" :tableData="categories"/>
            </div>
        
            <div class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
                <Dropdown textSizeClass="text-xl" paddingSizeClass="p-4" title="Create New Category">
                    <CategoryForm/>
                </Dropdown>
            </div>
        </div>

    </div>
    
    
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import DataTable from '@/components/shared/DataTable.vue';
    import FilterSection from '@/components/inventory/FilterSection.vue';
    import CategoryForm from '@/components/categories/CategoryForm.vue';

    export default {
        name: 'Home',
        components: {
            Dropdown,
            DropdownRow,
            FilterSection,
            CategoryForm,
            DataTable
        },
        data() {
            return {
                selectedMenuOptionIndex: 0,
                menuOptions: [
                    'Inventory',
                    'Products',
                    'Suppliers',
                    'Categories'
                ],
                categories: [
                    {
                        name: 'Consoles',
                        description: 'All gaming'
                    },
                    {
                        name: 'GPUs',
                        description: 'All gaming'
                    },
                    {
                        name: 'CPUs',
                        description: 'All gaming'
                    },
                    {
                        name: 'RAM',
                        description: 'All gaming'
                    }
                ],
                categoryColumns: [
                    {
                        header: 'Name',
                        field: 'name'
                    },
                    {
                        header: 'Description',
                        field: 'description'
                    },
                ],
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
        methods: {
            swapMenuOption(index) {
                this.selectedMenuOptionIndex = index;
                this.$refs['mainMenu'].toggle();
            }
        }
    }
</script>

<style scoped>
.appear {
    animation: appear 200ms ease-in forwards;
}

@keyframes appear {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 100;
    }
}
</style>