<template>
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
          <h1>Absences</h1>
          <hr /><br /><br />
          <alert :message="message" v-if="showMessage"></alert>
          <button
            type="button"
            class="btn btn-success btn-sm"
            @click="toggleAddStudentModal"
          >
            Add Absence
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">date</th>
                <th scope="col">id</th>
                <th scope="col">reason</th>
                <th scope="col">student_id</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(absence, id) in absences" :key="id">
                <td>{{ absence.date }}</td>
                <td>{{ absence.id }}</td>
                <td>{{ absence.reason }}</td>
                <td>{{ absence.student_id }}</td>
                <!-- <td>
                  <span v-if="student.present">Yes</span>
                  <span v-else>No</span>
                </td> -->
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      @click="toggleEditStudentModal(absence)"
                    >
                      Update
                    </button>
                    <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleDeleteStudent(absence)">
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
              <h5 class="modal-prenom">Add a new absence</h5>
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
                  <label for="addStudentPrenom" class="form-label">DATE:</label>
                  <input
                    type="date"
                    class="form-control"
                    id="addStudentPrenom"
                    v-model="addStudentForm.date"
                    placeholder="Enter date"
                  />
                </div>
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
                  <label for="addStudentName" class="form-label">reason:</label>
                  <input
                    type="text-area"
                    class="form-control"
                    id="addStudentName"
                    v-model="addStudentForm.reason"
                    placeholder="Enter reason"
                  />
                </div>
                <div class="mb-3">
                  <label class="form-check-label" for="addStudentPresent">student_id</label>
                  <input
                    type="text"
                    class="form-control"
                    id="addStudentName"
                    v-model="addStudentForm.student_id"
                    placeholder="Enter student_id"
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
                    <label for="editStudentPrenom" class="form-label">Date:</label>
                    <input
                    type="date"
                    class="form-control"
                    id="editStudentPrenom"
                    v-model="editStudentForm.date"
                    placeholder="Enter date"
                    />
                </div>
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
                <label for="editStudentName" class="form-label">reason:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editStudentName"
                  v-model="editStudentForm.reason"
                  placeholder="Enter reason"
                />
              </div>
              <div class="mb-3">
                <label for="editStudentName" class="form-label">student_id:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editStudentName"
                  v-model="editStudentForm.student_id"
                  placeholder="Enter student_id"
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
          date: '',
          id: '',
          reason: '',
          student_id: '',
        },
        absences: [],
        message: '',
        showMessage: false,
        activeEditStudentModal: false, // Corrected placement
        editStudentForm: {
          date: '',
          id: '',
          reason: '',
          student_id: '',
        },
      };
    },
  
    components: {
      alert: Alert,
    },
  
    methods: {
      addStudent(payload) {
        const path = 'http://service.info/absences';
        axios.post(path, payload)
          .then(() => {
            this.getStudents();
            this.message = 'Absence added!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getStudents();
          });
      },
      getStudents() {
        const path = 'http://service.info/absences';
        axios.get(path)
          .then((res) => {
            this.absences = res.data.absences;
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
          date: this.addStudentForm.date,
          id: this.addStudentForm.id,
          reason: this.addStudentForm.reason,
          student_id: this.addStudentForm.student_id,
          //present, // property shorthand
        };
        this.addStudent(payload);
        this.initForm();
      },
      initForm() {
        this.addStudentForm.date = '';
        this.addStudentForm.id = '';
        this.addStudentForm.reason = '';
        this.editStudentForm.student_id = '';
        
        this.editStudentForm.date = '';
        this.editStudentForm.id = ''; // Corrected property assignment
        this.editStudentForm.reason = '';
        this.editStudentForm.student_id = '';
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
      toggleEditStudentModal(absence) {
        if (student) {
          this.editStudentForm = absence;
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
            date: this.editStudentForm.date,
            id: this.editStudentForm.id,
            reason: this.editStudentForm.reason,
            student_id: this.editStudentForm.student_id,
        };
        this.updateStudent(payload, this.editStudentForm.id);
    },

      updateStudent(payload, absenceID) {
        const path = `http://service.info/absences/${absenceID}`;
        axios.put(path, payload)
          .then(() => {
            this.getStudents();
            this.message = 'Absence updated!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getStudents();
          });
      },


      handleDeleteStudent(absence) {
        this.removeStudent(absence.id);
        },
        removeStudent(absenceID) {
        const path = `http://service.info/absences/${absenceID}`;
        axios.delete(path)
            .then(() => {
            this.getStudents();
            this.message = 'Absence removed!';
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
  