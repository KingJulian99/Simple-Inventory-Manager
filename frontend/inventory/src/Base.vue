<template>
    <div class="p-10 flex flex-col justify-center items-center">
        <div class="w-full z-10 mb-8 flex flex-row justify-start items-center">
            <div class="w-fit h-36">
                <Dropdown ref="mainMenu" textSizeClass="text-8xl" paddingSizeClass="p-10" :title="menuOptions[selectedMenuOptionIndex]">
                    <DropdownRow @click="swapMenuOption(index)" v-for="(menuOption, index) in menuOptions" :key="index" v-show="menuOption !== menuOptions[selectedMenuOptionIndex]" :text="menuOption" size="lg"/>
                </Dropdown>
            </div>
            <div @click="goBack" v-show="isBackButtonVisible" class="appear text-8xl font-extralight flex flex-row justify-start items-center ml-10 gap-4">
                <div class="w-24 h-24 flex flex-col justify-center items-center hover:cursor-pointer hover:bg-stone-400 transition-all duration-200">
                    <img src="/images/arrow.svg" class="w-2/3 rotate-180 black-filter">
                </div>
                <div class="h-full flex flex-col justify-center items-start">
                    <h1>/ Details</h1>
                </div>
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
                isBackButtonVisible: false,
                backButtonPathName: ''
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
                let path = urlPath.split('/');

                if (path.length - 1 > 1) {
                    this.isBackButtonVisible = true;
                    this.backButtonPathName = path[1];
                } else {
                    this.isBackButtonVisible = false;
                }
            },
            goBack() {
                this.$router.push({ name: this.backButtonPathName });
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

.appear-and-slot-in {
    animation: appear-and-slot-in 200ms ease-in forwards;
}

@keyframes appear-and-slot-in {
    0% {
        opacity: 0;
        transform: translateX(30px);
    }
    100% {
        opacity: 100;
        transform: translateX(0);
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

.black-filter {
    filter: invert(100%) grayscale(100%);
}
</style>