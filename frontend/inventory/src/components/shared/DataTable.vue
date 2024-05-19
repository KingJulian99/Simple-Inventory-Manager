<template>
    <table ref="table">
        <thead class="border-2 border-black">
            <tr v-if="columnDefinitions.length > 0">
                <th v-for="(column, index) in columnDefinitions" :key="index" class="border-2 border-black p-2 min-w-48">{{ column.header }}</th>
            </tr>
        </thead>
        <tbody>
            <tr @click="handleRowClick(data.id)" v-for="(data, index) in tableData" :key="index" class="group appear hover:bg-stone-200 hover:cursor-pointer">
                <td v-for="(column, index) in columnDefinitions" class="border-2 border-black p-1 px-2 group-hover:p-2 transition-all duration-200">{{ data[column.field] }}</td>
            </tr>
        </tbody>
        
        <div v-if="tableData.length == 0"  class="appear w-full bg-red flex flex-row justify-center items-center mt-4">
            <p class="p-2 border-2 border-black border-dotted">Nothing to show.</p>
        </div>
    </table>
</template>

<script>
    export default {
        name: 'DataTable',
        props: {
            title: {
                type: String,
                default: ''
            },
            columnDefinitions: {
                type: Array,
                default: [] // Holds objects, each with a header and field
            },
            tableData: {
                type: Array,
                default: [] // Holds objects, each with all fields specified in columnDefinitions
            },
            emitOnRowClick: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            handleRowClick(id) {
                if (this.emitOnRowClick) {
                    this.$emit('rowClicked', id);
                } else {
                    this.pushDetails(id);
                }
            },
            pushDetails(objectId) {
                this.$router.push({ path: `${this.$route.fullPath + '/' + objectId}` });
            },
            flashGreen() {
                this.$refs['table'].classList.add('flash-green');
                setTimeout(() => {
                    this.$refs['table'].classList.remove('flash-green');
                }, 500);
            }
        }
    }
</script>