# Database UML

Bu diyagram okul ders programi sisteminin SQLite tablo yapisini gosterir.

```mermaid
classDiagram
    class Teacher {
        int id
        string name
        string branch
        int max_weekly_hours
    }

    class Lesson {
        int id
        string name
        int weekly_hours
        string level_group
    }

    class Classroom {
        int id
        int grade
        string section
        string name
    }

    class Schedule {
        int id
        int class_id
        int lesson_id
        int teacher_id
        int room_id
        string day
        int hour
    }

    class Room {
        int id
        string name
        string room_type
    }

    class TeacherUnavailability {
        int id
        int teacher_id
        string day
        int hour
    }

    class User {
        int id
        string name
        string role
    }

    Classroom "1" --> "0..*" Schedule : has
    Lesson "1" --> "0..*" Schedule : placed_as
    Teacher "1" --> "0..*" Schedule : teaches
    Room "1" --> "0..*" Schedule : used_in
    Teacher "1" --> "0..*" TeacherUnavailability : unavailable
```

## Kurallar

- `classes.name` benzersizdir. Ornek: `5-A`.
- `lessons.name` benzersizdir. Ornek: `Matematik`.
- `schedules.class_id + day + hour` benzersizdir; bir sinif ayni anda iki ders alamaz.
- `schedules.teacher_id + day + hour` benzersizdir; bir ogretmen ayni anda iki sinifa giremez.
- `rooms` derslik/laboratuvar/spor salonu gibi fiziksel alanlari tutar.
- `teacher_unavailability` ogretmenin uygun olmadigi gun ve saatleri tutar.
- `users` basit rol bilgisini tutar. Ornek roller: `Admin`, `Ogretmen`.
- `schedules` tablosu `classes`, `lessons`, `teachers` ve `rooms` tablolarina foreign key ile baglidir.
