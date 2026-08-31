---
title: 'CrabOS: An Operating System for Human-AI Co-inhabitation'
title_zh: CrabOS：面向人机共居的操作系统
authors:
- Qi Yang
- Yun Ma
affiliations:
- Institute for Artificial Intelligence, Peking University
arxiv_id: '2608.28165'
url: https://arxiv.org/abs/2608.28165
pdf_url: https://arxiv.org/pdf/2608.28165
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 人机协作操作系统设计
tags:
- Human-AI Collaboration
- Agent OS
- Task Orchestration
- Memory Management
- Seamless Task Handoff
one_liner: 提出人机共居概念，设计实现共享工作状态与接口的CrabOS，消除人机任务切换的桥接成本
practical_value: '- 可借鉴工作状态自然语言文本化设计，让电商运营、推荐Agent共享任务上下文（如活动策划、选品中间态），避免跨角色切换的信息对齐成本

  - 参考统一可审计能力入口设计，将推荐系统的召回、排序、生成等能力封装为统一调用接口，人机调用走同一鉴权、留痕链路，便于追溯操作效果

  - 复用L0对象层思路，将推荐/广告的用户画像、任务、历史交互统一为可寻址结构化文本对象，降低多Agent（选品/文案/投放Agent）的上下文同步成本

  - 电商复杂运营任务的多Agent编排无需单独开发调度逻辑，可基于可订阅状态对象组合实现任务触发、回调、进度同步，降低开发成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前AI Agent与人类的工作环境相互隔离，跨角色任务切换需要开发场景专属接口或用户手动迁移状态，协作成本随任务复杂度上升急剧增加，无法支撑人机交替主导的复杂长链路任务。
### 方法关键点
- 三大设计原则：工作数据序列化为人类与LLM均可直接读写的结构化自然语言文本对象；人机操作同一套可寻址的工作对象（含文件、任务、当前窗口、选中内容等动静态状态）；所有执行主体（人类/Agent/应用）通过同一可审计的统一入口调用系统能力，消除AI专属工具封装层。
- 四层架构：L0对象层将所有状态持久化为8类可寻址文本对象，无需额外API即可直接读写；L1系统服务层提供统一鉴权、调度、Agent Runtime、向量索引等基础能力；L2 Shell层同时作为人类操作入口与AI感知人类工作状态的接口；L3应用层所有应用与Agent对等，均可调用系统基础能力。
### 关键结果
通过四类核心场景案例验证：相比主流Agent系统，记忆管理策略可独立作为应用插拔，无需修改内核；所有应用原生支持上下文感知，无需每个场景单独开发感知逻辑；多Agent编排能力可直接通过对象原语组合实现，无需额外开发调度机制；自动生成语义操作粒度的全链路trace，无需单独开发埋点。

**最值得记住的一句话**：人机共居的核心是让人类与AI共享工作状态的表示与访问接口，把人机协作能力从应用层下沉到操作系统原生能力。
