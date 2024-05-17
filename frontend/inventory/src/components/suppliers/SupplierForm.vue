<template>
    <div class="w-full flex flex-col justify-start items-start p-4 border-b-2 border-black">
        <div v-show="errors.length > 0" class="w-full mb-8">
            <ErrorContainer :errors="errors"/>
        </div>

        <form @submit.prevent="validateAndSubmit" class="w-full">
            <label for="name">Name:</label>
            <input type="text" ref="name" v-model="formData.name" class="border-2 border-black ml-4 p-1">
            <br><br>
            <label for="description">Description:</label>
            <textarea type="text" ref="description" v-model="formData.description" class="border-2 border-black ml-4 p-1"></textarea>
            <br><br>
            <label for="name">Email:</label>
            <input type="text" ref="email" v-model="formData.email" class="border-2 border-black ml-4 p-1">
            <br><br>
            <label for="name">Address:</label>
            <input type="text" ref="address" v-model="formData.address" class="border-2 border-black ml-4 p-1">
            <br><br>
            <label for="name">Contact Number:</label>
            <input type="tel" ref="number" v-model="formData.number" class="border-2 border-black ml-4 p-1">
            <br><br>
            <div class="w-full flex flex-row justify-end items-center">
                <button type="submit" class="w-32 border-2 border-black hover:bg-stone-200 transition-all duration-200">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
    import ErrorContainer from '@/components/shared/ErrorContainer.vue';
    import axios from '@/axios';

    export default {
        name: 'SupplierForm',
        components: {
            ErrorContainer
        },
        props: {
            name: {
                type: String,
                default: ''
            },
            description: {
                type: String,
                default: ''
            },
            email: {
                type: String,
                default: ''
            },
            address: {
                type: String,
                default: ''
            },
            number: {
                type: String,
                default: ''
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
                    name: '',
                    description: '',
                    email: '',
                    address: '',
                    number: null
                }
            }
        },
        created() {
            this.formData.name = this.name;
            this.formData.description = this.description;
            this.formData.email = this.email;
            this.formData.address = this.address;
            this.formData.number = this.number;
        },
        methods: {
            validateAndSubmit() {
                if (this.validate()) {
                    this.submit();
                }
            },
            validate() {
                this.errors = [];

                if (this.formData.name.trim() == '') {
                    this.errors.push('Name can\'t be empty');
                } else if (this.formData.name.trim().length > 36) {
                    this.errors.push('Name can\'t be over 36 characters');
                }

                if (this.formData.description.trim() == '') {
                    this.errors.push('Description can\'t be empty');
                } else if (this.formData.description.trim().length > 128) {
                    this.errors.push('Description can\'t be over 128 characters');
                }

                if (this.formData.email.trim() == '') {
                    this.errors.push('Email can\'t be empty');
                } else if (this.formData.email.trim().length > 128) {
                    this.errors.push('Email can\'t be over 128 characters');
                } else if (this.formData.email.indexOf('@') == -1) {
                    this.errors.push('Email needs to be valid (with an @ symbol)');
                }

                if (this.formData.address.trim() == '') {
                    this.errors.push('Address can\'t be empty');
                } else if (this.formData.address.trim().length > 128) {
                    this.errors.push('Address can\'t be over 128 characters');
                }

                if (!this.formData.number) {
                    this.errors.push('Contact number can\'t be empty');
                } else if (this.formData.number.length > 10) {
                    this.errors.push('Contact number can\'t be over 10 characters');
                }

                return this.errors.length == 0;
            },
            async submit() {
                if (!this.isUpdate) {
                    try {
                        const response = await axios.post('/suppliers', this.formData);
                        this.$emit('created');
                        console.log(response);
                    } catch (error) {
                        this.errors.push('Issue reaching backend');
                    }
                } else {
                    try {
                        const response = await axios.patch(`/suppliers/${this.$route.params.id}`, this.formData);
                        this.$emit('updated');
                        console.log(response);
                    } catch (error) {
                        this.errors.push('Issue reaching backend');
                    }
                }
                
            }
        }
    }
</script>