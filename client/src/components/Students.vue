<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Students</h1>
          <hr /><br /><br />
          <alert :message="message" v-if="showMessage"></alert>
          <button
            type="button"
            class="btn btn-success btn-sm"
            @click="toggleAddStudentModal"
          >
            Add Student
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">id</th>
                <th scope="col">Nom</th>
                <th scope="col">Age</th>
                <th scope="col">Action</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(student, id) in students" :key="id">
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.age }}</td>
                <!-- <td>
                  <span v-if="student.present">Yes</span>
                  <span v-else>No</span>
                </td> -->
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      @click="toggleEditStudentModal(student)"
                    >
                      Update
                    </button>
                    <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleDeleteStudent(student)">
                    Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  
      <!-- add new student modal -->
      <div
        ref="addStudentModal"
        class="modal fade"
        :class="{ show: activeAddStudentModal, 'd-block': activeAddStudentModal }"
        tabindex="-1"
        role="dialog"
      >
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-prenom">Add a new student</h5>
              <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
                @click="toggleAddStudentModal"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="mb-3">
                  <label for="addStudentPrenom" class="form-label">ID:</label>
                  <input
                    type="text"
                    class="form-control"
                    id="addStudentPrenom"
                    v-model="addStudentForm.id"
                    placeholder="Enter prenom"
                  />
                </div>
                <div class="mb-3">
                  <label for="addStudentName" class="form-label">NOM:</label>
                  <input
                    type="text"
                    class="form-control"
                    id="addStudentName"
                    v-model="addStudentForm.name"
                    placeholder="Enter name"
                  />
                </div>
                <div class="mb-3">
                  <label class="form-check-label" for="addStudentPresent">Age</label>
                  <input
                    type="text"
                    class="form-control"
                    id="addStudentName"
                    v-model="addStudentForm.age"
                    placeholder="Enter Age"
                  />
                </div>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-primary btn-sm"
                    @click="handleAddSubmit"
                  >
                    Submit
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleAddReset"
                  >
                    Reset
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div v-if="activeAddStudentModal" class="modal-backdrop fade show"></div>
    </div>
  
    <!-- edit student modal -->
    <div
      ref="editStudentModal"
      class="modal fade"
      :class="{ show: activeEditStudentModal, 'd-block': activeEditStudentModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-prenom">Update</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleEditStudentModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="editStudentPrenom" class="form-label">ID:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editStudentPrenom"
                  v-model="editStudentForm.id"
                  placeholder="Enter prenom"
                />
              </div>
              <div class="mb-3">
                <label for="editStudentName" class="form-label">Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editStudentName"
                  v-model="editStudentForm.name"
                  placeholder="Enter name"
                />
              </div>
              <div class="mb-3">
                <label for="editStudentName" class="form-label">Age:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editStudentName"
                  v-model="editStudentForm.age"
                  placeholder="Enter age"
                />
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleEditSubmit"
                >
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleEditCancel"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeEditStudentModal" class="modal-backdrop fade show"></div>
  </template>
  
  <script>
  import axios from 'axios';
  import Alert from './Alert.vue';
  
  export default {
    data() {
      return {
        activeAddStudentModal: false,
        addStudentForm: {
          id: '',
          name: '',
          age: '',
        },
        students: [],
        message: '',
        showMessage: false,
        activeEditStudentModal: false, // Corrected placement
        editStudentForm: {
          id: '',
          name: '',
          age: '',
        },
      };
    },
  
    components: {
      alert: Alert,
    },
  
    methods: {
      addStudent(payload) {
        const path = 'http://app.info/students';
        axios.post(path, payload)
          .then(() => {
            this.getStudents();
            this.message = 'Student added!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getStudents();
          });
      },
      getStudents() {
        const path = 'http://app.info/students';
        axios.get(path)
          .then((res) => {
            this.students = res.data.students;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      handleAddReset() {
        this.initForm();
      },
      handleAddSubmit() {
        this.toggleAddStudentModal();
        // let present = false;
        // if (this.addStudentForm.present[0]) {
        //   present = true;
        // }
        const payload = {
          id: this.addStudentForm.id,
          name: this.addStudentForm.name,
          age: this.addStudentForm.age,
          //present, // property shorthand
        };
        this.addStudent(payload);
        this.initForm();
      },
      initForm() {
        // this.addStudentForm.prenom = '';
        this.addStudentForm.name = '';
        // this.addStudentForm.present = [];
        this.editStudentForm.id = '';
        this.editStudentForm.age = '';
        // this.editStudentForm.prenom = ''; // Corrected property assignment
        this.editStudentForm.name = ''; // Corrected property assignment
        // this.editStudentForm.present = []; // Corrected property assignment
        this.editStudentForm.age = '';
      },
      toggleAddStudentModal() {
        const body = document.querySelector('body');
        this.activeAddStudentModal = !this.activeAddStudentModal;
        if (this.activeAddStudentModal) {
          body.classList.add('modal-open');
        } else {
          body.classList.remove('modal-open');
        }
      },
      toggleEditStudentModal(student) {
        if (student) {
          this.editStudentForm = student;
        }
        const body = document.querySelector('body');
        this.activeEditStudentModal = !this.activeEditStudentModal;
        if (this.activeEditStudentModal) {
          body.classList.add('modal-open');
        } else {
          body.classList.remove('modal-open');
        }
      },
      handleEditSubmit() {
        this.toggleEditStudentModal(null);
        // const present = this.editStudentForm.present;
        const payload = {
            id: this.editStudentForm.id,
            name: this.editStudentForm.name,
            age: this.editStudentForm.age,
            // present: present,
        };
        this.updateStudent(payload, this.editStudentForm.id);
    },

    updateStudent(payload, studentID) {
      const path = `http://app.info/students/${studentID}`;
      axios.put(path, payload)
        .then(() => {
          this.getStudents();
          this.message = 'Student updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getStudents();
        });
    },


      handleDeleteStudent(student) {
        this.removeStudent(student.id);
      },
      removeStudent(studentID) {
      const path = `http://app.info/students/${studentID}`;
      axios.delete(path)
          .then(() => {
          this.getStudents();
          this.message = 'Student removed!';
          this.showMessage = true;
          })
          .catch((error) => {
          console.error(error);
          this.getStudents();
          });
      },

      handleEditCancel() {
        this.toggleEditStudentModal(null);
        this.initForm();
      },
    },
  
    created() {
      this.getStudents();
    },
  };
  </script>
  