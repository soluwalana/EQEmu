"""Task windows. Every offer on the window is accepted and its steps are queued.

A short offer stays in the book and is not taken.
"""

# from eqclient4.action import Action
# from eqclient4.actions.read_tasks import ReadTasks
from eqclient4.handler import Handler
from eqclient4.log import log
from eqclient4.structs import (
    EQStruct,
    OP_TaskActivity,
    OP_TaskActivityComplete,
    OP_TaskDescription,
    OP_TaskSelectWindow,
)


class TasksHandler(Handler):
    opcodes = (
        "OP_TaskSelectWindow",
        "OP_TaskActivity",
        "OP_TaskActivityComplete",
        "OP_TaskDescription",
    )

    def on(self, opcode: str, payload: EQStruct) -> None:
        match payload:
            case OP_TaskSelectWindow():
                log.info(f"Received Task Select Window - {payload}")

            case OP_TaskDescription():
                self.description(payload)
            case OP_TaskActivity():
                self.activity(payload)
            case OP_TaskActivityComplete():
                self.complete(payload)
            case _:
                log.error("Unknown task opcode: %s", payload)

    def description(self, data: OP_TaskDescription) -> None:
        log.info(f"Setting task description {data.task_id} {data.title}")
        self.world.tasks.tasks[data.task_id] = data
        # action: Action = ReadTasks(data.task_id)
        # self.loop.enqueue_once(action, source=f"task:{data.task_id}")
        log.error(f"Need to implement ReadTasks(data.task_id) {data.task_id}")

    def activity(self, data: OP_TaskActivity) -> None:
        log.info(f"Setting task activity {data.task_id} {data.activity_id} - {data.description} - {data.done} / {data.goal}")
        activity_map = self.world.tasks.activities[data.task_id]
        activity_map[data.activity_id] = data

    def complete(self, data: OP_TaskActivityComplete) -> None:
        activity_map = self.world.tasks.activities[data.task_id]
        activity = activity_map[data.activity_id]
        if data.task_completed:
            activity.done = activity.goal

    # def window_v0(self, row: OP_TaskSelectWindow) -> None:
    #     book = self.book()
    #     stored = []
    #     accepted: set[int] = set()
    #     giver = int(row.giver or 0)
    #     for task in row.tasks:
    #         if task.title and not book.title:
    #             book.title = task.title
    #         if task.description and not book.description:
    #             book.description = task.description
    #         locked = task.duration_code == SHORT
    #         for element in task.elements:
    #             activity = Activity(
    #                 task.task_id,
    #                 element.activity_id,
    #                 element.kind,
    #                 element.target,
    #                 element.item_list,
    #                 element.description or task.description,
    #                 element.goal,
    #                 locked=locked,
    #             )
    #             activity.zone_id = element.zone_id
    #             _put(book, activity)
    #             if not locked:
    #                 stored.append((activity, giver))
    #         if locked or int(task.task_id) in accepted:
    #             continue
    #         self.loop.send(
    #             "OP_AcceptNewTask",
    #             OP_AcceptNewTask(int(task.task_id), giver, row.task_type).serialize(),
    #         )
    #         accepted.add(int(task.task_id))
    #     for activity, _master in stored:
    #         if not _is_step(activity):
    #             continue
    #         self.append_step(activity)


#     def activity_v0(self, row: OP_TaskActivity) -> None:
#         book = self.book()
#         if row.locked:
#             current = _find(book, row.task_id, row.activity_id)
#             if current and current.target_name and (not current.locked):
#                 return
#             if not current:
#                 _put(
#                     book,
#                     Activity(row.task_id, row.activity_id, 0, "", "", "", 1, locked=True),
#                 )
#             else:
#                 current.locked = True
#             return
#         activity = Activity(
#             row.task_id,
#             row.activity_id,
#             row.kind,
#             row.target,
#             row.item_list,
#             row.description,
#             row.goal,
#             row.done,
#             locked=False,
#         )
#         activity.optional = bool(row.optional)
#         activity.zone_id = row.zone_id
#         _put(book, activity)
#         if activity.finished:
#             log.info(
#                 "task %s:%s done optional=%s %s",
#                 activity.task_id,
#                 activity.activity_id,
#                 int(activity.optional),
#                 activity.description or activity.target_name,
#             )
#             _release(self.loop, activity.task_id, activity.activity_id)

#     def complete_v0(self, row: OP_TaskActivityComplete) -> None:
#         task_id, activity_id, stage_complete = (
#             row.task_id,
#             row.activity_id,
#             row.stage_complete,
#         )
#         if not stage_complete:
#             return
#         book = self.book()
#         activity = _find(book, task_id, activity_id)
#         if not activity:
#             activity = Activity(task_id, activity_id, 0, "", "", "", 1, done=1)
#             book.activities.append(activity)
#         activity.done = max(activity.done, activity.goal)
#         _release(self.loop, task_id, activity_id)

#     def append_step(self, activity: Activity) -> None:
#         world = self.world
#         source = f"task:{activity.task_id}:{activity.activity_id}"
#         description = activity.description or activity.target_name
#         action: Action
#         if activity.kind in (SPEAK, DELIVER):
#             npc = 0
#             mob = mob_named(world, activity.target_name)
#             if mob:
#                 npc = mob.id
#             line = "hail" if activity.kind == SPEAK else description
#             action = Talk(npc, line, description)
#             action.bind_name = activity.target_name or ""
#         elif activity.kind == KILL:
#             spawn_id = 0
#             mob = mob_named(world, activity.target_name)
#             if mob:
#                 spawn_id = mob.id
#             action = Kill(spawn_id or None, None if spawn_id else activity.target_name, None)
#         elif activity.kind in (LOOT, COLLECT):
#             action = Fetch(_first_id(activity.item_list), activity.goal, description)
#         else:
#             return
#         action.description = description
#         action.task_text = description
#         enqueue_once(self.loop, world, action, source)


# def _is_step(activity: Activity) -> bool:
#     if activity.locked or activity.finished:
#         return False
#     if activity.kind not in (SPEAK, KILL, LOOT, DELIVER, COLLECT):
#         return False
#     if activity.kind in (LOOT, COLLECT):
#         return bool(activity.item_list or activity.target_name or activity.description)
#     return bool(activity.target_name or activity.description)


# def _put(book: Book, activity: Activity) -> None:
#     current = _find(book, activity.task_id, activity.activity_id)
#     if not current:
#         book.activities.append(activity)
#         return
#     done = max(current.done, activity.done)
#     activity.done = done
#     if current.target_name and (not activity.target_name):
#         activity.target_name = current.target_name
#     index = book.activities.index(current)
#     book.activities[index] = activity


# def _release(loop: Loop, task_id: int, activity_id: int) -> None:
#     """The step is done. Drop the action that was still hunting or talking."""
#     source = f"task:{int(task_id)}:{int(activity_id)}"
#     for action in queue_of(loop):
#         if action.source == source:
#             action.complete = True


# def _find(book: Book, task_id: int, activity_id: int) -> Activity | None:
#     for activity in book.activities:
#         if activity.task_id == task_id and activity.activity_id == activity_id:
#             return activity
#     return None


# def _first_id(item_list: str) -> int:
#     match = re.search("\\d+", item_list or "")
#     return int(match.group(0)) if match else 0
