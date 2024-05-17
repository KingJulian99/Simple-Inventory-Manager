<template>
    <div class="appear w-full h-full flex flex-row justify-start items-start">
        <div class="w-full h-full">
            <DataTable ref="table" :columnDefinitions="supplierColumns" :tableData="suppliers"/>
        </div>
    
        <div class="w-96 shrink-0 h-20 flex flex-row justify-center items-center">
            <Dropdown ref="formDropdown" textSizeClass="text-xl" paddingSizeClass="p-4" title="Create New Supplier">
                <SupplierForm @created="reloadData"/>
            </Dropdown>
        </div>
    </div>
</template>

<script>
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import DataTable from '@/components/shared/DataTable.vue';
    import FilterSection from '@/components/inventory/FilterSection.vue';
    import SupplierForm from '@/components/suppliers/SupplierForm.vue';
    import axios from '@/axios';

    export default {
        name: 'Suppliers',
        components: {
            Dropdown,
            DropdownRow,
            FilterSection,
            SupplierForm,
            DataTable
        },
        data() {
            return {
                suppliers: [],
                supplierColumns: [
                    {
                        header: 'Name',
                        field: 'name'
                    },
                    {
                        header: 'Description',
                        field: 'description'
                    },
                    {
                        header: 'Email',
                        field: 'email'
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
                this.getSuppliers();
            },
            async getSuppliers() {
                const response = await axios.get('/suppliers');
                console.log(response);
                this.suppliers = response.data.objects;
            }
        }
    }

</script>