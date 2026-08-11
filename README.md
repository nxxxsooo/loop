<p align="right"><a href="./README.en.md">English</a></p>

<h1 align="center">loop</h1>

<p align="center"><strong>一次触发，三个深循环，交付可验证结果。</strong></p>

<p align="center">
  <a href="#安装"><img src="https://img.shields.io/badge/安装-skills.sh-111820?style=flat-square" alt="通过 skills.sh 安装"></a>
  <a href="https://github.com/nxxxsooo/loop/releases"><img src="https://img.shields.io/github/v/release/nxxxsooo/loop?style=flat-square&color=5eead4" alt="最新版本"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/许可证-MIT-5eead4?style=flat-square" alt="MIT 许可证"></a>
</p>

`loop` 是唯一的常规入口。只需调用一次，它就会按产物就绪状态持续推进当前产品任务，不再要求你手动指定下一个 Skill。

```text
想法 -> deep-grill -> Product Brief
     -> deep-design -> Build Contract
     -> deep-build -> 已验证结果
```

## 安装

推荐使用引导安装。依次安装完整 loop bundle 和 `deep-design` 使用的 `design-taste-frontend`；两次选择相同的 Agent、Project／Global 和 Symlink／Copy：

```bash
npx skills@latest add nxxxsooo/loop --skill '*'
npx skills@latest add Leonxlnx/taste-skill --skill design-taste-frontend
```

需要直接完成全局安装时：

```bash
npx skills@latest add nxxxsooo/loop -g -y
npx skills@latest add Leonxlnx/taste-skill --skill design-taste-frontend -g -y
```

快速安装会跳过提示，并按 `skills` CLI 的 Agent 检测结果全局安装完整 bundle 与 Taste Skill。

开始任务时说：

> 使用 $loop 把这个想法推进到设计和实现。

后续普通回复会继续当前子循环。你也可以单独调用任意 `deep-*` Skill；直接调用不会自动开启持久 `loop`。

## 从 grill-loop v2 迁移

仓库已从 `nxxxsooo/grill-loop` 更名为 `nxxxsooo/loop`。GitHub 会重定向旧仓库 URL，但已安装快照仍保留旧 Skill 名。先删除一次，再安装 v3：

```bash
npx skills@latest remove grill-loop grilling -g -y
```

然后使用上面任一安装方式。

| Skill | 负责内容 | 就绪条件 |
|---|---|---|
| `loop` | 会话持续、产物迁移和 `?` | 用户要求的终点完成 |
| `deep-grill` | 想法澄清和对抗性审查 | Product Brief 或审查结论确认 |
| `deep-design` | 产品规格与实现设计 | Build Contract 确认 |
| `deep-build` | 实现、验证和授权范围内的交付 | 必过场景成功 |

## `?` 表示解释并续接

在活跃 loop 中，只发送：

```text
?
```

`loop` 会冻结当前动作，重新说明最后确认点、当前子循环和产物、发生的变化、重要性，以及原本准备执行的下一步，但不会结束当前 loop。

解释后，Codex 会先检查当前模式的工具元数据。若 `request_user_input` 可调用，会立即显示本地化原生问题界面，让你继续、调整下一步或停止；当前模式不可调用时，会自动改用同语言的一句续接提示，不因模式切换而暂停。选择继续会立即恢复原本下一步，不必重新点名任何 Skill。

## 原生问题工具

`deep-grill` 和 `deep-design` 会用当前客户端的原生问题界面处理归用户所有的决定。在 Codex 中，该界面是 `request_user_input`，当前仅在 Plan mode 可调用；其他模式不能靠 Skill 文案强制触发。工具受模式限制时，子循环会保留待决问题，请你切换模式，然后等待。只有客户端没有原生问题界面，或者你明确选择文字方式时，才使用文字问题。

## 规格与设计

`deep-design` 负责完整的规格和设计过程。小型工作可以把 Build Contract 放在当前任务或原生计划中。耐久、多会话、跨组件或高后果变更，会使用项目的官方 OpenSpec 工作流作为实体 Build Contract。若存在该契约，`deep-build` 使用官方流程实施。

领域、架构、前端、测试和交付等专家能力由当前子循环按需调用，用户无需管理内部路由。

其中，落地页、作品集、编辑型页面或视觉改版出现实质视觉设计问题时，`deep-design` 会在可用时默认加载 `design-taste-frontend`；仪表盘、数据表和多步骤产品界面不走该 Skill。

## 完整 loop 契约

以下内容与 [`skills/loop/SKILL.md`](./skills/loop/SKILL.md) 保持完全一致：

<!-- loop-skill-body:start -->
> # Loop
>
> Own progression, not the child methods. Route the active product task through three artifact contracts:
>
> ```text
> deep-grill -> confirmed Product Brief
> deep-design -> confirmed Build Contract
> deep-build -> verified result
> ```
>
> ## Keep The Loop Active
>
> A fresh loop starts only when the user explicitly invokes `loop`. After that, treat every ordinary reply as a continuation of the same loop until the goal is achieved, the user stops, the user clearly changes tasks, or further work requires authority outside the original request. The user does not need to name `loop` or any child again.
>
> Resume the current child while its output contract is incomplete. When its artifact is confirmed, select the next child from artifact readiness without asking the user to nominate a skill or choose a route. State the transition briefly and continue in the same response when the next action is already authorized. Artifact readiness chooses the child; it does not expand the user's authority or the requested endpoint.
>
> ## Route By Artifact Readiness
>
> - Use `deep-grill` when no confirmed Product Brief exists, when root product intent is unresolved, or when the requested endpoint is an isolated adversarial audit. Discovery mode produces the Product Brief; audit mode may finish without advancing when an audit is the whole request.
> - Use `deep-design` when the Product Brief is confirmed but no confirmed Build Contract exists.
> - Use `deep-build` when the Build Contract is confirmed and implementation is authorized.
> - Resume the same child when its contract is incomplete, even after a mode switch, clarification, or ordinary user answer.
> - Return an invalidated artifact to the child that produces it. A root product contradiction returns to `deep-grill`; a material behavior, interface, task, or verification gap returns to `deep-design`.
> - Honor a direct invocation of a child skill. Direct use does not require `loop`, but it also does not activate the persistent loop unless the user explicitly starts one.
>
> The active child selects any domain, architecture, research, interface, visual-design, testing, deployment, or other specialist it needs. The user does not manage internal routing.
>
> ## Preserve One Source Of State
>
> Carry the goal, current child, confirmed artifacts, constraints, authority, and evidence through the conversation and artifact references. For sustained work, use the active client's native goal or plan mechanism when available. Do not create duplicate workflow state, custom gates, hooks, or background processes.
>
> Never imitate a child contract inside `loop`. Delegate the work, accept its artifact only when its readiness rules are met, and reroute from evidence. Stop when the requested endpoint is complete, the user stops or changes tasks, progress requires new authority, or remaining work has diminishing returns.
<!-- loop-skill-body:end -->

## Raycast

导入 [`skills/loop/assets/raycast-snippets.json`](./skills/loop/assets/raycast-snippets.json)，即可使用 `;lp`、`;dg`、`;dd` 和 `;db`。安装 Skill 不会修改 Raycast。

## 更新

已安装副本是快照：

```bash
npx skills@latest update loop deep-grill deep-design deep-build design-taste-frontend -g -y
```

如果客户端已经缓存 Skill 元数据，请重新加载或新建任务。

## 许可证

本 bundle 使用 [MIT License](./LICENSE)。`deep-grill` 保留已整合上游源码的归属信息，见 [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md)。`design-taste-frontend` 从 [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill) 独立安装，不属于本 bundle，其许可证与更新由上游管理。
