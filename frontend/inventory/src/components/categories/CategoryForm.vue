<template>
    <div class="w-full flex flex-col justify-start items-start p-4 border-b-2 border-black">
        <div v-show="errors.length > 0" class="w-full mb-8">
            <ErrorContainer :errors="errors"/>
        </div>

        <form @submit.prevent="validateAndSubmit" class="w-full">
            <label for="name">Name:</label>
            <input type="text" ref="name" v-model="formData.name" class="border-2 border-black ml-4 p-1"><br><br>
            <label for="description">Description:</label>
            <textarea type="text" ref="description" v-model="formData.description" class="border-2 border-black ml-4 p-1"></textarea>
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
        name: 'CategoryForm',
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
                    description: ''
                }
            }
        },
        created() {
            this.formData.name = this.name;
            this.formData.description = this.description;
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

                return this.errors.length == 0;
            },
            async submit() {
                if (!this.isUpdate) {
                    try {
                        const response = await axios.post('/categories', this.formData);
                        this.$emit('created');
                        console.log(response);
                    } catch (error) {
                        this.errors.push('Issue reaching backend');
                    }
                } else {
                    try {
                        const response = await axios.patch(`/categories/${this.$route.params.id}`, this.formData);
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