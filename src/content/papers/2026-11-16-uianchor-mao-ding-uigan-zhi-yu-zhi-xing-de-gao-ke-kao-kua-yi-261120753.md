---
title: 'UIAnchor: Anchoring UI Perception and Action Execution for Reliable Service-Composed
  Mobile Task Automation with GUI Agents'
title_zh: UIAnchor：锚定UI感知与执行的高可靠跨应用移动GUI自动化多智能体系统
authors:
- Wentao Zhou
- Sicong Liu
- Zimu Zhou
- Yimeng Duan
- Yongyan Cai
- Weiye Wu
- Teng Li
- Daqing Zhang
- Zhiwen Yu
affiliations:
- 西北工业大学
- 香港城市大学
- 巴黎理工学院
- 哈尔滨工程大学
arxiv_id: '2611.20753'
url: https://arxiv.org/abs/2611.20753
pdf_url: https://arxiv.org/pdf/2611.20753
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: GUI Agent 移动任务自动化架构
tags:
- GUI Agent
- Multi-Agent
- LoRA
- Closed-loop Control
- Perception Anchoring
one_liner: 提出双阶段UI解析+元控制器架构的多智能体GUI系统，大幅提升跨应用长步长任务成功率
practical_value: '- 交互类Agent（如电商APP智能导购、自动化运营工具）可复用双阶段UI感知方案：先用SAM2做无训练分割提升小元素召回，再结合上下文消歧义，比单VLM端到端解析准确率更高，可零适配新APP

  - 长步长任务Agent可加轻量元控制器层，做动作前置信度校验、动作后状态差分核验，加针对性恢复逻辑，无需全流程重规划即可大幅降低错误传播概率

  - 多角色Agent部署可采用共享主干+Multi-LoRA方案，无需运行多个独立大模型，资源占用显著降低，同时保证各角色专业化性能，适合端边部署场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有基于LLM/VLM的移动GUI Agent在跨应用、长步长、小尺寸UI元素的复杂任务上可靠性极低，31.5%的失败来自UI元素漏识别/误识别，27.8%来自开环执行导致的错误传播，无法满足驾驶、无障碍等强可靠性场景需求，也难以落地电商APP自动化运营、用户交互助理等业务。

### 方法关键点
- 双阶段UI解析：第一阶段用SAM2做无训练分割+OCR提取全量UI元素，实现移动端<100×100px小元素召回率91.47%；第二阶段结合相邻文本、局部布局上下文推断元素功能语义，消歧义同形异义图标
- 元控制器闭环执行：维护包含toast、弹窗、页面跳转等系统事件的运行时元状态内存，执行前校验目标元素grounding置信度，低于阈值则触发重解析/重规划；执行后通过前后帧差分+元状态变化判断动作结果，匹配4类错误触发针对性恢复，避免错误累积
- 轻量化部署：UI解析用独立轻量pipeline，规划器、执行器、元控制器共享4B参数量Qwen3-VL主干，通过Multi-LoRA做角色专业化，仅需83M额外参数，大幅降低部署成本

### 关键结果
在L4级最难实用任务（20-30步、跨应用、目标元素<100×100px）上，成功率比GPT-4o高31.5%，比Mobile-Agent-v3高16.6%；单步延迟约2s（和人类操作速度相当），比基线降低75.5%，能耗降低52.4%，可泛化到未见过的APP和跨平台GUI。

**最值得记住的一句话**：高可靠交互类Agent场景下，显式拆分感知、执行、校验模块的结构化方案，比端到端单模型性价比高得多，小模型加合理流程设计也能超过大模型的任务表现。
