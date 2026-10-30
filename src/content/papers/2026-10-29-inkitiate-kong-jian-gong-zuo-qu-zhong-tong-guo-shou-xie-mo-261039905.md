---
title: 'Inkitiate: Initiating and Steering Agent Assistance through Ink in a Spatial
  Workspace'
title_zh: Inkitiate：空间工作区中通过手写墨迹引导Agent辅助的系统
authors:
- Liangwei Wang
- Nan Chen
- Luna K. Qiu
- Zilong Wang
- Fugee Tsung
- Yuyu Luo
- Yuqing Yang
affiliations:
- HKUST(GZ)
- Microsoft Research Asia
- CataX AI
- HKUST
arxiv_id: '2610.39905'
url: https://arxiv.org/abs/2610.39905
pdf_url: https://arxiv.org/pdf/2610.39905
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent人机交互 · 空间工作区墨迹输入
tags:
- Human-AI-Interaction
- Digital-Ink
- Spatial-Workspace
- Agent-Steering
- Knowledge-Work
one_liner: 提出支持手写墨迹输入的空间知识工作区，支持用户通过墨迹直接引导Agent完成知识任务
practical_value: '- 电商运营/商品策划场景可复用交互逻辑：支持运营在活动画布上圈选目标商品、手写营销指令，Agent自动绑定选中商品上下文生成对应文案/活动方案，无需重复输入商品信息

  - Agent交互可解释性设计可直接复用：执行过程中实时暴露理解的用户意图、用到的上下文资源、执行进度，支持随时中断修正，大幅降低用户信任成本，可应用于电商导购Agent、推荐结果解释场景

  - 多轮会话上下文管理思路可迁移：仅用用户显式选中内容+邻近相关内容+关联任务历史作为上下文，既保证相关性又减少token消耗，适合电商推荐、客服Agent的多轮交互场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前空间知识工作区中，手写墨迹仅作为内容载体，无法直接作为Agent指令触发任务；现有Agent交互要么把单次请求作为孤立会话，要么无差别引入全量画布内容导致意图理解偏差，且执行过程不透明、无法中途干预，难以适配连续迭代的知识工作需求。

### 方法关键点
- 输入层支持自由手写墨迹+预定义语义符号（#绑定资源、//指定Agent能力），结合用户显式选中的画布对象作为任务边界，避免无关内容进入上下文
- 执行层实时暴露Agent的理解意图、用到的资源、执行进度，支持用户随时中断，遇到歧义时弹出可选方案或支持用户补充墨迹澄清
- 结果层直接返回可编辑的画布对象，自动贴合当前墨迹位置排版，保留来源溯源信息，支持后续任务直接复用
- 上下文构建仅包含显式提交内容、邻近区域只读内容、关联任务历史，平衡上下文充足性与token开销

### 关键结果
18名受试者参与的测试中，SUS系统可用性平均得分5.93/7，NASA-TLX workload各维度得分均低于3/7（物理需求最低1.78，effort最高2.83）；100%受试者可完成墨迹触发Agent、导入/生成资源任务，89%可完成跨材料分析总结任务。

### 核心结论
面向开放域知识/创意工作的Agent交互，轻量的显式意图绑定+可干预的执行过程，远好于黑盒式的全自动化意图推断。
