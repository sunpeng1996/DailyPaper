---
title: 'VIEWCRAFT: Evolving What Multimodal Agents See and How They Read It'
title_zh: VIEWCRAFT：多模态Agent视觉证据接口与阅读流程协同进化框架
authors:
- Binxiao Xu
- Ruichuan An
- Bocheng Zou
- Weihua Du
- Xinyu Wei
- Hangyu Guo
- YiFan Zhang
- Renye Yan
- Chengqi Duan
- Hang Hua
affiliations:
- PKU
- MIT-IBM Computing Research Lab
- UW-Madison
- CASIA
- CMU
arxiv_id: '2610.15915'
url: https://arxiv.org/abs/2610.15915
pdf_url: https://arxiv.org/pdf/2610.15915
published: '2026-10-10'
collected: '2026-10-14'
category: Agent
direction: 多模态Agent · 技能自动进化
tags:
- Multimodal Agent
- Skill Evolution
- Evidence Interface
- Frozen LLM
- Prompt Optimization
one_liner: 冻结基座权重下联合优化多模态Agent的输入视图与阅读规则，提升任务表现同时降低输入token消耗
practical_value: '- 电商多模态客服/商品理解Agent可复用该联合优化逻辑：冻结大模型权重，同时优化输入视觉素材的裁剪/拼接/标注规则和对应的阅读prompt，在不换模型的前提下提升任务准确率，降低推理token成本

  - 长视频/直播内容理解场景可借鉴其frame选择+标注+阅读规则绑定的思路，比如直播带货高光片段提取任务，不用微调模型，只需要迭代选帧规则、帧拼接模板和对应的解读prompt，就能快速迭代效果

  - 多源信息聚合类推荐场景（比如用户意图匹配多模态素材的内容推荐）可参考其接口投影机制：如果联合优化的规则效果下降，单独复用其中的视觉素材预处理规则和原有prompt搭配，避免有用的预处理逻辑被浪费'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent技能优化多局限于文本prompt或工具逻辑调整，忽略输入证据呈现形式（如视频选帧、图像排版）与阅读规则的耦合关系，单独优化单侧收益有限，且微调基座模型成本高、技能复用性差。
### 方法关键点
- 技能拆分为可执行证据接口（负责观测数据的选择、变换、组织，如关键帧筛选、带时间标拼接、计数网格叠加）和对应阅读流程（解读视图的规则，如帧读取顺序、分区计数逻辑）两部分，全程冻结基座LLM权重
- 基于失败trace生成联合优化提案，通过重放校验和配对评估保留有效修改；新增接口投影机制：若联合提案整体效果下降但证据支撑度未降低，单独将新接口与原有阅读流程搭配重测，避免有用视觉编辑逻辑被丢弃
- 保留规则为任务分数提升，或分数不变但证据支撑度提升，优先降低输入token消耗
### 关键实验
在8个多模态基准（涵盖VQA、视频理解、表单理解等场景）测试，比直接调用基座平均提升6.1pp任务得分；5个多源任务上，学习到的接口比初始技能少用8~15%输入token，相同token预算下仍比直接调用高5.2pp；技能可跨基座迁移，所有迁移场景都比目标基座直接调用高至少1.5pp
### 核心结论
多模态Agent的可复用技能应该是「可执行证据接口+对应阅读规则」的绑定对，而非孤立的文本prompt或视觉处理逻辑
