---
title: 'LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents'
title_zh: LUMOS：面向可访问性接地AI Agent的语义操作系统层
authors:
- Yogeswar Reddy Thota
affiliations:
- University of Texas at Dallas
arxiv_id: '2606.30697'
url: https://arxiv.org/abs/2606.30697
pdf_url: https://arxiv.org/pdf/2606.30697
published: '2026-06-28'
collected: '2026-07-01'
category: Agent
direction: Agent 操作系统语义交互层
tags:
- LLM Agents
- Accessibility API
- UI Automation
- Semantic Grounding
- Agent Interface
one_liner: 基于系统可访问性API构建语义交互层，降低Agent操作桌面的token消耗与歧义
practical_value: '- 构建电商/广告投放自动化Agent时，可复用从UIA/DOM提取语义蓝图+稳定ID的思路，替代截图+OCR方案，大幅降低token开销和识别错误率

  - Agent动作空间可参考约束式设计，用通用可见UI原语替代应用定制脚本，降低跨场景适配成本，同时加安全校验层避免高危操作

  - 做光标/触点相关的交互Agent（如用户操作意图预判）时，可复用`ElementFromPoint`语义指针接地思路，直接从系统API拿元素语义，无需依赖视觉模型

  - 电商后台RPA升级可基于这套语义层，把传统固定脚本RPA改成LLM驱动的动态自动化系统，适配非固定流程的运营任务'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有桌面操作系统UI面向人类视觉交互设计，当前PC/网页端Agent普遍依赖截图+VLM解析UI，存在token成本高、视觉歧义多、坐标误差大、延迟高的问题；而操作系统原生的Accessibility API、DOM树已经包含Agent所需的结构化语义信息，此前未被有效利用。

### 方法关键点
- 感知层：对接Windows UIA框架与浏览器可访问性树，提取UI元素的稳定ID、角色、名称、值、坐标、可执行动作，生成过滤冗余视觉信息的紧凑语义蓝图
- 实时语义指针接地：通过系统`ElementFromPoint`类API直接查询光标位置的UI元素语义，替代截图裁剪+VLM解析流程，快速校验动作目标正确性
- 规划层：给LLM输入用户目标、历史记忆、当前语义蓝图，约束LLM仅输出符合固定JSON schema的单步动作，每步执行后重新观测状态，避免幻觉化长脚本
- 动作层：定义通用可见UI原语（点击、输入、按键、打开应用等），仅执行和人类操作等价的可见动作，新增安全白名单拦截高危操作

### 关键结果
原型验证阶段对比截图+OCR方案：语义蓝图token量降低90%+，光标元素识别延迟从数百ms降至数十ms，动作接地准确率提升20%+；debug trace显示语义修复模块可减少80%以上LLM常见操作错误（重复输入、指令照搬、未主动终止等）。

### 核心洞察
可访问性基础设施未来会是AI原生操作系统的核心语义基底，不需要把所有交互感知问题都抛给VLM从像素重新解析。
