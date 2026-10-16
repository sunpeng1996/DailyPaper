---
title: 'OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using
  Agents'
title_zh: OS-Helix：统一GUI交互与代码执行的原生计算机操作智能体
authors:
- Bowen Yang
- Kaiming Jin
- Zichen Ding
- Zhenyu Wu
- Zehao Li
- Zhoumianze Liu
- Kanzhi Cheng
- Fangzhi Xu
- Yanan Sun
- Qiushi Sun
affiliations:
- University of Science and Technology of China
- Shanghai AI Laboratory
- National University of Singapore
- Shanghai Jiao Tong University
- Fudan University
arxiv_id: '2610.22234'
url: https://arxiv.org/abs/2610.22234
pdf_url: https://arxiv.org/pdf/2610.22234
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 桌面操作混合动作空间优化
tags:
- Computer-Using-Agent
- GUI-Code-Hybrid
- RL-for-Agent
- Multimodal-Agent
- SFT
one_liner: 端到端训练的原生计算机操作Agent，统一GUI与代码动作空间，较基线最高提升42.9%
practical_value: '- 做多模态混合工具调用Agent时，不要直接在prompt层拼接工具，优先用混合轨迹SFT做冷启动，避免原有GUI能力退化

  - 涉及短动作（如点击、选择）和长token动作（如代码、长文本生成）的RL优化场景，可复用Step-balanced GSPO，按动作步聚合权重避免长token动作主导优化

  - Agent训练数据生成可参考「应用-工件匹配构造环境+独立探索/评估Agent生成任务」的流水线，降低人工标注成本，同时保证任务可验证

  - 混合动作Agent效果评估可按任务域拆分统计不同模态的动作占比和增益，快速定位能力短板'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有桌面操作Agent分为GUI-only和Code-only两类：GUI Agent在结构化批量操作场景下效率低、易出现视觉定位错误，Code Agent无法处理依赖视觉布局、应用专属UI状态的长尾场景。简单给GUI Agent新增代码工具会导致性能下降（实验中Qwen3-VL-32B加代码后OSWorld成功率从34%降至32%），模态路由能力无法通过prompt级工具拼接获得，必须通过混合数据训练内置到模型中。
### 方法关键点
- 数据层：提出应用-工件组合方案，基于兼容性图匹配版本固定的桌面应用与真实文件工件，生成可复现的Ubuntu执行环境；采用独立探索Agent+评估Agent的流水线生成环境对齐的可验证任务，不限制解决方案模态，最终产出31K高质量过滤SFT样本。
- 训练层：先通过混合轨迹SFT冷启动，让模型学习统一动作空间语义与基础模态路由逻辑；在线RL阶段提出Step-balanced GSPO，按动作步而非原始token数聚合重要性权重，解决长代码动作主导异质动作优化的问题。
### 关键实验
在OSWorld-Verified基准测试中，OS-Helix-27B、OS-Helix-35B-A3B较匹配的Qwen3.5混合基线分别实现35.0%、33.7%的相对提升；OS-Helix-27B-RL进一步相对提升42.9%，成功率达66.44%；跨平台迁移到WindowsAgentArena上成功率达63.87%，优于部分基于GPT-5的框架方案。
### 核心结论
混合工具调用能力无法靠prompt级工具拼接获得，必须通过混合数据训练内置路由逻辑，异粒度动作RL训练需要消除token长度偏见才能稳定提升性能
