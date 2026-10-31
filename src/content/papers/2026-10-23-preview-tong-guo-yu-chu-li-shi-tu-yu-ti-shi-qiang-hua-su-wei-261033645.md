---
title: 'PreView: Enhancing GUI Grounding with Preprocessed Views and Cues'
title_zh: PreView：通过预处理视图与提示强化GUI元素定位能力
authors:
- Wenjun Hou
- Kaishuai Xu
affiliations:
- Independent Researcher
arxiv_id: '2610.33645'
url: https://arxiv.org/abs/2610.33645
pdf_url: https://arxiv.org/pdf/2610.33645
published: '2026-10-23'
collected: '2026-10-31'
category: Agent
direction: Agent GUI操作 · 多模态输入预处理
tags:
- GUI Grounding
- LLM Agent
- Multimodal
- Input Enhancement
- Zero Tuning
one_liner: 无需微调原有多模态模型，通过轻量预处理模块生成视图与提示提升GUI定位准确率
practical_value: '- 开发电商端侧操作Agent（如自动上架、竞品数据爬取Agent）时，无需微调多模态大模型，新增轻量预处理模块即可提升界面控件识别准确率，大幅降低训练与迭代成本

  - 可复用「局部视图放大+视觉/文本辅助提示」的预处理范式，优化推荐系统多模态内容理解（如商品图细节识别、广告素材元素定位）任务的输入质量

  - 业务场景中若使用冻结大模型做推理，可直接借鉴输入侧增强的思路，无需调整大模型权重即可快速提升效果，适配业务快速迭代需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
GUI grounding是智能Agent执行界面操作的核心能力，现有模型在高分辨率、布局密集的复杂界面下对小控件的定位准确率偏低，直接裁剪放大局部视图仍存在目标歧义，而微调大模型的成本高、迭代慢。

### 方法关键点
1. 设计无需修改原有grounding模型权重的轻量预处理模块PreView，输出两类互补输入特征：面向定位的任务相关视图、面向目标理解的候选专属提示
2. 轻量辅助模型预测并优化裁剪中心，放大局部视图提升细节可见度，同时生成带位置提示的红圈视觉标记、描述候选控件身份/功能的文本提示，共同输入冻结的多模态模型完成推理

### 关键结果
在5个基准测试集上，无需微调Qwen3-VL-2B、OS-Atlas-4B、Qwen3-VL-4B等主流多模态模型，即可显著提升其平均GUI定位准确率
