<template>
    
    <div class="appear w-full h-full flex flex-col justify-start items-center">
        <div class="w-full h-24 z-10">
            <FilterSection :categories="categories" :suppliers="suppliers" :categoryFilters="categoryFilters" :supplierFilters="supplierFilters" @addCategoryFilter="addCategoryFilter" @removeCategoryFilter="removeCategoryFilter" @addSupplierFilter="addSupplierFilter" @removeSupplierFilter="removeSupplierFilter"/>
        </div>

        <div class="w-full flex flex-row justify-around items-start gap-4">
            <div @click="unfilterOnProduct" v-if="isProductFiltered" class="w-14 h-14 shrink-0 flex flex-col justify-center items-center border-2 border-black hover:bg-stone-400 hover:cursor-pointer transition-all duration-200">
                <img src="/images/arrow.svg" class="black-filter w-2/3 rotate-180">
            </div>

            <div class="w-full h-full">
                <DataTable v-if="!isProductFiltered" ref="table" class="appear" :columnDefinitions="inventoryColumns" :tableData="rolledUpInventory" :emitOnRowClick="true" @rowClicked="filterOnProduct"/>
                <DataTable v-if="isProductFiltered" ref="table" class="appear-and-slot-in" :columnDefinitions="detailedInventoryColumns" :tableData="filteredInventory.map(item => ({
                                                                                                                                                                                        id: item.id,
                                                                                                                                                                                        product_id: item.product.id,
                                                                                                                                                                                        name: item.product.name,
                                                                                                                                                                                        description: item.product.description,
                                                                                                                                                                                        categories: this.generateCategoryStringFromInventoryItem(item),
                                                                                                                                                                                        suppliers: item.supplier.name,
                                                                                                                                                                                        purchase_price: item.purchase_price
                                                                                                                                                                                    }))"/>
            </div>
        
            <div v-show="!isProductFiltered" class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
                <Dropdown ref="formDropdown" textSizeClass="text-xl" paddingSizeClass="p-4" title="Create New Inventory Item">
                    <InventoryItemForm @created="reloadData"/>
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
    import InventoryItemForm from '@/components/inventory/InventoryItemForm.vue';
    import axios from '@/axios';

    export default {
        name: 'Inventory',
        components: {
            Dropdown,
            DropdownRow,
            FilterSection,
            InventoryItemForm,
            DataTable
        },
        data() {
            return {
                categories: [],
                suppliers: [],
                categoryFilters: [],
                supplierFilters: [],
                inventoryColumns: [
                    {
                        header: 'Quantity',
                        field: 'quantity'
                    },
                    {
                        header: 'Product Name',
                        field: 'name'
                    },
                    {
                        header: 'Product Description',
                        field: 'description'
                    },
                    {
                        header: 'Product Categories',
                        field: 'categories'
                    },
                ],
                detailedInventoryColumns: [
                    {
                        header: 'Product Name',
                        field: 'name'
                    },
                    {
                        header: 'Supplier',
                        field: 'suppliers'
                    },
                    {
                        header: 'Purchase Price',
                        field: 'purchase_price'
                    },
                ],
                inventory: [],
                filteredInventory: [],
                rolledUpInventory: [], // The same as filtered inventory, but rolled up by the product Id. Each key is a productID.
                isProductFiltered: false,
                selectedProductFilterId: -1
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
                this.rolledUpInventory = [];
                this.getCategories();
                this.getSuppliers();
                this.getInventory();
            },
            async getCategories() {
                const response = await axios.get('/categories');
                this.categories = response.data.objects;
            },
            async getSuppliers() {
                const response = await axios.get('/suppliers');
                this.suppliers = response.data.objects;
            },
            async getInventory() {
                const response = await axios.get('/inventory');
                this.inventory = response.data.objects;
                this.filteredInventory = this.inventory.slice();
                this.generateRolledUpInventory();
            },
            generateCategoryStringFromInventoryItem(item) {
                let categories = '';

                for (let j = 0; j < item.product.categories.length; j++) {
                    categories = categories + item.product.categories[j].name;

                    if (j != item.product.categories.length - 1) {
                        categories = categories + ', ';
                    }
                }

                return categories;
            },
            generateRolledUpInventory() {
                this.rolledUpInventory = [];
                for (let i = 0; i < this.filteredInventory.length; i++) {
                    let index = this.rolledUpInventory.findIndex(obj => obj.id === this.filteredInventory[i].product.id);

                    if (index !== -1) {
                        this.rolledUpInventory[index].quantity++;
                    } else {
                        let categories = this.generateCategoryStringFromInventoryItem(this.filteredInventory[i]);

                        this.rolledUpInventory.push( {
                            id: this.filteredInventory[i].product.id,
                            quantity: 1,
                            name: this.filteredInventory[i].product.name,
                            description: this.filteredInventory[i].product.description,
                            categories: categories
                        } )
                    }
                }
            },
            filterInventory() {
                this.filteredInventory = this.inventory.slice();

                // Filter on product if required
                if (this.isProductFiltered) {
                    this.filteredInventory = this.filteredInventory.filter(item => item.product.id == this.selectedProductFilterId);
                }

                // Filter by category
                if (this.categoryFilters.length > 0) {
                    let filterCategoryIds = this.categoryFilters.map(filterCategory => filterCategory.id);

                    this.filteredInventory = this.filteredInventory.filter(item => {
                        let presentCategoryIds = item.product.categories.map(presentCategory => presentCategory.id);
                        return presentCategoryIds.some(element => filterCategoryIds.includes(element));
                    });
                }

                // Filter by supplier
                if (this.supplierFilters.length > 0) {
                    let filterSupplierIds = this.supplierFilters.map(supplierFilter => supplierFilter.id);

                    this.filteredInventory = this.filteredInventory.filter(item => filterSupplierIds.includes(item.supplier.id));
                }

                this.generateRolledUpInventory();
            },
            addCategoryFilter(category) {
                const exists = this.categoryFilters.some(item => item.id === category.id);

                if (!exists) {
                    this.categoryFilters.push(category);
                }

                this.filterInventory();
            },
            removeCategoryFilter(category) {
                this.categoryFilters = this.categoryFilters.filter(item => item.id != category.id);
                this.filterInventory();
            },
            addSupplierFilter(supplier) {
                const exists = this.supplierFilters.some(item => item.id === supplier.id);

                if (!exists) {
                    this.supplierFilters.push(supplier);
                }

                this.filterInventory();
            },
            removeSupplierFilter(supplier) {
                this.supplierFilters = this.supplierFilters.filter(item => item.id != supplier.id);
                this.filterInventory();
            },
            filterOnProduct(product_id) {
                this.selectedProductFilterId = product_id;
                this.isProductFiltered = true;
                this.filterInventory();
            },
            unfilterOnProduct() {
                this.isProductFiltered = false;
                this.selectedProductFilterId = -1;
                this.filterInventory();
            }
        }
    }
</script>