---
title: 'Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of
  Zero-Shot Agentic and Fine-Tuned Systems'
title_zh: 土耳其多模态视频事实核查：新数据集及零样本Agent与微调系统对比
authors:
- Azra Açıl
affiliations:
- Queen Mary University of London (QMUL)
arxiv_id: '2611.08651'
url: https://arxiv.org/abs/2611.08651
pdf_url: https://arxiv.org/pdf/2611.08651
published: '2026-11-05'
collected: '2026-11-09'
category: Agent
direction: 多模态事实核查 · Agent与微调系统对比
tags:
- Fact-Checking
- Multimodal
- Low-Resource-Language
- LoRA
- Agent
one_liner: 发布首个土耳其语多模态视频事实核查数据集TeViD，对比零样本Agent与LoRA微调的核查系统效果
practical_value: '- 低资源垂直场景构建数据集时，可复用「权威来源采集+公开数据集翻译+合成样本补全」方案解决类别不平衡问题，适配小语种/细分领域任务需求

  - 多模态内容合规核查类Agent开发时，可新增语义一致性校验、5W1H问题管理、排除目标站点的双语证据检索模块，避免数据泄露同时提升判断准确率

  - 资源受限的垂直分类任务中，可对比零样本Agent框架与LoRA小参数微调方案，根据算力成本、响应时延、效果要求选择最优落地路径'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
短视频多模态虚假信息在社交平台传播速度快，现有自动化事实核查系统多针对英文文本，土耳其语等低资源语言的多模态核查工具极度稀缺。
### 方法关键点
1. 构建首个土耳其语多模态视频事实核查数据集TeViD，从IFCN认证的官方核查站点采集原始数据，补充Snopes数据集翻译样本与合成样本缓解类别不平衡问题；
2. 基于同源开源基座搭建两套核查pipeline：① 3MFact-TR零样本Agent方案，适配多角色3MFact框架，新增语义不一致检测、5W1H问题管理、排除核查站点的双语证据检索三个自定义模块；② 用LoRA微调Qwen2.5-7B的闭卷判决方案。
### 关键结果
完成两套系统在accuracy、macro F1、True类F1、True类召回指标上的对比，通过消融实验验证了新增三个模块的有效性。
