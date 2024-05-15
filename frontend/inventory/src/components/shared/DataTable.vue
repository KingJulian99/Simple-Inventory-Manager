<template>
    <table>
        <thead class="border-2 border-black">
            <tr v-if="columnDefinitions.length > 0">
                <th v-for="(column, index) in columnDefinitions" :key="index" class="border-2 border-black p-2 min-w-48">{{ column.header }}</th>
            </tr>
        </thead>
        <tbody>
            <tr @click="pushDetails(data.id)" v-for="(data, index) in tableData" :key="index" class="group hover:bg-stone-200 hover:cursor-pointer">
                <td v-for="(column, index) in columnDefinitions" class="border-2 border-black p-1 group-hover:p-2 transition-all duration-200">{{ data[column.field] }}</td>
            </tr>
        </tbody>
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
            }
        },
        methods: {
            pushDetails(objectId) {
                this.$router.push({ path: `${this.$route.fullPath + '/' + objectId}` });
            }
        }
    }
</script>