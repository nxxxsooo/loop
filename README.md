<p align="right"><a href="./README.en.md">English</a></p>

<p align="center">
  <img src="./assets/grill-loop-launch-cn-poster.png" alt="grill-loop——让循环跟着工作走" width="560">
</p>

<h1 align="center">grill-loop</h1>

<p align="center"><strong>让循环跟着工作走。</strong></p>

<p align="center">
  一个显式路由器，每次只选一个有价值的能力。<br>
  遵循它自己的契约，再根据变化重新选择。
</p>

<p align="center">
  <a href="#安装"><img src="https://img.shields.io/badge/安装-skills.sh-111820?style=flat-square" alt="通过 skills.sh 安装"></a>
  <a href="https://github.com/nxxxsooo/grill-loop/releases"><img src="https://img.shields.io/github/v/release/nxxxsooo/grill-loop?style=flat-square&color=5eead4" alt="最新版本"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/许可证-MIT-5eead4?style=flat-square" alt="MIT 许可证"></a>
</p>

## 安装

一次安装包含 `grill-loop`、`grilling` 和 `deep-grill`：

```bash
npx skills@latest add nxxxsooo/grill-loop --skill '*' -g -y
```

| Skill | 作用 | 来源 |
|---|---|---|
| `grill-loop` | 根据当前目标和产物选择下一项能力 | 本仓库 |
| `grilling` | 一次一个问题，访谈用户脑中的关键选择 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) |
| `deep-grill` | 自主调查、反驳和修正方案 | [nxxxsooo/deep-grill](https://github.com/nxxxsooo/deep-grill) |

Wayfinder、OpenSpec、Open Design、taste 和其他专家能力按当前环境选用，不强制打包。

当 grill-loop 选择 `wayfinder` 时，它遵循该能力的共享 Issue 决策地图契约。若路线已经明确、工作可在单个 agent 会话内完成，则不创建 Wayfinder 地图；需要持久化变更记录时，仍可直接进入 OpenSpec。

当 grill-loop 选择 OpenSpec 时，会先检查目标项目是否已为当前客户端初始化。缺失配置只通过 `openspec init <project-root> --tools <active-client>` 生成，路由器不会手工拼装 OpenSpec 文件。OpenSpec CLI 仍需由当前环境提供；使用生成的入口前，应按 CLI 提示重新加载或重启客户端。

这里的 `--skill '*'` 表示安装仓库中的三个 skill；`--all` 还会安装到所有受支持的 agent，不是同一个意思。

然后在任意任务中明确说：

> 使用 $grill-loop 继续这个任务。

grill-loop 只在被点名时运行。它不会自动触发，也不会强迫所有关联能力都执行。

### 可选：Raycast snippets

如果使用 Raycast，可通过 Raycast 的「Import Snippets」命令导入[随包提供的 snippets](./skills/grill-loop/assets/raycast-snippets.json)：

| Skill | 关键词 |
|---|---|
| `grilling` | `;gr` |
| `deep-grill` | `;dg` |
| `grill-loop` | `;lp` |

这些 snippets 会粘贴完整提示词，适用于任何文本输入框。导入是可选操作；安装 skill 不会修改用户的 Raycast 数据。重复项由 Raycast 在导入时跳过，具体行为参见 [Raycast 官方导入说明](https://manual.raycast.com/import-export)。

## 为什么需要它

真实工作不会沿着一套固定方法前进。缺失的产品选择可能需要 `grilling`；成形方案可能需要 `deep-grill`；跨越多个会话的路线迷雾可能需要 `wayfinder`；已成形的持久变更适合进入 OpenSpec；apply-ready 的用户界面可能仍需要 Open Design 原型和 taste 复核。

grill-loop 只拥有路由决定。它选择当前最小且有价值的能力，遵循该能力自己的契约，传递必要上下文，再重新判断下一步。

## 按答案所在位置路由

| 当前缺口 | 适合的下一步 |
|---|---|
| 意图、优先级、风险容忍或 taste 只存在于用户这里 | `grilling` |
| 方案或决策需要自主调查和对抗审查 | `deep-grill` |
| 目标或路线仍有大量决策迷雾，工作超过一个 agent 会话，且需要共享 Issue 决策地图 | `wayfinder` |
| 改动已足够成形，应该进入持久探索、规格、实施或归档 | OpenSpec |
| 工作已经明确、单个 agent 会话可完成，且不需要持久变更记录 | 直接执行或使用当前客户端的轻量计划 |
| 规格已可实施，但用户界面结构或视觉方向仍未解决 | Open Design 或其他原型能力 |
| 可评审的前端或品牌原型需要视觉方向或批评 | `design-taste-frontend` 或对应设计专家 |
| 其他专家更适合当前动作 | 对应 Skill 或工具 |

这些是选项，不是阶段。工作变化时，可以跳过、重复、重排、返回或停止。

OpenSpec 输出「ready for `/opsx-apply`」只是新的证据，不是 Loop 的终点。若实现仍依赖未解决的用户界面设计，先把规格交给 Open Design 形成可评审原型，再按适用范围交给 taste 或其他设计专家复核；将确认后的结构、状态与视觉决策回写 OpenSpec 的 design 和 tasks，重新确认 apply-ready 后再实施。纯后端、设计已明确或没有重要设计面的变更直接跳过这条支路。

当后续工作适合用持久 goal 推进时，grill-loop 会在当前交接中自然提出一张简洁、可裁剪的 goal card：

```text
Goal:
Project / sources of truth:
Boundaries (may change / must preserve):
Done when:
Must-pass real scenarios:
```

确实不适用的字段可以省略。用户同意整张 card 后，它调用当前客户端已有的原生 goal 机制，并持续选择下一项有价值的能力，直到目标达成；只有继续推进需要新的用户输入或授权时才暂停。它不维护自己的 goal 状态。否则，请求完成或继续循环的收益已经很低即可停止。

<p align="center">
  <img src="./assets/grill-loop-detail.webp" alt="一根青绿色编织绳穿过精密加工的石墨门件" width="440">
</p>

## 完整契约

路由器本身只有四段话。以下内容与 [`skills/grill-loop/SKILL.md`](./skills/grill-loop/SKILL.md) 保持逐字同步：

<!-- grill-loop-skill-body:start -->
> # Grill Loop
>
> Follow the user's goal and the latest evidence or artifacts. Choose the smallest next useful capability, load and follow its own contract, then reassess from what changed. Treat a capability's suggested next command as evidence, not as the loop's decision; reassess before relaying or acting on it. Briefly explain each transition; the user may choose the next capability at any time.
>
> Use `grilling` when a material answer lives only in the user's intent, priorities, risk tolerance, or taste. Use `deep-grill` when a plan or decision needs autonomous investigation and adversarial review. Use `wayfinder` when the destination or route remains too uncertain and expansive for one agent session and needs a shared issue-tracker map of decision tickets. When its decisions make the way coherent enough for a durable change, reassess whether OpenSpec is the next move. Use OpenSpec when the work should enter or continue durable exploration, specification, implementation, or archival. Before the first OpenSpec move, resolve the intended project root and verify both its OpenSpec project state and active-client integration. If either is missing, initialize or add the client only through `openspec init <project-root> --tools <active-client>`; name all intended clients in the comma-separated `--tools` value when appropriate. Never hand-create or copy generated OpenSpec commands, skills, or bootstrap state. Follow the CLI's reload or restart instruction before invoking the generated entry point. If the CLI is unavailable, explain the prerequisite and request installation authority instead of simulating OpenSpec. When an apply-ready change still has unresolved user-facing design, use Open Design or another prototyping capability to make it reviewable, then use `design-taste-frontend` where its scope fits or another design specialist. Feed accepted decisions back into the OpenSpec design and tasks before implementation; skip this route when no material design decision remains. If the work is already clear, small enough for one agent session, and needs no durable change record, execute directly or use the active client's lightweight planning rather than forcing either Wayfinder or OpenSpec. Use another available skill or tool when it is a better next move.
>
> Treat these as options, not stages. Skip, repeat, reorder, or return to them freely. Load only what the current move needs. Carry forward the goal, confirmed decisions, constraints, and artifact references, but impose no shared output format and maintain no duplicate workflow state.
>
> Preserve every capability's scope, authority, and safety boundaries. Add no custom gates, hooks, background processes, or state files. When sustained work needs a goal, propose this adaptable card in the current transition: `Goal`, `Project / sources of truth`, `Boundaries (may change / must preserve)`, `Done when`, and `Must-pass real scenarios`; omit irrelevant fields. After user approval, register it with the active client's native goal mechanism when available and keep routing until it is met; pause only for new user input or authority. Keep no goal state of your own. Otherwise, stop when the request is fulfilled or returns diminish.
<!-- grill-loop-skill-body:end -->

## 边界

- 不增加强制顺序或生命周期。
- 不增加统一输出格式或重复任务状态。
- 不增加自定义门禁、hook、后台进程或状态文件。
- 用户同意提议后，原生客户端可以持久推进 goal；grill-loop 不复制 goal 状态。
- 不扩大用户授权，也不绕过被选能力的契约。
- 不自动触发。

## 更新

已安装副本不会自动跟随仓库变化：

若现有副本来自 `v1.2.0` 或更早的单 skill 布局，旧 lock 仍指向仓库根目录的 `SKILL.md`。首次迁移到三 skill bundle 时，请重新绑定一次来源：

```bash
npx skills@latest add nxxxsooo/grill-loop --skill '*' -g -y
```

迁移后，日常更新使用：

```bash
npx skills@latest update grill-loop grilling deep-grill -g -y
```

项目级安装把 `-g` 换成 `-p`。

## 许可证

本仓库与 `deep-grill` 使用 [MIT](./LICENSE)。打包的 `grilling` 保留 Matt Pocock 的 MIT 许可与来源，见 [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md)。
