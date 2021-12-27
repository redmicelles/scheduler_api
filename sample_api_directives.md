#View Users
query {
  users {
    edges {
      node {
        username,
        archived,
        verified,
        email,
        secondaryEmail,
      }
    }
  }
}

#Register a User
mutation {
  register(
    email: "new_user@email.com",
    username: "new_user",
    password1: "123456",
    password2: "123456",
  ) {
    success,
    errors,
    token,
    refreshToken
  }
}

#Create a Schedule
mutation{
createSchedule(scheduleData:{startDate:"2021-12-27", startTime:"08:30:00", duration: 45}){
  schedule{
    id
    startDateTime
    endDateTime
  }
}
}

#Update a Schedule
mutation {
  updateSchedule(scheduleData: {id: 1, startDate: "2021-12-27", startTime: "10:30:00", duration: 45}) {
    schedule {
      startDateTime
      endDateTime
    }
  }
}


#View my schedules and thier reservations
query{
  mySchedules{
    id
    startDate
    startTime
    endDate
    endTime
    reservation{
      id
      email
      fullname
    }
  }
}

#View a user's schedules
query{
  userSchedules(userId: 1){
    id
    startDateTime
    endDateTime
    user{
      id
      username
      email
    }
  }
}

#create a reservation
mutation{
createReservation(reservationData:{fullname: "Victor John", email: "victor@gmail.com", schedule:"2"}){
  reservation{
    id
    fullname
    email
    schedule{
      id
      startDateTime
      endDateTime
      user{
        id
        username
        email
      }
    }
  }
}
}
