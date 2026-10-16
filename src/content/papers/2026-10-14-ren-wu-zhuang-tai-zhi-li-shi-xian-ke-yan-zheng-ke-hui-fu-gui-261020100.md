---
title: 'Task-State Governance: A Virtual Machine for Verifiable and Recoverable GUI
  Agent Execution'
title_zh: 任务状态治理：实现可验证可恢复GUI Agent执行的虚拟机
authors:
- Wenkui Yang
- Yiming Hao
- Kai Zhou
- Chengyu Pu
- Yuzhe Zhang
- Jie Cao
- Jin Huang
- Shuai Ma
- Feng Tian
affiliations:
- 中国科学院大学SAIS
- 中国科学院自动化研究所
- 美团
- 北京大学
- 中国科学院软件研究所
arxiv_id: '2610.20100'
url: https://arxiv.org/abs/2610.20100
pdf_url: https://arxiv.org/pdf/2610.20100
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: GUI Agent 可验证可恢复执行治理架构
tags:
- GUI_Agent
- Task_State_Governance
- TaskVM
- Verifiable_Execution
- Recoverable_Execution
one_liner: 提出基于状态契约的TaskVM架构，实现GUI Agent跨端可验证可恢复执行，提升用户管控力与信任
practical_value: '- 落地电商导购、运营自动化类Agent时，可复用执行器与验证器架构分离的设计，操作后独立校验页面真实状态，不依赖Agent自报的执行结果，避免改价、上下架等核心操作出错

  - 可直接复用动作可逆性分类逻辑，将业务操作划分为可逆、可补偿、不可逆三类，回滚时明确告知用户能力边界，禁止对不可逆操作（如订单支付）提供虚假撤销承诺

  - 跨端Agent开发可借鉴GUI-only纯视觉设计，仅用用户可见的页面元素做定位，不依赖DOM ID、接口字段等内部属性，提升动态改版场景下的执行鲁棒性'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前GUI Agent普遍采用计划中心的交互模式，用户仅能管控执行步骤，无法明确指定需保留的状态边界，且Agent自报完成的机制可信度低，执行出错后缺乏明确的恢复方案，难以落地到真实业务场景。
### 方法关键点
- 提出任务状态契约范式，将任务拆解为期望状态、需保留状态、观测状态三部分，仅当最新观测同时满足前两者时才判定任务完成
- 架构上严格分离执行器与独立视觉验证器，验证器仅基于最新页面截图判断结果，不共享执行器的内部状态，杜绝自证完成的问题
- 明确动作可逆性三类划分：可逆、可补偿、不可逆，禁止对不可逆操作提供虚假撤销承诺，降低用户过度信任风险
- 采用GUI-only纯视觉输入输出规范，仅使用用户可见的页面元素，不依赖DOM ID等非公开内部属性，保障跨端兼容性
### 关键实验结果
在36个跨生产力、社交、内容应用的任务实例上测试，对比Direct-CUA、Planner-CUA两个基线：
- 契约严格通过率达58.3%，较Direct-CUA提升16.6%，较Planner-CUA提升23.5%
- 原子谓词平均通过率达87%，较两个基线分别提升14.3%、18%
- 管控密集型任务上通过率达71.4%，优势更显著，但执行耗时为Direct-CUA的2.2倍
### 最值得记住的一句话
用户真正关心的是应用状态的最终变化，而非Agent的执行步骤，将管控对象从执行过程升级为结果状态，是提升Agent落地可用性的核心路径。
