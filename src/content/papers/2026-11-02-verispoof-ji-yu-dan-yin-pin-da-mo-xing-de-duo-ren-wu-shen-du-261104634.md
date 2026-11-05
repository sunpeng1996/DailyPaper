---
title: 'VeriSpoof: Beyond Real or Fake with One Audio LLM'
title_zh: VeriSpoof：基于单音频大模型的多任务深度伪造检测系统
authors:
- Yang Xiao
- Ting Dang
affiliations:
- The University of Melbourne
arxiv_id: '2611.04634'
url: https://arxiv.org/abs/2611.04634
pdf_url: https://arxiv.org/pdf/2611.04634
published: '2026-11-02'
collected: '2026-11-05'
category: Other
direction: 音频大模型 · 深度伪造多任务检测
tags:
- Audio-LLM
- Deepfake-Detection
- Multi-task-Learning
- Parameter-efficient-Fine-tuning
- Open-source
one_liner: 单权重开源音频LLM统一5类深度伪造司法分析任务，公开权重模型性能第一
practical_value: '- 低参微调方案可复用：仅微调约1%参数即可驱动2.85B大模型，适配单24G GPU，可直接迁移到电商多模态内容审核模型的轻量化微调场景

  - 多任务统一架构可借鉴：无需额外任务头、用输出句子置信度做阈值的设计，可用于搭建统一的直播语音、UGC语音、语音广告的合规/真伪校验系统，减少多任务维护成本

  - 可解释决策逻辑可复用：输出可独立验证的决策理由的思路，能解决内容审核场景的结果回溯、误判排查需求，提升业务方对AI决策的信任度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统深度伪造检测器仅能输出真假二元判断，无法满足司法场景需要的生成源归因、伪造片段定位、同源验证等多任务需求，且决策缺乏可校验的依据。

### 方法关键点
- 单音频LLM统一5类深度伪造分析任务，共享全量权重，无需额外添加任务头，直接用输出句子的似然得分作为阈值判断依据
- 决策输出可独立校验的结构化理由，通过反事实样本训练保证决策逻辑与输出证据严格匹配
- 仅微调29.7M参数（占总2.85B参数的1%左右），搭配梯度检查点技术，单张24GB GPU即可完成训练

### 关键结果数字
- VeriSpoof-Plus在14个Speech-DF-Arena测试集上 pooled EER 2.14%，在28个参赛系统中排第3，是公开权重模型中的第1名
- VeriSpoof-Base EER达4.43%，仅为次优公开权重检测器的一半不到
- 同源验证任务EER 6.2%，可识别训练中未见过的生成器的同源样本
- 可验证理由逻辑对部分伪造样本的检出率达99.6%，远高于单步判断的78.4%
