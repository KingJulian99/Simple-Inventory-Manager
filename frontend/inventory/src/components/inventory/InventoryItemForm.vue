<template>
    <div class="w-full flex flex-col justify-start items-start p-4 border-b-2 border-black">
        <div v-show="errors.length > 0" class="w-full mb-8">
            <ErrorContainer :errors="errors"/>
        </div>

        <form @submit.prevent="validateAndSubmit" class="w-full">
            <Dropdown ref="productDropdown" textSizeClass="text-base" paddingSizeClass="p-2" title="Product" class="z-10">
                <DropdownRow @click="selectProductOption(index)" v-for="(productOption, index) in productOptions" :key="index" :text="productOption.name" size="sm"/>
            </Dropdown>
            <div class="w-full flex flex-row justify-start items-start flex-wrap gap-2 mt-4">
                <Tag v-if="Object.keys(this.selectedProduct).length !== 0" @remove="removeProductOption" :text="selectedProduct.name" size="sm" class="mb-4"/>
            </div>

            <Dropdown ref="supplierDropdown" textSizeClass="text-base" paddingSizeClass="p-2" title="Supplier">
                <DropdownRow @click="selectSupplierOption(index)" v-for="(supplierOption, index) in supplierOptions" :key="index" :text="supplierOption.name" size="sm"/>
            </Dropdown>
            <div class="w-full flex flex-row justify-start items-start flex-wrap gap-2 mt-4">
                <Tag v-if="Object.keys(this.selectedSupplier).length !== 0" @remove="removeSupplierOption" :text="selectedSupplier.name" size="sm"/>
            </div>
            <br>

            <label for="price">Purchase Price:</label>
            <input type="number" ref="price" v-model="formData.purchase_price" min="0" step="0.01" class="border-2 border-black ml-4 p-1">
            <br><br>
            <label v-if="!isUpdate" for="quantity">Quantity:</label>
            <input v-if="!isUpdate" type="number" ref="quantity" v-model="formData.quantity" min="1" class="border-2 border-black ml-4 p-1">
            
            <div class="w-full flex flex-row justify-end items-center mt-4">
                <button type="submit" class="w-32 border-2 border-black hover:bg-stone-200 transition-all duration-200">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
    import ErrorContainer from '@/components/shared/ErrorContainer.vue';
    import Dropdown from '@/components/shared/Dropdown.vue';
    import DropdownRow from '@/components/shared/DropdownRow.vue';
    import Tag from '@/components/shared/Tag.vue';
    import axios from '@/axios';

    export default {
        name: 'InventoryItemForm',
        components: {
            ErrorContainer,
            Dropdown,
            DropdownRow,
            Tag
        },
        props: {
            name: {
                type: String,
                default: ''
            },
            purchase_price: {
                type: Number,
                default: 0
            },
            product: {
                type: Object,
                default: {}
            },
            supplier: {
                type: Object,
                default: {}
            },
            isUpdate: {
                type: Boolean,
                default: false
            }
        },
        data() {
            return {
                errors: [],
                formData: {
                    purchase_price: 0,
                    quantity: 1
                },
                productOptions: [],
                selectedProduct: {},
                supplierOptions: [],
                selectedSupplier: {}
            }
        },
        created() {
            this.loadData();
            this.formData.purchase_price = this.purchase_price;
            this.selectedProduct = JSON.parse(JSON.stringify(this.product));
            this.selectedSupplier = JSON.parse(JSON.stringify(this.supplier));
        },
        methods: {
            async loadData() {
                const product_response = await axios.get('/products');
                this.productOptions = product_response.data.objects;

                const supplier_response = await axios.get('/suppliers');
                this.supplierOptions = supplier_response.data.objects;
            },
            selectProductOption(index) {
                if (Object.keys(this.selectedProduct).length === 0) {
                    this.selectedProduct = this.productOptions[index];
                }

                this.$refs['productDropdown'].toggle();
            },
            removeProductOption() {
                this.selectedProduct = {};
            },
            selectSupplierOption(index) {
                if (Object.keys(this.selectedSupplier).length === 0) {
                    this.selectedSupplier = this.supplierOptions[index];
                }

                this.$refs['supplierDropdown'].toggle();
            },
            removeSupplierOption() {
                this.selectedSupplier = {};
            },
            validateAndSubmit() {
                if (this.validate()) {
                    this.submit();
                }
            },
            validate() {
                this.errors = [];

                if (Object.keys(this.selectedProduct).length === 0) {
                    this.errors.push('You need to select a product');
                }

                if (Object.keys(this.selectedSupplier).length === 0) {
                    this.errors.push('You need to select a supplier');
                }

                return this.errors.length == 0;
            },
            async submit() {
                if (!this.isUpdate) {
                    try {
                        const selectedProductId = this.selectedProduct.id;
                        this.formData['product_id'] = selectedProductId;
                        const selectedSupplierId = this.selectedSupplier.id;
                        this.formData['supplier_id'] = selectedSupplierId;

                        const response = await axios.post('/inventory', this.formData);
                        this.$emit('created');

                    } catch (error) {
                        this.errors.push('Issue reaching backend');
                    }
                } else {
                    try {
                        const selectedProductId = this.selectedProduct.id;
                        this.formData['product_id'] = selectedProductId;
                        const selectedSupplierId = this.selectedSupplier.id;
                        this.formData['supplier_id'] = selectedSupplierId;
                        
                        const response = await axios.patch(`/inventory/${this.$route.params.id}`, this.formData);
                        this.$emit('updated');
                        
                    } catch (error) {
                        this.errors.push('Issue reaching backend');
                    }
                }
            }
        }
    }
</script>