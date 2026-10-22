---
title: 'Multimodal Embodied Agents: A Unified Capability-centric Perspective from
  Computer-Use to Robot-Use'
title_zh: 多模态具身Agent：从计算机使用到机器人使用的能力统一框架
authors:
- Yanzhe Chen
- Ziyi Yang
- Jifeng Zhu
- Qiming Huang
- Ruihe An
- Peiyao Xu
- Hesen Yang
- Runda Liu
- Chang Gong
- Zhijun Cao
affiliations:
- Show Lab, National University of Singapore
arxiv_id: '2610.30108'
url: https://arxiv.org/abs/2610.30108
pdf_url: https://arxiv.org/pdf/2610.30108
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: 具身Agent · 跨域能力统一评估
tags:
- Multimodal Embodied Agent
- PAPAV
- Capability Framework
- Computer-Use Agent
- Robotics System
one_liner: 提出PAPAV能力框架，打通计算机使用类Agent与机器人系统的跨域评估逻辑
practical_value: '- 搭建电商场景交互类Agent（如AR导购、后台自动化操作Agent、仓储拣货机器人）时，可直接复用PAPAV五模块拆分逻辑设计交互闭环，无需从零梳理功能边界

  - 评估长链路交互Agent时，除整体任务成功率外，需补充Anticipate、Verify两个隐性能力的专项测试，避免仅靠结果指标低估泛化风险

  - 设计涉及物理操作的业务Agent（如线下门店导购机器人、智能仓储作业Agent）时，需将不可逆、实时耦合等物理约束提前嵌入Plan模块的前置校验规则，降低错误操作的业务损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent（MMA）多聚焦数字界面操作，机器人系统（RS）多聚焦物理空间控制，两类系统的评估体系各自独立，缺乏统一的能力对比框架，既无法横向对齐能力差异，也难以为跨域多模态具身Agent（MMEA）的设计提供可复用的范式。

### 方法关键点
- PAPAV统一能力框架按交互闭环的功能属性拆分为Perceive（状态感知）、Anticipate（动作效果预判）、Plan（可行路径规划）、Act（动作执行）、Verify（结果校验）5个独立模块，不绑定具体实现架构，可适配数字、物理两类交互场景。
- 归纳物理交互场景的5类核心约束：部分可观测、可模拟性有限、动作不可逆、实时耦合、结果难校验，明确从数字交互向物理交互迁移的能力要求差异。
- 构建覆盖64个主流基准的能力标注体系，区分显式能力评估与仅通过任务结果推断的隐式能力评估。

### 关键结果
对64个基准的统计显示，当前超90%的显式评估集中在Act模块，仅5个基准覆盖Anticipate、3个覆盖Verify，两类核心隐性能力的评估存在明显空白。

### 核心结论
具身Agent的能力评估不能只看最终任务成功率，拆解到交互闭环的每个功能模块才能精准定位能力短板，支撑可落地的系统迭代。
