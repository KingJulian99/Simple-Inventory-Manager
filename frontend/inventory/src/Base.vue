<template>
    <div class="p-10 flex flex-col justify-center items-center">
        <div class="w-full z-10 mb-5">
            <div class="w-fit h-36">
                <Dropdown ref="mainMenu" textSizeClass="text-8xl" paddingSizeClass="p-10" :title="menuOptions[selectedMenuOptionIndex]">
                    <DropdownRow @click="swapMenuOption(index)" v-for="(menuOption, index) in menuOptions" :key="index" v-show="menuOption !== menuOptions[selectedMenuOptionIndex]" :text="menuOption" size="lg"/>
                </Dropdown>
            </div>
        </div>

        <div class="w-full flex flex-row justify-start items-start">
            <router-view></router-view>
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
        name: 'Base',
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
            }
        },
        methods: {
            setSelectedMenuOptionToURL(urlPath) {
                let firstBit = urlPath.trim().split('/')[1];
                for (let i = 0; i < this.menuOptions.length; i++) {
                    if (this.menuOptions[i].toLowerCase() == firstBit) {
                        this.selectedMenuOptionIndex = i;
                    }
                }
            },
            conditionallyAddBackButton(urlPath) {
                // Add this when on a deeper URL path.
            },
            swapMenuOption(index) {
                this.selectedMenuOptionIndex = index;
                this.$refs['mainMenu'].toggle();
                this.$router.push({ name: this.menuOptions[index].toLowerCase() });
            }
        },
        watch: {
            '$route'(to, from) {
                this.setSelectedMenuOptionToURL(to.path);
                this.conditionallyAddBackButton(to.path);
            }
        }
    }
</script>

<style>
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

.flash-green {
    animation: flash-green 500ms ease-in forwards;
}

@keyframes flash-green {
    0% {
       background-color: transparent; 
    }
    50% {
        background-color: green;
    }
    100% {
        background-color: transparent; 
    }
}
</style>